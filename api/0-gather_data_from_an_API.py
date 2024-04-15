#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":

    Id = sys.argv[1]

    """ get userinformations with request"""
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(Id))

    """ get username """
    username = user.json().get('name')

    """ get all usertasks """
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completedTasks = 0

    for task in tasks.json():
        if task.get('userId') == int(Id):
            totalTasks += 1
            if task.get('completed'):
                completedTasks += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(username, completedTasks, totalTasks))

    print('\n'.join(["\t " + task.get('title') for task in tasks.json()
          if task.get('userId') == int(Id) and task.get('completed')]))
