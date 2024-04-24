#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
from sys import argv, exit


def get_emloyee_progress(employee_id):
    """Function that uses restapi to get employee todo status"""

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f'{base_url}/users'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_respons = requests.get(user_url)
        todo_respons = requests.get(todo_url)

        us_data = user_respons.json()
        todos_data = todo_respons.json()
        name = None
        for i in us_data:
            if i['id'] == employee_id:
                name = i['name']
        Dn_task = [task["title"] for task in todos_data if task["completed"]]
        total = len(todos_data)

        print(f"Employee {name} is done with tasks("
              f"{len(Dn_task)}/{total}):")

        for task in Dn_task:
            print(f"\t{task}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    if (len(argv) < 2):
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        exit(1)
    employee_id = int(argv[1])
    get_emloyee_progress(employee_id)
