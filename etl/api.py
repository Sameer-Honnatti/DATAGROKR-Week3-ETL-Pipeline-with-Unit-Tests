import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

def fetch_users():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()

def user_generator(users):
    for user in users:
        yield user

def fetch_user_generator():
    users = fetch_users()
    return user_generator(users)