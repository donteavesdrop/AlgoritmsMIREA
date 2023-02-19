class Node: #Создание класса дерева

    def __init__(self, data):

        self.left = None #указатель на левого потомка
        self.right = None #указатель на правого потомка
        self.data = data #ключ узла

    def insert(self, data): #Метод добавления элементов в дерево

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PreorderTraversal(self, root): #прямой обход дерева Root -> Left ->Right
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def InorderTransversal(self): #симметричный обход дерева
        if self.left:
            self.left.InorderTransversal()
        a=self.data
        print(self.data, end=' ')
        if self.right:
            self.right.InorderTransversal()

    def PostorderTransversal(self): #обратный обход дерева
        if self.left:
            self.left.PostorderTransversal()
        if self.right:
            self.right.PostorderTransversal()
        print(self.data, end=' ')
    def ParentSon(self): #метод для представления дерева в виде списка сыновей
        parent = self.data
        if self.left:
            ParentSon.append(self.left.data)
        if self.right:
            ParentSon.append(self.right.data)
        print("Pодитель -",parent, "Сыновья -",ParentSon)
        if self.left:
            ParentSon.clear()
            self.left.ParentSon()
        if self.right:
            ParentSon.clear()
            self.right.ParentSon()
        parent = ""
parent = ""
ParentSon=[]
a_tree = Node(8)
a_tree.insert(3)
a_tree.insert(10)
a_tree.insert(2)
a_tree.insert(9)
a_tree.insert(4)

b_tree = Node(5)
b_tree.insert(2)
b_tree.insert(6)
b_tree.insert(1)
b_tree.insert(3)
b_tree.insert(12)

print("\n Список сыновей дерева А:")
a_tree.ParentSon()
print("\n Список сыновей дерева B:")
b_tree.ParentSon()
print("\nОбратный обход дерева A: ", end="")
a_tree.PostorderTransversal()
print("\nЦентрированный обход дерева B: ", end="")
b_tree.InorderTransversal()

d3=b_tree.PreorderTraversal(b_tree)
print("\n \nА = A ⋃пр B // элементы дерева В будут добавлены в дерево А в прямом порядке обхода дерева В")
print("Прямой обход дерева B: ", end="")
print(d3)

for i in range (len(d3)): #А = A ⋃пр B
    a_tree.insert(int(d3[i-1]))
print("Итоговый результат в виде списка сыновей А:")
a_tree.ParentSon()
