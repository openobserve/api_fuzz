import json
import requests

def create_blns_json(url):
    # Getting the list from the repository
    response = requests.get(url)
    blns = response.json()

    # Creating the JSON object
    json_data = []
    for i, naughty_string in enumerate(blns):
        # Each item in the list is a dictionary with a key-value pair
        # where the key is 'key' followed by the index and the value is the naughty string
        json_data.append({f'key{i}': naughty_string})

    return json_data

def get_blns_array(url):
    # Getting the list from the repository
    response = requests.get(url)
    blns = response.json()

    return blns
