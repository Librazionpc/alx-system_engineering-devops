#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
from sys import argv, exit


def get_emloyee_progress(employee_id):
    """Function that uses restapi to get employee todo status"""

    base_url = 'https://jsonplaceholder.typicode.com'
    session_req = requests.Session()

    id_url = f'{base_url}/users/{employee_id}/todos'
    name_url = f'{base_url}/users/{employee_id}'

    employee_response = session_req.get(id_url)
    employee_name_response = session_req.get(name_url)

    employee_data = employee_response.json()
    employee_name = employee_name_response.json()['name']

    total_tasks = len(employee_data)
    completed_tasks = sum(1 for task in employee_data if task['completed'])

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    for task in employee_data:
        if task['completed']:
            print(f"\t{task['title']}")


if __name__ == "__main__":
    if (len(argv) < 2):
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        exit(1)
    employee_id = int(argv[1])
    get_emloyee_progress(employee_id)
