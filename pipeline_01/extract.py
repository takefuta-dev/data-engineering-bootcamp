import csv
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response.status_code)

users = response.json()

transformed_users = []

for user in users:
    transformed_user = {
        "name": user["name"],
        "city": user["address"]["city"]
    }

    transformed_users.append(transformed_user)

print(transformed_users)

with open("pipeline_01/users.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "city"])
    writer.writeheader()
    writer.writerows(transformed_users)