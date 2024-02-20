#!/usr/bin/python3
""" a  script to export data in the CSV format """
import sys
import csv
import requests


def fetch_todo_progress(employee_id):
    """ Fetch user details """
    user_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user_data = user_response.json()

    if 'id' not in user_data:
        print("User not found.")
        return
    
    user_id = user_data['id']
    username = user_data['username']
    
    # Fetch TODO list for the user
    todos_response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos_data = todos_response.json()

    if len(todos_data) == 0:
        print(f"No TODOs found for user {username}.")
        return
    
    # Write data to CSV file
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos_data:
            task_completed_status = "True" if todo['completed'] else "False"
            task_title = todo['title']
            writer.writerow([user_id, username, task_completed_status, task_title])
    
    print(f"Data exported to {filename} successfully.")


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
