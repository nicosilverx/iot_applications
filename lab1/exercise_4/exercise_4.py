import json

class Contact:
    def __init__(self):
        self.personal_data = {
            "name" : "",
            "surname" : "",
            "email" : ""
        }
    def insert_personal_data(self, file_path):
        self.personal_data=json.load(open(file_path, "r"))
        print(self.personal_data) 

#if __name__=="__main__":
#    c1=Contact()
#    c1.insert_personal_data("./contact.json")        
    