#!/usr/bin/python3
import sys
import requests
import json

if __name__ == "__main__":
    Id = sys.argv[1]

    """ get userinformations with request"""
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(Id))

    """ get username """
    username = users.json().get('name')

    """ get all usertasks """
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')

    dictionary = {}

    for task in tasks.json():
        if task.get('userId') == int(Id):
            dictionary = {
                Id: [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": username
                    }
                ]
            }

    json_object = json.dumps(dictionary)

    with open(f"{Id}.json", "w") as outfile:
        outfile.write(json_object)
