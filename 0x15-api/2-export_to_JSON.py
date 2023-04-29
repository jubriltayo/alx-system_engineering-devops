#!/usr/bin/python3
"""export to json of  employee TODO list information from a REST API"""

import json
import requests
import sys


if __name__ == "__main__":
    # Get employee name
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user_ep = "{}/users/{}".format(url, user_id)
    username = requests.get(user_ep).json().get("username")

    # Get employee tasks
    tasks_ep = "{}/todos".format(url)
    tasks = requests.get(tasks_ep).json()
    tasks_user = {user_id: [{"task": task.get("title"),
                             "completed": task.get("completed"),
                             "username": username}
                            for task in tasks if task.get("userId") ==
                            int(user_id)]
                  }

    # Write output to json
    with open("{}.json".format(user_id), 'w', encoding='utf-8') as f:
        json.dump(tasks_user, f)
