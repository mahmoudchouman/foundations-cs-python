class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1
        print("Node of value ", value, "was added")

    def delNode(self, value):
        if self.size == 0:
            print("Nothing to delete, list is empty!")
        elif self.size == 1:
            self.head = self.head.next
            print("Node ", value, "was deleted")
            self.size -= 1
        else:
            current = self.head
            while current.next is not None:
                if current.next.info == value:
                    current.next = current.next.next
                    print("Node ", value, "was deleted!")
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

    def enqueue(self, item):
        self.items.append(item)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue is already empty!")
        else:
            removed_item = self.items.pop(0)
            self.size -= 1
            return removed_item

    def display(self):
        print(self.items)


class Student:

    def __init__(self, name, midterm_grade, final_grade, good_attitude):
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.good_attitude = good_attitude


class PriorityQueue:

    def __init__(self):
        self.head = None
        self.size = 0

    def displayNodes(self):
        current = self.head

        while current != None:
            print(current.info)
            current = current.next

    def enqueue(self, Student):

        node = Node(Student)
        if self.size == 0:
            node.next = self.head
            self.head = node
            self.size += 1
        else:
            current = self.head
            previous = None

            while current is not None and current.info.good_attitude and \
                    (current.info.final_grade > Student.final_grade or
                     (current.info.final_grade == Student.final_grade and
                      current.info.midterm_grade > Student.midterm_grade)):
                previous = current
                current = current.next

            node.next = current
            if previous is not None:
                previous.next = node
            else:
                self.head = node

            self.size += 1

    def dequeue(self):

        if self.size == 0:
            print("Your Queue is Empty! Enqueue first.")
        elif self.size == 1:
            print("We are removing:", self.head.info.name)
            dequeued_student = self.head.info.name
            self.head = None
            self.size -= 1
            return dequeued_student

        else:
            print("We are removing:", self.head.info.name)
            dequeued_student = self.head.info.name
            current = self.head
            self.head = self.head.next
            current.next = None
            self.size -= 1
            return dequeued_student


class Graph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def addVertex(self):
        self.num_vertices += 1
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * self.num_vertices)
        print("Added vertex", self.num_vertices - 1)

    def addEdge(self, v1, v2):

        if 0 < v1 < self.num_vertices and 0 < v2 < self.num_vertices:
            self.adj_matrix[v1][v2] = 1
            self.adj_matrix[v2][v1] = 1
            print("Added an edge between vertices", v1, "and", v2)
        else:
            print("Invalid vertex input")

    def removeVertex(self, vertex):
        if 0 <= vertex < self.num_vertices:
            del self.adj_matrix[vertex]
            for row in self.adj_matrix:
                del row[vertex]
            self.num_vertices -= 1
            print("Vertex", vertex, "was removed!")
        else:
            print("Vertex", vertex, "does not exist in your graph!")

    def removeEdge(self, vertex1, vertex2):
        if 0 <= vertex1 < self.num_vertices and 0 <= vertex2 < self.num_vertices:
            if self.adj_matrix[vertex1][vertex2] == 1:
                self.adj_matrix[vertex1][vertex2] = 0
                self.adj_matrix[vertex2][vertex1] = 0
                print("Edge between Vertices", vertex1, "and", vertex2, "removed!")
            else:
                print("No edge between Vertices ", vertex1, "and", vertex2, "exist!")
        else:
            print("Invalid vertices input!")


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
            if isPalindrome():
                print("The string you entered is a palindrome!")
            else:
                print("The string you entered is not a palindrome :( ")
        elif choice == 3:
            priorityQueue()
        elif choice == 4:
            evaluateInfix()
        elif choice == 5:
            graph()
        elif choice == 6:
            print("Exiting the program , have a nice day!")
            exit()
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
            return
        else:
            print("Invalid choice!")


def isPalindrome():
    s = input("Please input the word you want to check: ")
    string_list = []

    for letter in s:
        string_list.append(letter)

    qq = Queue()

    for letter in string_list:
        qq.enqueue(letter)

    while qq.size != 0:
        if qq.dequeue() != qq.items[-1]:
            return False
        else:
            return True


def priorityQueue():
    pq = PriorityQueue()

    while True:
        print("Menu:")
        print("a. Add a student")
        print("b. Interview a student")
        print("c. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "a":
            name = input("Enter student name: ")
            midterm_grade = int(input("Enter midterm grade (0-100): "))
            final_grade = int(input("Enter final grade (0-100): "))
            good_attitude = bool(input("Does the student have a good attitude? (True/False): "))
            student = Student(name, midterm_grade, final_grade, good_attitude)
            pq.enqueue(student)

        elif choice == "b":
            if pq.size > 0:
                interviewed_student = pq.dequeue()
                print("Interviewing student:", interviewed_student)
            else:
                print("Priority Queue is empty. No students to interview.")
        elif choice == "c":
            displayMenu()
            return
        else:
            print("Invalid choice. Please enter a, b, or c.")


def evaluateInfix():
    pass


def graph():
    num_vertices = int(input("Please enter the number of vertices that your graph has: "))
    g = Graph(num_vertices)
    while True:
        print("a.Add vertex")
        print("b.Add edge")
        print("c.Remove vertex")
        print("d.Remove edge")
        print("e.Display vertices with a degree of X or more")
        print("f.Return to main menu")
        choicee = input("Please enter one of the above choices: ").lower()

        if choicee == "a":
            g.addVertex()
        elif choicee == "b":
            vertex1 = int(input("Please enter vertex 1: "))
            vertex2 = int(input("Please enter vertex 2: "))
            g.addEdge(vertex1, vertex2)
        elif choicee == "c":
            vertex = int(input("Please enter the vertex you wish to remove: "))
            g.removeVertex(vertex)
        elif choicee == "d":
            vertex1 = int(input("Please enter vertex 1: "))
            vertex2 = int(input("Please enter vertex 2: "))
            g.removeEdge(vertex1, vertex2)
        elif choicee == "e":
            n = int(input("Please enter a numerical value to display all vertices of that degree and higher: "))
            for i in range(g.num_vertices):
                if i >= n:
                    print("vertex ", i)
        elif choicee == "f":
            displayMenu()
            return
        else:
            print("Invalid choice!")


def main():
    name = input("What is your name?: ")
    print("Thank you for using my program", name)
    displayMenu()


main()
