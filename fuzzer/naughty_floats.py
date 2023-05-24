import requests
import fuzzer.utils as utils


def get_naughty_floats():
    large_strings = [
        -1,
        -1.8624876384682468,
        0,
        1,
        1.8624876384682468,
        1.862487638468246889,
        1.8624876384682468893,
        1.86248763846824688978,
        1.1,
        1.01,
        1.001,
        1.0001,
        1.00001,
        1.000001,
        1.0000001
    ]

    return large_strings


def send_naughty_floats_to_api(username, password, url):
    # Basic Authentication
    auth = (username, password)

    # Setting headers for a JSON request
    headers = {
        'Content-Type': 'application/json'
    }

    large_list = get_naughty_floats()
    for naughty_number in large_list:
        json_data = utils.create_json_data_from_number(naughty_number)
        print(json_data)

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
