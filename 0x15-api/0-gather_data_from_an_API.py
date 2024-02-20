#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def fetch_todo_progress(employee_id):
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = response.json()

    employee_name = None
    for user in users:
        if user['id'] == employee_id:
            employee_name = user['name']
            break

    if employee_name is None:
        print("Employee not found.")
        return

    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todo_response = requests.get(todo_url)
    todos = todo_response.json()

    total_tasks = len(todos)
    completed_tasks = [todo['title'] for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks(
            {num_completed_tasks}/{total_tasks}): ")
    for task in completed_tasks:
        print(f"\t{task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    fetch_todo_progress(employee_id)
