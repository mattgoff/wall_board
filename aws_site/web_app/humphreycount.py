import requests


def humphrey_stats():

    r = requests.get("https://api.thingspeak.com/channels/284894/feeds.json?results=5")
    results = r.json()
    humphrey_results = {'feeds': results['feeds']}
    return humphrey_results