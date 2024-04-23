#!/usr/bin/python3
"""Using what you did in the task #0, extend
your Python script to export data in the CSV format.
"""

from sys import argv
import csv
import requests


def export_to_csv(employee_id):
    """Function that uses restapi to get employee todo status to csv file"""

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_respons = requests.get(user_url)
        todo_respons = requests.get(todo_url)

        us_data = user_respons.json()
        todos_data = todo_respons.json()

        csv_file = f"{us_data['id']}.csv"

        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for task in todos_data:
                writer.writerow([us_data['id'], us_data['username'],
                                 task['completed'], task['title']])

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit()


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])
    export_to_csv(employee_id)
