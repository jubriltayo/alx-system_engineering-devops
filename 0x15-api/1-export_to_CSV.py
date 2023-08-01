#!/usr/bin/python3
"""export to csv of employee TODO list information from a REST API"""

import csv
import json
import requests
import sys


if __name__ == "__main__":
    # Get employee name
    url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])
    user_ep = "{}/users/{}".format(url, user_id)
    username = requests.get(user_ep).json().get("username")

    # Get employee tasks
    tasks_ep = "{}/todos".format(url)
    tasks = requests.get(tasks_ep).json()
    user_tasks = [[user_id, username, task.get("completed"),
                  task.get("title")] for task in tasks
                  if user_id == task.get("userId")]

    # Save to csv
    with open("{}.csv".format(user_id), 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        # Add each row of data to csv file
        for row in user_tasks:
            writer.writerow(row)
