class Node:
    def __init__(self):
        self.name = ""
        self.telephone = ""
        self.key = 0

class Hashing:
    def __init__(self):
        self.data = [Node() for _ in range(100)]
        self.size = 100

    def ascii_generator(self, s):
        return sum(ord(c) for c in s) % 100

    def create_record(self, name, telephone):
        k = self.ascii_generator(name)
        index = k % self.size

        while True:
            if self.data[index].key == 0:
                self.data[index].key = k
                self.data[index].name = name
                self.data[index].telephone = telephone
                break
            else:
                index = (index + 1) % self.size

    def search_record(self, name):
        k = self.ascii_generator(name)
        index = k % self.size

        for _ in range(self.size):
            if self.data[index].key == k:
                print("\nRecord found")
                print("Name:", self.data[index].name)
                print("Telephone:", self.data[index].telephone)
                return
            else:
                index = (index + 1) % self.size

        print("Record not found")

    def delete_record(self, name):
        k = self.ascii_generator(name)
        index = k % self.size

        for _ in range(self.size):
            if self.data[index].key == k:
                self.data[index].key = 0
                self.data[index].name = ""
                self.data[index].telephone = ""
                print("\nRecord deleted successfully")
                return
            else:
                index = (index + 1) % self.size

        print("\nRecord not found")

    def update_record(self, name):
        k = self.ascii_generator(name)
        index = k % self.size

        for _ in range(self.size):
            if self.data[index].key == k:
                print("Enter the new telephone number:")
                telephone = input()
                self.data[index].telephone = telephone
                print("\nRecord updated successfully")
                return
            else:
                index = (index + 1) % self.size

        print("Record not found")

    def display_record(self):
        print("\tName\t\tTelephone")
        for node in self.data:
            if node.key != 0:
                print("\t{}\t\t{}".format(node.name, node.telephone))

if __name__ == "__main__":
    s = Hashing()
    while True:
        print("\n-------------------------")
        print("Telephone book Database")
        print("-------------------------")
        print("1. Create Record")
        print("2. Display Record")
        print("3. Search Record")
        print("4. Update Record")
        print("5. Delete Record")
        print("6. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            name = input("Enter name: ")
            telephone = input("Enter Telephone number: ")
            s.create_record(name, telephone)
        elif choice == 2:
            s.display_record()
        elif choice == 3:
            name = input("Enter the name: ")
            s.search_record(name)
        elif choice == 4:
            name = input("Enter the name: ")
            s.update_record(name)
        elif choice == 5:
            name = input("Enter name to delete: ")
            s.delete_record(name)
        elif choice == 6:
            break
        else:
            print("\nYou entered something wrong!")
