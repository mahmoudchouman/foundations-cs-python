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

    def displayNodes(self):
        current = self.head
        while current != None:
            print(current.info, end=" ")
            current = current.next



def displayMenu():
    print("Main Menu:")
    print("1-Singly Linked List")
    print("2-Check if Palindrome")
    print("3-Priority Queue")
    print("4-Evaluate an infix Expression")
    print("5-Graph")
    print("6-Exit")

def linkedList():
    ll = LinkedList()

    print("a.Add Node")
    print("b.Display Nodes")
    print("c.Search for & Delete Node")
    print("d.Return to main menu")

def ifPalindrome():
    pass

def priorityQueue():
    pass

def evaluateInfix():
    pass

def graph():
    pass


def main():
    name = input("What is your name?: ")
    print("Thank you for using my program" , name)

    while True:
        displayMenu()
        choice = input("Please enter a choice between 1 and 6: ")

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







main()
