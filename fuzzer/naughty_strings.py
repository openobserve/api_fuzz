import fuzzer.blns2 as blns2
import fuzzer.utils as utils
import requests


def get_blns_array():
    url = 'https://raw.githubusercontent.com/minimaxir/big-list-of-naughty-strings/master/blns.json'
    blns = blns2.get_blns_array(url)
    return blns


# def create_json_data_from_string(str):
#     json_data = []
#     json_data.append({'key': str})
#     return json_data

#  iterate over each item in the blns_array and send it to the API


def send_naughty_strings_to_api(username, password, url):
    # Basic Authentication
    auth = (username, password)

    # Setting headers for a JSON request
    headers = {
        'Content-Type': 'application/json'
    }

    naughty_list = get_blns_array()
    for naughty_string in naughty_list:
        json_data = utils.create_json_data_from_string(naughty_string)

        try:
            # Sending a POST request
            response = requests.post(
                url, auth=auth, headers=headers, json=json_data)

            # If the request was successful, response.status_code will be 200
            if response.status_code == 200:
                print('Request was successful.')
            else:
                print(
                    f'Request failed with status code {response.status_code}.')

        except requests.exceptions.RequestException as e:
            print(f'Request failed due to an exception: {e}')
