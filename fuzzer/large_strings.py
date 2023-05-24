import requests
import fuzzer.utils as utils


def get_large_strings():
    large_strings = [
        'a' * 1,
        'a' * 10,
        'a' * 100,
        'a' * 1000,
        'a' * 10000,
        'a' * 100000
    ]

    return large_strings


def send_large_strings_to_api(username, password, url):
    # Basic Authentication
    auth = (username, password)

    # Setting headers for a JSON request
    headers = {
        'Content-Type': 'application/json'
    }

    large_list = get_large_strings()
    for naughty_string in large_list:
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
