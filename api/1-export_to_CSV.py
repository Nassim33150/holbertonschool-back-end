#!/usr/bin/python3
""" Records all tasks that are owned by this employee """
import sys
import requests
import csv

if __name__ == "__main__":
    USER_ID = sys.argv[1]

    """ get userinformations with request"""
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(USER_ID))

    """ get username """
    EMPLOYEE_NAME = user.json().get('name')

    """ get all usertasks """
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')

    """ write to CSV """
    with open(f"{USER_ID}.csv", mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for task in tasks.json():
            if task.get('userId') == int(USER_ID):
                TASK_COMPLETED_STATUS = task.get('completed')
                TASK_TITLE = task.get('title')
                writer.writerow([
                    f'"{USER_ID}"',
                    f'"{EMPLOYEE_NAME}"',
                    f'"{TASK_COMPLETED_STATUS}"',
                    f'"{TASK_TITLE}"'
                ])
