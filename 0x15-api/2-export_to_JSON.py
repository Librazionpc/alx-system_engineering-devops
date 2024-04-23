"""Using what you did in the task #0, extend
your Python script to export data in the json format.
"""

from sys import argv
import json
import requests


def export_to_json(employee_id):
    """Function that uses restapi to get employee todo status to json file"""

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_respons = requests.get(user_url)
        todo_respons = requests.get(todo_url)

        us_data = user_respons.json()
        todos_data = todo_respons.json()

        json_file = f"{us_data['id']}.json"

        json_data = {
            str(employee_id): [
                {"task": task['title'], "completed": task['completed'],
                 "username": us_data['username']} for task in todos_data]
        }

        with open(json_file, 'w') as file:
            json.dump(json_data, file, indent=4)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 export_to_json.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])
    export_to_json(employee_id)
