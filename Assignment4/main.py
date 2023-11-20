class Node:
    def __init__(self,info):
        self.info = info
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def delNode(self,value):
        if self.size == 0:
            print("Nothing to delete, list is empty!")
        elif self.size == 1:
            self.head = self.head.next
            print("Node " , value , "was deleted")
            self.size -= 1
        else:
            current = self.head
            while current.next is not None:
                if current.next.info == value:
                    current.next = current.next.next
                    print("Node " , value , "was deleted!")
                    self.size -= 1
                    break
                current = current.next

    def displayNodes(self):
        current = self.head
        while current != None:
            print(current.info, end=" ")
            current = current.next
        print()

class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self,item):
        self.items.append(item)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue is already empty!")
        else:
            self.items.pop(self.items[0])
        self.size -= 1

    def display(self):
        print(self.items)




def displayMenu():
    while True:
        print("Main Menu:")
        print("1-Singly Linked List")
        print("2-Check if Palindrome")
        print("3-Priority Queue")
        print("4-Evaluate an infix Expression")
        print("5-Graph")
        print("6-Exit")
        choice = int(input("Please enter a choice between 1 and 6: "))
        if choice == 1:
            linkedList()
        elif choice == 2:
            ifPalindrome()
        elif choice == 3:
            priorityQueue()
        elif choice == 4:
            evaluateInfix()
        elif choice == 5:
            graph()
        elif choice == 6:
            print("Exiting the program , have a nice day!")
            break
        else:
            print("Invalid input , please enter a number between 1 and 6")

def linkedList():
    ll = LinkedList()
    while True:
        print("a.Add Node")
        print("b.Display Nodes")
        print("c.Search for & Delete Node")
        print("d.Return to main menu")
        choicee = input("Please enter one of the above choices: ").lower()

        if choicee == "a":
            node_value = input("Please enter a numerical value: ")
            if node_value.isnumeric():
                ll.addNode(node_value)
            else:
                print("please enter an appropriate choice!")
        elif choicee == "b":
            ll.displayNodes()
        elif choicee == "c":
            del_node = input("Please enter the value of the node u want to delete: ")
            ll.delNode(del_node)

        elif choicee == "d":
            displayMenu()
            break
        else:
            print("Invalid choice!")










def ifPalindrome():
    s = input("Please input the word you want to check: ")
    string_list =[]

    for letter in s:
       string_list.append(letter)

    qq = Queue()

    for letter in string_list:
        qq.enqueue(letter)

    qq.display()

    if qq[0] == qq[-1]:










def priorityQueue():
    pass

def evaluateInfix():
    pass

def graph():
    pass


def main():
    name = input("What is your name?: ")
    print("Thank you for using my program" , name)

    displayMenu()





main()
