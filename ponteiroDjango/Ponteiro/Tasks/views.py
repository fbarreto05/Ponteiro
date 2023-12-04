from django.shortcuts import render
from .models import User
from .models import Group
from .models import groupLinkedList
from .models import groupListNode
from .models import userTreeNode
from .models import userBinarySearchTree
from django.http import HttpResponse
from django.shortcuts import redirect
import os
from shutil import copyfile
from django.conf import settings
from PIL import Image
from django.views.decorators.cache import cache_control
import secrets

titlelanguage = 'pt'

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def title(request):
    global titlelanguage
    if request.GET.get('language'):
        titlelanguage = request.GET.get('language')
    return render(request, f'{titlelanguage}/titleScreen.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    global titlelanguage
    error = request.GET.get('error')
    return render(request, f'{titlelanguage}/loginScreen.html', {'error' : error})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    global titlelanguage
    error = request.GET.get('error')
    return render(request, f'{titlelanguage}/registerScreen.html', {'error' : error})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def registerValidate(request):
    id = request.POST.get('userid')
    if request.FILES.get('picture') == None:

        profile_directory = os.path.join(settings.BASE_DIR, f'media/user_profiles/{id}/profilePicture')
        os.makedirs(profile_directory, exist_ok=True)

        default_picture_path = os.path.join(settings.BASE_DIR, 'media', 'anonymous.png')
        copyfile(default_picture_path, os.path.join(profile_directory, 'anonymous.png'))

        picture = f'user_profiles/{id}/profilePicture/anonymous.png'
    else:
        picture = request.FILES.get('picture')
        try:
            img = Image.open(picture)
            img.verify()
        except Exception as e:
            return redirect('/ponteiro/register/?error=1')

    name = request.POST.get('username')
    description = request.POST.get('userdescription')
    password = request.POST.get('userpass')
    language = titlelanguage
    
    newUser = User.objects.filter(id = id)
    if len(newUser) > 0:
        return redirect('/ponteiro/register/?error=2')

    if id.strip() == '' or password.strip() == '' or name.strip() == '':
        return redirect('/ponteiro/register/?error=3')
    
    if any(char in id for char in [' ', '<', '>', ':', '"', '/', '\\', '|', '?', '*']):
        return redirect('/ponteiro/register/?error=4')
    
    if len(id.strip()) < 5 or len(password.strip()) < 5 or len(name.strip()) < 5:
        return redirect('/ponteiro/register/?error=5')
    if len(id.strip()) > 20 or len(password.strip()) > 20:
        return redirect('/ponteiro/register/?error=6')
    if len(name.strip()) > 80:
        return redirect('/ponteiro/register/?error=7')
    if len(description) > 800:
        return redirect('/ponteiro/register/?error=8')

    newGroupNode = groupListNode(data = None, next = None)
    newGroupNode.save()

    newGroupList = groupLinkedList(head = newGroupNode)
    newGroupList.save()

    newUser = User(picture=picture, name=name, id=id, description=description, password=password, language=language, groupsList = newGroupList)
    newUser.save()

    return redirect('/ponteiro/register/?error=0')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loginValidate(request):
    id = request.POST.get('userid')
    password = request.POST.get('userpass')

    if id.strip() == '' or password.strip() == '':
        return redirect('/ponteiro/login/?error=1')

    newUser = User.objects.filter(id = id).filter(password = password)
    if len(newUser) == 0:
        return redirect('/ponteiro/login/?error=2')
    
    request.session['User'] = newUser[0].id
    return redirect(f'/ponteiro/{id}/home')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request, id):
    if request.session.get('User') == id:
        newUser = User.objects.filter(id = id)

        groupPics = []
        groupList = []
        idList = []
        groups = False
   
        if not newUser[0].groupsList.isEmpty():
            for groupData in newUser[0].groupsList.traverse():
                if groupData: groupPics.append(groupData.picture), groupList.append(groupData.name), idList.append(groupData.id)
            groups = True
            print(groupPics[0])
            groupList = zip(groupPics, groupList, idList)
        else: groupList = "Você ainda não está em nenhum grupo!"

        theme = newUser[0].theme
        language = newUser[0].language
        pictureShow = newUser[0].picture
        error = request.GET.get('error')
        return render(request, f'{ language }/homeScreen.html', {'picture' : pictureShow, 'id' : id, 'theme' : theme, 'groupList' : groupList, 'groups' : groups, 'error' : error})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profile(request, id):
    if request.session.get('User') == id:
        newUser = User.objects.filter(id = id)
        theme = newUser[0].theme
        language = newUser[0].language
        pictureShow = newUser[0].picture
        nameShow = newUser[0].name
        idShow = newUser[0].id
        descriptionShow = newUser[0].description
        passwordShow = newUser[0].password
        error = request.GET.get('error')
        return render(request, f'{ language }/profileScreen.html', {'picture' : pictureShow, 'name' : nameShow, 'id' : idShow, 'description' : descriptionShow, 'password' : passwordShow, 'error' : error, 'theme' : theme}) 
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profileedit(request, id):
    if request.session.get('User') == id:
        error = request.GET.get('error')
        newUser = User.objects.filter(id = id)
        theme = newUser[0].theme
        language = newUser[0].language
        pictureShow = newUser[0].picture
        return render(request, f'{ language }/profileEditScreen.html', {'id' : id, 'error' : error, 'picture' : pictureShow, 'theme' : theme})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profileeditValidate(request, id):
    if request.session.get('User') == id:
        user_instance = User.objects.get(id=id)

        if 'picture' in request.FILES:
            picture = request.FILES['picture']
            try:
                img = Image.open(picture)
                img.verify()
            except Exception as e:
                return redirect(f'/ponteiro/{id}/profile/edit/?error=1')
            imgpath = user_instance.picture.path
            user_instance.picture = picture

        if 'description' in request.POST:
            user_description = request.POST['description']
            if user_description:
                if (user_description == user_instance.description):
                    return redirect(f'/ponteiro/{id}/profile/edit/?error=4')
                if len(user_description) <= 800:
                    user_instance.description = user_description
                else:
                    return redirect(f'/ponteiro/{id}/profile/edit/?error=2')

        if 'password' in request.POST:
            user_password = request.POST['password']
            if user_password:
                if (user_password == user_instance.password):
                    return redirect(f'/ponteiro/{id}/profile/edit/?error=4')
                if len(user_password.strip()) <= 20 and len(user_password.strip()) >= 5:
                    user_instance.password = user_password
                else:
                    return redirect(f'/ponteiro/{id}/profile/edit/?error=3')

        if (not('picture' in request.FILES) and len(user_description.strip()) == 0 and len(user_password.strip()) == 0):
            return redirect(f'/ponteiro/{id}/profile/edit/?error=4')
        user_instance.save()
        
        if 'picture' in request.FILES:
            os.remove(imgpath)

        return redirect(f'/ponteiro/{id}/profile/edit/?error=0')

    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profiledelete(request, id):
    if request.session.get('User') == id:
        imgpath = User.objects.filter(id = id)[0].picture.path
        dirpath = os.path.dirname(imgpath)
        rootpath = os.path.dirname(dirpath)
        os.remove(imgpath)
        os.rmdir(dirpath)
        os.rmdir(rootpath)
        user = User.objects.filter(id = id)

        if not user[0].groupsList.isEmpty():
            for group in user[0].groupsList.traverse():
                if group.membersList.search(user[0]): group.membersList.delete(user[0])
                if group.adminList.search(user[0]): group.adminList.delete(user[0])
            if group.adminList.isEmpty:
                if not group.membersList.isEmpty:
                    todelete = group.membersList.root.data
                    group.membersList.delete(todelete)
                    group.adminList.insert(todelete)
                else:
                    group.delete()

        User.objects.filter(id = id).delete()
        request.session.flush()
        return redirect('/ponteiro/login/?error=0')
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userSearch(request, id):
    if request.session.get('User') == id:
        newUser = User.objects.filter(id = id)
        theme = newUser[0].theme
        language = newUser[0].language
        pictureShow = newUser[0].picture
        error = request.GET.get('error')
        return render(request, f'{ language }/userSearchScreen.html', {'picture' : pictureShow, 'id' : id,'error' : error, 'theme' : theme})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def searchValidate(request, id):
    if request.session.get('User') == id:
        userSearchId = request.POST.get('usersearchid')

        if userSearchId.strip() == '':
            return redirect(f'/ponteiro/{id}/userSearch/?error=1')
        newUser = User.objects.filter(id = userSearchId).exclude(id = id)
        if len(newUser) == 0:
            return redirect(f'/ponteiro/{id}/userSearch/?error=2')
        else:
            return redirect(f'/ponteiro/{id}/{newUser[0].id}_profile')
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userSearchProfile(request, id, searchid):
    if request.session.get('User') == id:
        yourUser = User.objects.filter(id = id)
        theme = yourUser[0].theme
        language = yourUser[0].language
        picture = yourUser[0].picture
        newUser = User.objects.filter(id = searchid)
        pictureShow = newUser[0].picture
        nameShow = newUser[0].name
        idShow = newUser[0].id
        descriptionShow = newUser[0].description
        return render(request, f'{ language }/userSearchProfileScreen.html', {'picture' : picture, 'pictureSearched' : pictureShow, 'name' : nameShow, 'id' : id, 'idSearched' : idShow, 'description' : descriptionShow, 'theme' : theme})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def notifications(request, id):
    if request.session.get('User') == id:
        newUser = User.objects.filter(id = id)
        screen = request.GET.get('screen')
        language = newUser[0].language
        picture = newUser[0].picture
        theme = newUser[0].theme
        return render(request, f'{ language }/notificationsScreen.html', {'picture' : picture, 'id' : id, 'theme' : theme, 'screen' : screen})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def homeconfig(request, id):
    if request.session.get('User') == id: 
        newUser = User.objects.filter(id = id)
        theme = newUser[0].theme
        language = newUser[0].language
        pictureShow = newUser[0].picture
        return render(request, f'{ language }/homeConfigScreen.html', {'picture' : pictureShow, 'id' : id, 'theme' : theme})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def homeconfigvalidate(request, id):
    if request.session.get('User') == id:
        user_instance = User.objects.get(id=id)
        theme = request.GET.get('themechange')
        language = request.GET.get('languagechange')

        if theme:
            user_instance.theme = theme
        if language:
            user_instance.language = language
        user_instance.save()
        return redirect(f'/ponteiro/{ id }/config')
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request, id):
    if request.session.get('User') == id:
        request.session.flush()
        return redirect('/ponteiro')
    else:
        print()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def createGroup(request, id):
    if request.session.get('User') == id: 
        newUser = User.objects.filter(id = id)
        theme = newUser[0].theme
        language = newUser[0].language
        pictureShow = newUser[0].picture
        error = request.GET.get('error')

        return render(request, f'{ language }/createGroupScreen.html', {'picture' : pictureShow, 'id' : id, 'theme' : theme, 'error' : error})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def createGroupValidate(request, id):
    if request.session.get('User') == id:
        user_instance = User.objects.get(id=id)

        groupID = secrets.token_hex(5)
        if len(Group.objects.filter(id=groupID)) > 0:
            return redirect(f'/ponteiro/{id}/home/createGroup/?error=1')

        if request.FILES.get('picture') == None:
            profile_directory = os.path.join(settings.BASE_DIR, f'media/groups/{groupID}/bannerPicture')
            os.makedirs(profile_directory, exist_ok=True)

            default_picture_path = os.path.join(settings.BASE_DIR, 'media', 'defBanner.png')
            copyfile(default_picture_path, os.path.join(profile_directory, 'defBanner.png'))

            picture = f'groups/{groupID}/bannerPicture/defBanner.png'
        else:
            picture = request.FILES.get('picture')
            try:
                img = Image.open(picture)
                img.verify()
            except Exception as e:
                return redirect(f'/ponteiro/{id}/home/createGroup/?error=2')
        
        name = request.POST.get('name')
        description = request.POST.get('description')

        if name.strip() == '':
            return redirect(f'/ponteiro/{id}/home/createGroup/?error=3')
        elif len(name.strip()) < 5:
            return redirect(f'/ponteiro/{id}/home/createGroup/?error=4')
        elif len(name.strip()) > 80:
            return redirect(f'/ponteiro/{id}/home/createGroup/?error=5')
        elif len(description.strip()) > 800:
            return redirect(f'/ponteiro/{id}/home/createGroup/?error=6')

        admListNode = userTreeNode(data=None, left=None, right=None)
        memberListNode = userTreeNode(data=None, left=None, right=None)
        admListNode.save()
        memberListNode.save()

        admList = userBinarySearchTree(root = admListNode)
        memberList = userBinarySearchTree(root = memberListNode)
        admList.save()
        memberList.save()


        newGroup = Group(picture=picture, name=name, id=groupID, description=description, adminList=admList, membersList=memberList)
        newGroup.save()

        user_instance.groupsList.push(newGroup)
        newGroup.adminList.insert(user_instance)

        return redirect(f'/ponteiro/{ id }/home/createGroup/?error=0')
    
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def groupSearch(request, id):
    if request.session.get('User') == id:
        newUser = User.objects.filter(id = id)
        theme = newUser[0].theme
        language = newUser[0].language
        pictureShow = newUser[0].picture
        error = request.GET.get('error')

        return render(request, f'{ language }/groupSearchScreen.html', {'picture' : pictureShow, 'id' : id,'error' : error, 'theme' : theme})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def groupSearchValidate(request, id):
    if request.session.get('User') == id:
        groupID = request.POST.get('key')

        if groupID.strip() == '':
            return redirect(f'/ponteiro/{id}/home/groupSearch/?error=1')
        groupInstance = Group.objects.filter(id = groupID)
        if len(groupInstance) == 0:
            return redirect(f'/ponteiro/{id}/home/groupSearch/?error=2')
        else:
            return redirect(f'/ponteiro/{id}/{groupInstance[0].id}_group')
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def showGroup(request, id, groupID):
    if request.session.get('User') == id:
        user = User.objects.filter(id = id)
        theme = user[0].theme
        language = user[0].language
        picture = user[0].picture
        error = request.GET.get('error')

        groupInstance = Group.objects.filter(id = groupID)
        groupPicture = groupInstance[0].picture
        groupName = groupInstance[0].name
        groupKey = groupInstance[0].id
        groupDescription = groupInstance[0].description
        return render(request, f'{ language }/showGroupSearchScreen.html', {'picture' : picture, 'banner' : groupPicture, 'groupName' : groupName, 'id' : id, 'groupKey' : groupKey, 'description' : groupDescription, 'theme' : theme, 'error' : error})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def enterGroup(request, id, groupID):
    if request.session.get('User') == id:
        user_instance = User.objects.get(id=id)
        group_instance = Group.objects.get(id=groupID)

        if user_instance.groupsList.search(group_instance.id) == group_instance.id:
            return redirect(f'/ponteiro/{ id }/{ groupID }_group/?error=1')
        else:
            user_instance.groupsList.push(group_instance)
            group_instance.membersList.insert(user_instance)

        return redirect(f'/ponteiro/{ id }/{ groupID }_group/?error=0')
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def groupHome(request, id, groupID):
    if request.session.get('User') == id:
        user_instance = User.objects.get(id=id)
        group_instance = Group.objects.get(id=groupID)

        if user_instance.groupsList.isEmpty():
            return redirect(f'/ponteiro/{ id }/home/?error=1')
        _, current = user_instance.groupsList.search(group_instance.id)

        if current == None:
            return redirect(f'/ponteiro/{ id }/home/?error=1')
        
        user_instance.groupsList.delete(group_instance.id)
        user_instance.groupsList.push(group_instance)
        language = user_instance.language
        picture = user_instance.picture
        groupName = group_instance.name
        groupID = group_instance.id
        theme = user_instance.theme

        return render(request, f'{ language }/groupHomeScreen.html', {'picture' : picture, 'groupName' : groupName, 'groupID' : groupID, 'id' : id, 'theme' : theme, 'language' : language})
    
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def groupData(request, id, groupID):
    if request.session.get('User') == id:
        user_instance = User.objects.get(id=id)
        group_instance = Group.objects.get(id=groupID)

        if user_instance.groupsList.isEmpty():
            return redirect(f'/ponteiro/{ id }/home/?error=1')
        _, current = user_instance.groupsList.search(group_instance.id)

        if current == None:
            return redirect(f'/ponteiro/{ id }/home/?error=1')

        memberList = []
        idList = []
        adminList = []
        admIdList = []
        isAdmin = False

        if not group_instance.membersList.isEmpty():
            for memberData in group_instance.membersList.traverse():
                if memberData: memberList.append(memberData.name), idList.append(memberData.id)
            memberList = zip(memberList, idList)

        for adminData in group_instance.adminList.traverse():
            if adminData: adminList.append(adminData.name), admIdList.append(adminData.id)
        if user_instance.id in admIdList: isAdmin = True
        adminList = zip(adminList, admIdList)

        language = user_instance.language
        picture = user_instance.picture
        groupPicture = group_instance.picture
        groupName = group_instance.name
        groupID = group_instance.id
        theme = user_instance.theme
        groupDescription = group_instance.description
        error = request.GET.get('error')

        return render(request, f'{ language }/groupDataScreen.html', {'picture' : picture, 'banner' : groupPicture, 'groupName' : groupName, 'groupID' : groupID, 'groupDescription' : groupDescription, 'id' : id, 'theme' : theme, 'language' : language, 'memberList' : memberList, 'adminList' : adminList, 'isAdm' : isAdmin, 'error' : error})
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')
    
def groupRemove(request, id, groupID):
    if request.session.get('User') == id:
        user_instance = User.objects.get(id=id)
        group_instance = Group.objects.get(id=groupID)

        if user_instance.groupsList.isEmpty():
            return redirect(f'/ponteiro/{ id }/home/?error=1')
        _, current = user_instance.groupsList.search(group_instance.id)

        if current == None:
            return redirect(f'/ponteiro/{ id }/home/?error=1')
        
        toRemove = User.objects.get(id=request.GET.get('removeId'))

        if id != toRemove.id:
            _, current = group_instance.adminList.search(user_instance)
            if current == None:
                return redirect(f'/ponteiro/{ id }/group/{ groupID }/data/?error=3')
                    
        if not group_instance.membersList.isEmpty():
            _, current = group_instance.membersList.search(toRemove)
            if current: group_instance.membersList.delete(toRemove)

        _, current = group_instance.adminList.search(toRemove)
        if current: group_instance.adminList.delete(toRemove)
        if group_instance.adminList.isEmpty():
            if not group_instance.membersList.isEmpty():
                promotion = group_instance.membersList.root.data
                group_instance.membersList.delete(promotion)
                group_instance.adminList.insert(promotion)
            else:
                toRemove.groupsList.delete(group_instance.id)
                group_instance.delete()
                return redirect(f'/ponteiro/{ id }/home/?error=0')

        toRemove.groupsList.delete(group_instance.id)

        if toRemove.id == id:
            return redirect(f'/ponteiro/{ id }/home/?error=0')
        return redirect(f'/ponteiro/{ id }/group/{ groupID }/data/?error=0')
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')
    
def groupPromote(request, id, groupID):
    user_instance = User.objects.get(id=id)
    group_instance = Group.objects.get(id=groupID)
    
    if request.session.get('User') == id:
        if user_instance.groupsList.isEmpty():
            return redirect(f'/ponteiro/{ id }/home/?error=1')
        _, current = user_instance.groupsList.search(group_instance.id)

        if current == None:
            return redirect(f'/ponteiro/{ id }/home/?error=1')
        
        _, current = group_instance.adminList.search(user_instance)
        if current == None:
            return redirect(f'/ponteiro/{ id }/group/{ groupID }/data/?error=3')
        
        toPromote = User.objects.get(id=request.GET.get('promoteId'))

        _, current = group_instance.membersList.search(toPromote)
        if current: 
            group_instance.adminList.insert(toPromote)
            group_instance.membersList.delete(toPromote)
            return redirect(f'/ponteiro/{ id }/group/{ groupID }/data/?error=1')

    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')
    
def groupDemote(request, id, groupID):
    user_instance = User.objects.get(id=id)
    group_instance = Group.objects.get(id=groupID)
    
    if request.session.get('User') == id:
        if user_instance.groupsList.isEmpty():
            return redirect(f'/ponteiro/{ id }/home/?error=1')
        _, current = user_instance.groupsList.search(group_instance.id)

        if current == None:
            return redirect(f'/ponteiro/{ id }/home/?error=1')
        
        _, current = group_instance.adminList.search(user_instance)
        if current == None:
            return redirect(f'/ponteiro/{ id }/group/{ groupID }/data/?error=3')
        
        toDemote = User.objects.get(id=request.GET.get('demoteId'))

        _, current = group_instance.adminList.search(toDemote)
        if current: 
            group_instance.membersList.insert(toDemote)
            group_instance.adminList.delete(toDemote)
            return redirect(f'/ponteiro/{ id }/group/{ groupID }/data/?error=1')
        
        else: return redirect(f'/ponteiro/{ id }/group/{ groupID }/data/?error=4')
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')
    
def groupErase(request, id, groupID):
    if request.session.get('User') == id:
        group_instance = Group.objects.get(id=groupID)
        user_instance = User.objects.get(id=id)

        if user_instance.groupsList.isEmpty():
            return redirect(f'/ponteiro/{ id }/home/?error=1')
        _, current = user_instance.groupsList.search(group_instance.id)

        if current == None:
            return redirect(f'/ponteiro/{ id }/home/?error=1')
        
        _, current = group_instance.adminList.search(user_instance)
        if current == None:
            return redirect(f'/ponteiro/{ id }/group/{ groupID }/data/?error=3')

        if not group_instance.membersList.isEmpty():
            for member in group_instance.membersList.traverse():
                group_instance.membersList.delete(member)
                user_instance = User.objects.get(id=member.id)
                user_instance.groupsList.delete(group_instance.id)
        for member in group_instance.adminList.traverse():
            group_instance.adminList.delete(member)
            user_instance = User.objects.get(id=member.id)
            user_instance.groupsList.delete(group_instance.id)

        imgpath = group_instance.picture.path
        dirpath = os.path.dirname(imgpath)
        rootpath = os.path.dirname(dirpath)
        os.remove(imgpath)
        os.rmdir(dirpath)
        os.rmdir(rootpath)

        group_instance.delete()
        return redirect(f'/ponteiro/{ id }/home/?error=2')
    else:
        request.session.flush()
        return redirect('/ponteiro/login/?error=3')

# Create your views here.