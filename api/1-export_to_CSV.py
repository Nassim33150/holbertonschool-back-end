#!/usr/bin/python3
import sys
import requests
import csv

if __name__ == "__main__":
    Id = sys.argv[1]
    
    """ get userinformations with request"""
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(Id))
    
    """ get username """
    username = user.json().get('name')
    
    """ get all usertasks """
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
     
    with open(f"{Id}.csv", mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for task in tasks.json():
            if task.get('userId') == int(Id):
                writer.writerow([f'"{Id}"', f'"{username}"', f'"{task.get("completed")}"', f'"{task.get("title")}"'])
