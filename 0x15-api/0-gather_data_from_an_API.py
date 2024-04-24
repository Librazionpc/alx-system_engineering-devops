#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

import requests
from sys import argv, exit


def get_emloyee_progress(employee_id):
    """Function that uses restapi to get employee todo status"""

    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    try:
        user_respons = requests.get(user_url).json()
        todo_respons = requests.get(todo_url).json()

        
        mployee_name = None
        for user in user_respons:
            if user['id'] == int(employee_id):
                employee_name = user['name']
                break
        
        if employee_name is None:
            print(f"Error: Employee with ID {employee_id} not found")
            exit(1)
        
        Dn_task = [task["title"] for task in todo_respons if task["userId"] == int(employee_id) and task['completed']]
        total = len(todo_respons) + sum(1 for task in todo_respons if task['userId'] == int(employee_id))

        print(f"Employee {employee_name} is done with tasks("
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
