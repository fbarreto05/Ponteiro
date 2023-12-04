from django.db import models

def user_profile_image_path(instance, filename):
    return f'user_profiles/{instance.id}/profilePicture/{filename}'

def group_image_path(instance, filename):
    return f'groups/{instance.id}/bannerPicture/{filename}'

class groupListNode(models.Model):
        data = models.ForeignKey('Group', on_delete=models.CASCADE, null=True, blank=True)
        next = models.ForeignKey('groupListNode', on_delete=models.CASCADE, null=True, blank=True)

class groupLinkedList(models.Model):
        head = models.ForeignKey('groupListNode', on_delete=models.CASCADE, null=True, blank=True)

        def isEmpty(self):
            return self.head.data is None

        def __find(self, goal):
            current = self.head
            parent = self
            while (current and goal != current.data.id):
                parent = current
                current = current.next
            return parent, current
        
        def search(self, goal):
            if self.isEmpty(): print("Empty list")
            else: return self.__find(goal)

        def __delete(self, goal):
            parent, node = self.search(goal)
            if parent is self:
                if node.next is None: 
                    self.head.data = None
                    self.head.save()
                else:
                    self.head = node.next
                    self.save()
            else:
                parent.next = node.next
                parent.save()

        def delete(self, goal):
            if self.isEmpty(): print("Empty list")
            else: return self.__delete(goal)

        def push(self, new_data):
            if self.isEmpty():
                self.head.data = new_data
                self.head.save()
            else:
                new_node = groupListNode(data=new_data, next=self.head)
                new_node.save()
                self.head = new_node
            self.save()
                
        def __traverse(self, node):
            if node is None:
                return
            for nextData in self.__traverse(node.next):
                yield(nextData)
            yield(node.data)

        def traverse(self):
            if self.isEmpty(): print("Empty list")
            else: return self.__traverse(self.head)

    
class userTreeNode(models.Model):
        data = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True, related_name='dataTreeNode')
        left = models.ForeignKey('userTreeNode', on_delete=models.CASCADE, null=True, blank=True, related_name='leftData')
        right = models.ForeignKey('userTreeNode', on_delete=models.CASCADE, null=True, blank=True, related_name='rightData')

class userBinarySearchTree(models.Model):
        root = models.ForeignKey('userTreeNode', on_delete=models.CASCADE, null=True, blank=True, related_name='userTree')

        def isEmpty(self):
            return self.root.data is None
        
        def __find(self, goal):
            current = self.root
            parent = self

            while (current and goal != current.data):
                parent = current
                current = (current.left if goal.name < current.data.name else current.right)
            return parent, current
        
        def search(self, goal):
            if self.isEmpty(): print("Empty tree")
            else: return self.__find(goal)
            
        def insert(self, data):
            if self.isEmpty():
                self.root.data = data
                self.root.save()
            else:
                parent, node = self.__find(data)
                if node:
                    node.data = data
                    return False
                elif data.name < parent.data.name:
                    parent.left = userTreeNode(data=data, left = None, right = None)
                    parent.left.save()
                else:
                    parent.right = userTreeNode(data=data, left = None, right = None)
                    parent.right.save()
                parent.save()
            self.save()    
        
        def traverse(self):
            if self.isEmpty(): print("Empty tree")
            else: return self.__traverse(self.root)

        def __traverse(self, node):
            if node is None:
                return
            
            for leftData in self.__traverse(node.left):
                yield(leftData)

            yield(node.data)

            for rightData in self.__traverse(node.right):
                yield(rightData)

        def __promote_sucessor(self, node):                    
            sucessor = node.right
            parent = node

            while sucessor.left:
                parent = sucessor
                sucessor = sucessor.left

            node.data = sucessor.data
            self.__delete(parent, sucessor)

        def __delete(self, parent, node):
            deleted = node.data
            
            if node.left:
                if node.right:
                    self.__promote_sucessor(node)
            
                else:
                    if parent is self:
                        self.root = node.left

                    elif parent.left is node:
                        parent.left = node.left

                    else:
                        parent.right = node.left
            
            else:
                if parent is self:
                    if node.right: 
                        self.root = node.right
                    else:
                        self.root.data = None
                        self.root.save()
                
                elif parent.left is node:
                    parent.left = node.right

                else:
                    parent.right = node.right

            parent.save()
            print("User deleted")
            return deleted
        
        def delete(self, goal):
            parent, node = self.__find(goal)

            if node is not None:
                return self.__delete(parent, node)
            else:
                print("Node not found")

        def nodes(self):
            count = 0
            for key, data in self.traverse():
                count += 1
            return count

class User(models.Model):
    picture = models.ImageField(upload_to=user_profile_image_path, blank=True, null=True, default='media/anonymous.png')
    name = models.TextField(max_length=80, default = 'name')
    id = models.TextField(max_length=20, default = 'id', primary_key=True)
    description = models.TextField(max_length=800, default = 'description')
    password = models.TextField(max_length=20, default = 'password')
    theme = models.TextField(max_length=5, default = 'light')
    language = models.TextField(max_length=2, default = 'pt')

    groupsList = models.ForeignKey('groupLinkedList', on_delete=models.CASCADE, null=True, blank=True)


class Group(models.Model):
    picture = models.ImageField(upload_to=group_image_path, blank=True, null=True, default='media/defBanner.png') 
    name = models.TextField(max_length=80, default = 'name')
    id = models.TextField(max_length=20, default = 'id', primary_key=True)
    description = models.TextField(max_length=800, default = 'description')

    adminList = models.ForeignKey('userBinarySearchTree', on_delete=models.CASCADE, null=True, blank=True, related_name='admins')
    membersList = models.ForeignKey('userBinarySearchTree', on_delete=models.CASCADE, null=True, blank=True, related_name='members')

 
# Create your models here.
