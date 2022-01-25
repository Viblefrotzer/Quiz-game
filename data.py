import requests

# getting question data from API

parameters = {
    "amount": 10,
    "type": "boolean",
}

imported_data = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = imported_data.json()['results']
