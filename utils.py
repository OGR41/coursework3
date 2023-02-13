import requests
from pprint import pprint


def get_data(url):
    try:
        response = requests.request("GET", url)
        if response.status_code == 200:
            return response.json(), "INFO: Данные успешно получены"
        return None, f"ERROR: status_code: {response.status_code}"

    except requests.exceptions.ConnectionError:
        return None, "ERROR: requests.exceptions.ConnectionError"

    except requests.exceptions.JSONDecodeError:
        return None, "ERROR: requests.exceptions.JSONDecodeError"


def get_filter_data(data):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data

