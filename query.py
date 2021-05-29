import requests
from formatter import format

def query(params):
    pair = params["pair"]
    response = requests.get(f"https://yobit.net/api/3/ticker/{pair}").json()
    return format(response, params)