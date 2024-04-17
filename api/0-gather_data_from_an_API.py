#!/usr/bin/python3
"""For a given employee ID, returns information about
their todo list progress"""
import sys
import requests

if __name__ == "__main__":

    Id = sys.argv[1]

    """ get userinformations with request"""
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(Id))

    """ get username """
    EMPLOYEE_NAME = user.json().get('name')

    """ get all usertasks """
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0

    for task in tasks.json():
        if task.get('userId') == int(Id):
            TOTAL_NUMBER_OF_TASKS += 1
            if task.get('completed'):
                NUMBER_OF_DONE_TASKS += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    print('\n'.join(["\t " + task.get('title') for task in tasks.json()
          if task.get('userId') == int(Id) and task.get('completed')]))
