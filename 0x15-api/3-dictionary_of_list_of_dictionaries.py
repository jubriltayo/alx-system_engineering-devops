#!/usr/bin/python3
"""export to json all employee TODO list information from a REST API"""

import json
import requests
import sys


if __name__ == "__main__":
    # Get employee name
    url = "https://jsonplaceholder.typicode.com"
    user_ep = "{}/users".format(url)
    users = requests.get(user_ep).json()

    # Get employee tasks
    tasks_ep = "{}/todos".format(url)
    tasks = requests.get(tasks_ep).json()
    tasks_user = {user.get("id"): [{"username": user.get("username"),
                                    "task": task.get("title"),
                                    "completed": task.get("completed")}
                                   for task in tasks if task.get("userId") ==
                                   user.get("id")]
                  for user in users
                  }

    # Save to json
    with open("todo_all_employees.json", 'w', encoding='utf-8') as f:
        json.dump(tasks_user, f)
