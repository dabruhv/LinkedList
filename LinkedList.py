class Student:
    def __init__(self, name, ID, favColor, next=None):
        self.name = name
        self.ID = ID
        self.favColor = favColor
        self.next = next
        
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, name, ID, favColor):
        newStudent = Student(name, ID, favColor) #insantiate a new student mode
        if self.head: #check if a head exists
            current = self.head #create a temporary pointer to the head node
            #while there's another node in the line, "walk" down the line until the end
            while current.next:
                current = current.next 
            current.next = newStudent #add the new student to the end
        else:
            self.head = newStudent #if there was no head student, insert at front of empty line
    
    def printList(self):
        current = self.head
        while current:
            print("Student name:", current.name, ", ID:", current.ID," favorite color: ", current.favColor)
            current = current.next
            
    def search(self, name):
        current = self.head
        while current:
            
            if name == current.name:
                return True
            else:
                current = current.next
        return False
    
    def size(self):
        bruh = 0
        current = self.head
        while current:
            bruh+=1
            current = current.next
        return bruh
    
    def select(self,num):
        num-=1
        current = self.head
        for i in range(num):
            current = current.next
        print("Student name:", current.name, ", ID:", current.ID," favorite color: ", current.favColor)
#----------------------------------------------
StudentLine = LinkedList()
StudentLine.insert("Rey", 456987, "pink")
StudentLine.insert("Kevin", 123987, "blue")
StudentLine.insert("Simon", 4, "purple")
StudentLine.insert("Ricky", 7844, "yellow")
StudentLine.insert("Lukas", 4832, "blue")
StudentLine.insert("Dom", 90430, "blue")
StudentLine.printList()
huh = str(input("gimmie name: "))
print(StudentLine.search(huh))
print("number of people is ", StudentLine.size())
sus = int(input("gimmie number "))
StudentLine.select(sus)
