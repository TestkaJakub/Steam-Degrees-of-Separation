import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')


def get_friends(steam_id):
    url = f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={API_KEY}&steamid={steam_id}&relationship=friend'
    response = requests.get(url)
    if not response:
        return None

    friends = response.json()['friendslist']['friends']
    steam_ids = [friend['steamid'] for friend in friends]
    return steam_ids


def get_name(steam_id):
    url = f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={API_KEY}&steamids={steam_id}'
    response = requests.get(url)
    if not response:
        return steam_id

    name = response.json()['response']['players'][0]['personaname']
    return name
