import json, pprint, time, datetime

def search_by_name(catalog, device_name):
    for device in catalog["devicesList"]:
        if device["deviceName"] == device_name:
            pprint.pprint(device)

def search_by_id(catalog, id):
    for device in catalog["devicesList"]:
        if device["deviceID"] == id:
            pprint.pprint(device)
            return 0
    return -1

def search_by_service(catalog, service):
    for device in catalog["devicesList"]:
        if device["availableServices"].__contains__(service):
            pprint.pprint(device)

def search_by_measure_type(catalog, measure_type):
    for device in catalog["devicesList"]:
        if device["measureType"].__contains__(measure_type):
            pprint.pprint(device)

def insert_device(catalog):
    now = datetime.datetime.now()  
    catalog["lastUpdate"] = f"{now.year}-{now.month}-{now.day} {now.hour}:{now.minute}"
    new_id = input("Insert the new ID: ")
    state = ""
    if search_by_id(catalog, new_id) == 0:
        print("The ID is already present in the catalog, proceed to update the device")    
        state = "update"
    else:
        print("The ID is not in the catalog, inserting a new device")
        state = "new"

    new_device_name = input("Insert the new Device Name: ")
    new_measure_type = (input("Insert the list of Measure Types separated by a space: ")).split()
    new_avaliable_services = (input("Insert the list of Avaliable services separated by a space: ")).split()
    new_services_details = []
    MQTT_service_details = {
        "serviceType" : "",
        "serviceIP" : "",
        "topic" : []
    }
    REST_service_details = {
        "serviceType" : "",
        "serviceIP" : ""
    }

    for aval_service in new_avaliable_services:
        print(f"Service {aval_service}:")
        new_service_type = aval_service
        new_service_ip = input("Insert the new service IP: ")

        if aval_service == "MQTT":
            new_service_topic = (input("Insert the list of topics, separated by a space: ")).split()

            MQTT_service_details["serviceType"] = new_service_type
            MQTT_service_details["serviceIP"] = new_service_ip
            MQTT_service_details["topic"] = new_service_topic

            new_services_details.append(MQTT_service_details)
        elif aval_service == "REST":
            REST_service_details["serviceType"] = new_service_type
            REST_service_details["serviceIP"] = new_service_ip

            new_services_details.append(REST_service_details)
        
    new_last_update = f"{now.year}-{now.month}-{now.day}"

    if state == "new":
        catalog["devicesList"].append({
            "deviceID" : new_id,
            "deviceName" : new_device_name,
            "measureType" : new_measure_type,
            "availableServices" : new_avaliable_services,
            "servicesDetails" : new_services_details,
            "lastUpdate" : new_last_update
        })
    elif state == "update":
        for device in catalog["devicesList"]:
            if device["deviceID"] == new_id:
                device["deviceID"] = new_id
                device["deviceName"] = new_device_name
                device["measureType"] = new_measure_type
                device["availableServices"] = new_avaliable_services
                device["servicesDetails"] = new_services_details
                device["lastUpdate"] = new_last_update

def print_all(catalog):
    pprint.pprint(catalog)

if __name__ == "__main__":
    catalog = json.load(open("catalog.json", "r", encoding='utf-8'))

    while(1):
        print("Avaliable services:")
        print("1) Search by name <device_name>")
        print("2) Search by ID <device_ID>")
        print("3) Search by service <service>")
        print("4) Search by measure type <measure_type>")
        print("5) Insert device")
        print("6) Print all catalog")
        print("9) Exit")
        cmd = input()

        if cmd == "1":
            search_by_name(catalog, input("Insert the device name: "))
        elif cmd == "2":
            search_by_id(catalog, input("Insert the device ID: "))
        elif cmd == "3":
            search_by_service(catalog, input("Insert the service: "))
        elif cmd == "4":
            search_by_measure_type(catalog, input("Insert the measure type: "))
        elif cmd == "5":
            insert_device(catalog)
        elif cmd == "6":
            print_all(catalog)
        elif cmd == "9":
            break
            
        json.dump(catalog, open("catalog.json", "w", encoding='utf-8'))