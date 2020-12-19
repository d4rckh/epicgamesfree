import requests

print("Epic Games Free Game Promotion Parser by d4rckh.")

r = requests.get("https://www.epicgames.com/store/backend/static/freeGamesPromotions")

for game in r.json()["data"]["Catalog"]["searchStore"]["elements"]:
    print("---"*10)
    print(game["title"] + ": " + game["description"])
    for image in game["keyImages"]:
        if image["type"] == "VaultClosed":
            print("Unwrapped showcase: " + image["url"])
        if image["type"] == "DieselStoreFrontWide":
            print("Wrapped showcase: " + image["url"])
