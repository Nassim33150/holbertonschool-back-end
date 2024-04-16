#!/usr/bin/python3
import requests
import json

""" Records all tasks from all employees """
if __name__ == "__main__":
    
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    
    user_tasks = {}

    
    for user in users:
        user_id = user['id']
        username = user['name']

        
        user_task_list = []

        
        for task in tasks:
            if task['userId'] == user_id:
                user_task_list.append({
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                })

        
        user_tasks[user_id] = user_task_list

    
    with open("todo_all_employees.json", "w") as outfile:
        json.dump(user_tasks, outfile)
