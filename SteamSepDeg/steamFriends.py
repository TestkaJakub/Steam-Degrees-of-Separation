import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')


def get_friends(steam_id):
    url = f'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={API_KEY}&steamid={steam_id}&relationship=friend'
    response = requests.get(url)
    friends = response.json()['friendslist']['friends']
    steam_ids = [friend['steamid'] for friend in friends]
    return steam_ids