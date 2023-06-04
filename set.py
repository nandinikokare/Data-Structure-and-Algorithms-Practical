class Set:
    def __init__(self):
        self.l = []
        self.l1 = []
        self.u = []
        self.I = []
        self.d = []
    
    def insert(self):
        print("SET A:")
        n = int(input("How many elements you want to add in Set A: "))
        print("Enter elements:")
        for _ in range(n):
            num = int(input())
            self.l.append(num)
        
        print("SET B:")
        m = int(input("How many elements you want to add in Set B: "))
        print("Enter elements:")
        for _ in range(m):
            num = int(input())
            self.l1.append(num)
    
    def add(self):
        c = input("In which set do you want to add an element (A/B): ")
        if c.upper() == 'A':
            num = int(input("Enter element: "))
            self.l.append(num)
            print("Element inserted")
        elif c.upper() == 'B':
            num = int(input("Enter element: "))
            self.l1.append(num)
            print("Element inserted")
        else:
            print("Invalid set")
    
    def display(self):
        print("The elements for Set A:")
        print("{", end=" ")
        for num in self.l:
            print(num, end=" ")
        print("}")

        print("The elements for Set B:")
        print("{", end=" ")
        for num in self.l1:
            print(num, end=" ")
        print("}")
    
    def search(self, key):
        if key in self.l or key in self.l1:
            print("The element is present")
        else:
            print("The element is not present")
    
    def delete1(self, key):
        if self.l == [] and self.l1 == []:
            print("Set A and Set B are empty")
        else:
            self.search(key)
            if key in self.l:
                self.l.remove(key)
                print("Element deleted from Set A")
            elif key in self.l1:
                self.l1.remove(key)
                print("Element deleted from Set B")
            else:
                print("Element not found")
    
    def union1(self):
        self.u = self.l + [num for num in self.l1 if num not in self.l]
        print("The Union Set of A & B is: {", end=" ")
        for num in self.u:
            print(num, end=" ")
        print("}")
    
    def intersection(self):
        self.I = [num for num in self.l if num in self.l1]
        if self.I == []:
            print("There is no common element in Set A and Set B")
        else:
            print("The Intersection Set of A & B is: {", end=" ")
            for num in self.I:
                print(num, end=" ")
            print("}")
    
    def difference(self):
        self.d = [num for num in self.l if num not in self.l1]
        if self.d == []:
            print("Set A and Set B are equal")
        else:
            print("The Difference Set of A & B is: {", end=" ")
            for num in self.d:
                print(num, end=" ")
            print("}")

s = Set()
s.insert()

while True:
    print("\n-----------------------------")
    print("Set Theory")
    print("-----------------------------")
    print("1. Add Element")
    print("2. Delete Element")
    print("3. Search Element")
    print("4. Display")
    print("5. Union")
    print("6. Intersection")
    print("7. Difference")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        s.add()
    elif choice == 2:
        key = int(input("Enter which element to delete: "))
        s.delete1(key)
    elif choice == 3:
        key = int(input("Enter the element to be searched: "))
        s.search(key)
    elif choice == 4:
        s.display()
    elif choice == 5:
        s.union1()
    elif choice == 6:
        s.intersection()
    elif choice == 7:
        s.difference()
    elif choice == 8:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
