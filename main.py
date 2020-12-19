import requests

print("Epic Games Free Game Promotion Parser by d4rckh.")

base_url = "https://www.epicgames.com"

r = requests.get( base_url + "/store/backend/static/freeGamesPromotions")

def handleData(data):
    for game in data["Catalog"]["searchStore"]["elements"]:
        print("---"*10)
        print(game["title"] + ": " + game["description"])
        for image in game["keyImages"]:
            if image["type"] == "VaultClosed":
                print("Unwrapped showcase: " + image["url"])
            if image["type"] == "DieselStoreFrontWide":
                print("Wrapped showcase: " + image["url"])

handleData(r.json()["data"])
