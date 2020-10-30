import json

class Contact:
    def __init__(self):
        self.personal_data = {
            "name" : "",
            "surname" : "",
            "email" : ""
        }
    def insert_personal_data(self, name, surname, email):
        self.personal_data = {
            "name" : name,
            "surname" : surname,
            "email" : email
        }
    def insert_personal_data_from_json(self, file_path):
        self.personal_data=json.load(open(file_path, "r"))
        print(self.personal_data) 
    def get_personal_data(self):
        return [self.personal_data["name"], self.personal_data["surname"], self.personal_data["email"]]

#if __name__=="__main__":
#    c1=Contact()
#    c1.insert_personal_data("./contact.json")        
    