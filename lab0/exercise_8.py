if __name__=="__main__":
    personal_data = {
        "projectName":"",
        "company":"",
        "deviceList":[
            {
                "deviceID":"",
                "deviceName":"",
                "deviceType":""
            }
        ]
    }
    personal_data["projectName"] = input("Project name: ")
    personal_data["company"] = input("Company: ")
    personal_data["deviceList"][0]["deviceID"] = input("Device ID: ")
    personal_data["deviceList"][0]["deviceName"] = input("Device Name: ")
    personal_data["deviceList"][0]["deviceType"] = input("Device Type: ")

    print(personal_data)
    