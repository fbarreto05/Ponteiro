from django.db import models

def user_profile_image_path(instance, filename):
    return f'user_profiles/{instance.id}/profilePicture/{filename}'

def group_image_path(instance, filename):
    return f'groups/{instance.id}/bannerPicture/{filename}'

class groupListNode(models.Model):
        data = models.OneToOneField('Group', on_delete=models.CASCADE, null=True, blank=True)
        next = models.OneToOneField('groupListNode', on_delete=models.CASCADE, null=True, blank=True)

class groupLinkedList(models.Model):
        head = models.OneToOneField('groupListNode', on_delete=models.CASCADE, null=True, blank=True)

        def isEmpty(self):
            if self.head.data == None:
                return True
            else: return False

        def __find(self, goal):
            current = self.head
            parent = self
            while current and goal != current.data.id:
                parent = current
                current = current.next
            return parent, current
        
        def search(self, goal):
            if self.isEmpty(): print("Empty list")
            else: return self.__find(goal)

        def __delete(self, goal):
            parent, node = self.search(goal)
            parent.next = node.next

        def delete(self, goal):
            if self.isEmpty(): print("Empty list")
            else: return self.__delete(goal)

        def push(self, new_data):
                new_node = groupListNode(data=new_data, next=self.head)
                new_node.save()
                print(self.head)
                self.head = new_node
                print (self.head)
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

    
class userTreeNode():
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

class userBinarySearchTree():
        def __init__(self):
            self.__root = None

        def isEmpty(self):
            return self.__root is None
        
        def __find(self, goal):
            current = self.__root
            parent = self

            while (current and goal != current.data):
                parent = current
                current = (current.left if goal < current.data else current.right)
            return (current, parent)
        
        def search(self, goal):
            if self.isEmpty(): print("Empty tree")
            else:
                node, parent = self.__find(goal)
                return node.data if node else None
            
        def insert(self, data):
            node, parent = self.__find(data)
            if node:
                node.data = data
                return False
            if parent is self:
                self.__root = self.userTreeNode(data)
            elif data < parent.data:
                parent.left = self.userTreeNode(data)
            else:
                parent.right = self.userTreeNode(data)
            return True
        
        def traverse(self):
            if self.isEmpty(): print("Empty tree")
            else: return self.__traverse(self.__root)

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
                        self.__root = node.left

                    elif parent.left is node:
                        parent.left = node.left

                    else:
                        parent.right = node.left
            
            else:
                if parent is self:
                    self.__root = node.right
                
                elif parent.left is node:
                    parent.left = node.right

                else:
                    parent.right = node.right

            print("User deleted")
            return deleted
        
        def delete(self, goal):
            node, parent = self.__find(goal)

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

    groupsList = models.OneToOneField('groupLinkedList', on_delete=models.CASCADE, null=True, blank=True)


class Group(models.Model):
    picture = models.ImageField(upload_to=group_image_path, blank=True, null=True, default='media/defBanner.png') 
    name = models.TextField(max_length=80, default = 'name')
    id = models.TextField(max_length=20, default = 'id', primary_key=True)
    description = models.TextField(max_length=800, default = 'description')

    adminList = userBinarySearchTree()
    membersList = userBinarySearchTree()

 
# Create your models here.
