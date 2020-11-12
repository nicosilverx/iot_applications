import json, pprint, time, datetime, cherrypy

def search_by_name(catalog, device_name):
    for device in catalog["devicesList"]:
        if device["deviceName"] == device_name:
            return device

def search_by_id(catalog, id):
    for device in catalog["devicesList"]:
        if device["deviceID"] == id:
            return device
    return -1

def search_by_service(catalog, service):
    for device in catalog["devicesList"]:
        if device["availableServices"].__contains__(service):
            return device

def search_by_measure_type(catalog, measure_type):
    for device in catalog["devicesList"]:
        if device["measureType"].__contains__(measure_type):
            return device

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
    return catalog


class WebCatalog(object):
    exposed = True
    

    def GET(self, *uri, **params):
        catalog = json.load(open("catalog.json", "r", encoding='utf-8'))
        #Check URI
        uri = list(uri)
        #Check Params
        if params!={}:
            keysList=list(params.keys())
            valuesList=[params[key] for key in params.keys()]
        
        print(keysList[0])

        if keysList[0] == "deviceName":
            return json.dumps(search_by_name(catalog, valuesList[0]))
        elif keysList[0] == "id":
            return json.dumps(search_by_id(catalog, int(valuesList[0])))
        elif keysList[0] == "service":
            return json.dumps(search_by_service(catalog, valuesList[0]))
        elif keysList[0] == "measureType":
            return json.dumps(search_by_measure_type(catalog, valuesList[0]))
        
        json.dump(catalog, open("catalog.json", "w", encoding='utf-8'))
        


if __name__ == "__main__":
    conf={
        '/':{
            'request.dispatch':cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on':True
        }
    }   
    cherrypy.tree.mount(WebCatalog(), '/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()