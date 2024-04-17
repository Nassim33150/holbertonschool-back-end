#!/usr/bin/python3
""" Records all tasks that are owned by this employee """
import sys
import requests
import json

if __name__ == "__main__":
    USER_ID = sys.argv[1]

    """ get userinformations with request"""
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(USER_ID))

    """ get username """
    USERNAME = users.json().get('name')

    """ get all usertasks """
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')

    dictionary = {}

    for task in tasks.json():
        if task.get('userId') == int(USER_ID):
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            dictionary = {
                USER_ID: [
                    {
                        "task": TASK_TITLE,
                        "completed": TASK_COMPLETED_STATUS,
                        "username": USERNAME
                    }
                ]
            }

    json_object = json.dumps(dictionary)

    with open(f"{USER_ID}.json", "w") as outfile:
        outfile.write(json_object)
