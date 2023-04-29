#!/usr/bin/python3
"""prints employee TODO list information from a REST API"""

import requests
import sys


if __name__ == "__main__":
    # Get employee name
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user_ep = "{}/users/{}".format(url, user_id)
    name = requests.get(user_ep).json().get("name")

    # Get employee tasks
    tasks_ep = "{}/todos".format(url)
    tasks = requests.get(tasks_ep).json()
    tasks_t = [dict for dict in tasks if dict.get("userId") == int(user_id)]
    tasks_c = [dict for dict in tasks_t if dict.get("completed")]

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(tasks_c), len(tasks_t)))
    for task in tasks_c:
        print("\t {}".format(task.get("title")))
