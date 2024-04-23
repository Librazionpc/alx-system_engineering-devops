#!/usr/bin/env python3
"""Using what you did in the task #0, extend
your Python script to export data in the json format.
"""

import sys
import json
import requests

def export_to_json_all_employees():
    """Function that uses restapi to get employee todo status to json file"""

    base_url = 'https://jsonplaceholder.typicode.com'
    users_url = f'{base_url}/users'

    try:
        users_response = requests.get(users_url)
        users_data = users_response.json()

        all_tasks = {}
        for user in users_data:
            user_id = user['id']
            user_username = user['username']
            todos_url = f'{base_url}/todos?userId={user_id}'
            todos_response = requests.get(todos_url)
            todos_data = todos_response.json()
            user_tasks = [{"username": user_username, "task": task['title'],
                           "completed": task['completed']} for task in todos_data]
            all_tasks[str(user_id)] = user_tasks

        json_file = "todo_all_employees.json"
        with open(json_file, 'w') as file:
            json.dump(all_tasks, file, indent=4)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    export_to_json_all_employees()
