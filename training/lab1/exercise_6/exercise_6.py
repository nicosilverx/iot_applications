import math, json

""" player = {"tid": 0,
"name":"",
"ratings":[{"hgt": 0,"stre":0,"spd":0,"jmp":0,"endu":0,"ins":0,"dnk":0,"ft":0,"fg":0,"tp":0,"diq":0,"oiq":0,"drb":0,"pss":0,"reb":0}],
"pos":"","hgt":0,"weight":0,
"born":{"year":0,"loc":""},
"imgURL":"",
"contract":{"amount":0,"exp":0},
"draft":{"round":0,"pick":0,"tid":0,"originalTid":0,"year":0},
"college":"",
"awards":[{"season":0,"type":""},{"season":0,"type":""}],
"injury":{"type":"","gamesRemaining":0}} """

players_db = {"startingSeason":0,
"version":0,
"players":[]}


def avg_ratings(players_db):
    avg_player = 0.0
    avg_tot = 0.0
    name = ""
    for player in players_db["players"]:
        avg_player = 0.0
        name = player["name"]
        for ratings_list in player["ratings"]:
            for rating in ratings_list:
                avg_player += ratings_list[rating]

        avg_player = avg_player / 15    
        print(f"{name}:{avg_player:.2f}")
        avg_tot += avg_player
    avg_tot = avg_tot / len(players_db["players"])
    
def avg_measures(players_db):
    avg_height = 0.0
    avg_weight = 0.0
    for player in players_db["players"]:
        avg_height += (player["hgt"] / 39.37)
        avg_weight += (player["weight"] / 2.205)
    avg_height = avg_height / len(players_db["players"])
    avg_weight = avg_weight / len(players_db["players"])
    print(f"Average height: {avg_height:.2f} m\nAverage weight: {avg_weight:.2f} kg")

def avg_age(players_db):
    age = 0
    for player in players_db["players"]:
        age += 2020 - ((player["born"])["year"])
    age = age // len(players_db["players"])
    print(f"Average age: {age}")

if __name__=="__main__":
    players_db = json.load(open("playerNBA.json", "r", encoding='utf-8'))
    #avg_ratings(players_db)
    avg_measures(players_db)
    avg_age(players_db)