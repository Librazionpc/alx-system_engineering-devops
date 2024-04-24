#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
from sys import argv, exit


def get_emloyee_progress(employee_id):
    """Function that uses restapi to get employee todo status"""

    base_url = "https://jsonplaceholder.typicode.com"
    session_req = requests.Session()

    try:
        id_url = '{}/users/{}/todos'.format(base_url, employee_id)
        name_url = '{}/users/{}'.format(base_url, employee_id)
        id_response = session_req.get(id_url)
        name_response = session_req.get(name_url)

        id_data = id_response.json()
        name_data = name_response.json()

        Dn_task = [task["title"] for task in id_data if task["completed"]]
        total = len(id_data)

        print(f"Employee {name_data['name']} is done with tasks("
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
