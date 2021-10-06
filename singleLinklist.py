import os
import sys
# create a node
class Node:
    def __init__(self, info, Next=None):
        self.data = info
        self.next = Next

class SingleLinkList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert_at_first(self, item):
        newNode = Node(item)
        if self.first == None:
            newNode.next = None
            self.first = newNode
            self.last = newNode
        else:
            newNode.next = self.first
            self.first = newNode

    def insert_at_position(self, item, position):
        newNode = Node(item)
        if self.first == None:
            self.first = newNode
            self.last = newNode
        else:
            temp = self.first
            for i in range(1, position-1):
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode

    def insert_at_end(self, item):
        newNode = Node(item)
        if self.first == None:
            self.first = newNode
            self.last = newNode
        else:
            temp = self.first
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            self.last = newNode

    def delete_at_first(self):
        if self.first == None:
            Print("Empty List. Void Deletion.")
            return
        else:
            temp = self.first
            self.first = self.first.next
            del temp

    def delete_at_position(self, position):
        if self.first == None:
            print("Empyt List. Void Deletion.")
            return
        else:
            temp = self.first
            for i in range(1,position-1):
                temp = temp.next
            hold = temp.next
            temp.next = hold.next
            del hold

    def delete_at_end(self):
        temp = self.first
        if self.first == None:
            Print("Empty List. Void Deletion.")
            return
        elif temp.next == None:
            hold = self.first
            self.first = None
            del hold
        else:
            while temp.next != None:
                temp = temp.next
            hold = temp.next
            temp.next = None
            del hold

    def display(self):       
        temp = self.first
        if temp == None:
            print("Empty Linked List.")
        else:
            while temp != None:
                print(temp.data)
                temp = temp.next


def main():
    print("Menu for programm:")
    print("1.Insert First\n2.Insert at given position\n3.Insert at last")
    print("4.Delete First\n5.Delete at given position\n6.Delete at last")
    print("9. Display Items\n10.Exit")
    choice = int(input("Enter Your Choice: "))
    my_list = SingleLinkList()
    if choice == 1:
        item = int(input("Enter element: "))       
        my_list.insert_at_first(item)
        my_list.display()

    elif choice == 2:
        my_list.insert_at_first(5)
        my_list.insert_at_first(4)
        my_list.insert_at_first(6)
        item = int(input("Enter element: "))
        position = int(input("Enter position: "))       
        my_list.insert_at_position(item, position)
        my_list.display()

    elif choice == 3:
        #my_list.insert_at_first(5)
        #my_list.insert_at_first(4)
        item = int(input("Enter element: ")) 
        my_list.insert_at_end(item)
        my_list.display()

    elif choice == 4:
        my_list.insert_at_first(5)
        my_list.insert_at_first(4)
        my_list.display()
        my_list.delete_at_first()
        print("After deleting")
        my_list.display()
    
    elif choice == 5:
        pass

    elif choice == 6:
        pass

    elif choice == 9:
        #my_list = SingleLinkList()
        my_list.display()
            
    elif choice == 10:
        print("Exiting System.")
        exit()
    else:
        print("Please enter valid choice.")

if __name__ == "__main__":
    main()




