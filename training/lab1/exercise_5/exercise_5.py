from exercise_4 import *

class AddressBook:
    def __init__(self):
        self.client_list = []

    def add_contact_by_params(self, name, surname, email):
        contact = Contact()
        contact.insert_personal_data(name, surname, email)
        self.client_list.append(contact)

    def add_contact(self, contact):
        self.client_list.append(contact)

    def find_by_name(self, name):
        for client in self.client_list:
            if (client.get_personal_data()[0] == name):
                return client.get_personal_data()
        print(f"No client with name = {name} was found")
        return ""

    def show(self):
        for client in self.client_list:
            print(client.get_personal_data())

    def remove_by_name(self, name):
        for client in self.client_list:
            if (client.get_personal_data()[0] == name):
                self.client_list.remove(client)
        print(f"No client with name = {name} was found")
    
    def update_contact(self, contact_old, contact_new):
        for client in self.client_list:
            if (client == contact_old):
                self.client_list.remove(contact_old)
                self.add_contact(contact_new)
    
    def update_contact_by_params(self, name_old, name_new, surname_new, email_new):
        for client in self.client_list:
            if (client.get_personal_data()[0] == name_old):
                self.client_list.remove(client)
                self.add_contact_by_params(name_new, surname_new, email_new)

                
if __name__=="__main__":
    #Client ;)
    address_book = AddressBook()
    while True:
        user_input = input("Welcome to the application to manage your contacts\nPress 's' to show the list of contacts\nPress 'n' to add a contact\n"+
            "Press 'f' to find a contact\nPress 'd' to delete a contact\nPress 'u' to update a contact\nPress 'q' to quit\n")    
        
        if user_input=="s":
            address_book.show()
            
        elif user_input=="n":
            name = input("Name: ")
            surname = input("Surname: ")
            email = input("Email: ")
            address_book.add_contact_by_params(name, surname, email)
            
        elif user_input=="f":
            name = input("Insert the name to search: ")
            address_book.find_by_name(name)

        elif user_input=="d":
            name = input("Insert the name to delete: ")
            address_book.remove_by_name(name)
        elif user_input=="u":
            name_old = input("Insert the name of the contact to update: ")
            name_new = input("New name: ")
            surname_new = input("New surname: ")
            email_new = input("New email: ")
            address_book.update_contact_by_params(name_old, name_new, surname_new, email_new)
        elif user_input=="q":
            break
        else:
            print("Command not recoginzed")
    print("Goodbye!")