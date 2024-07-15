import requests
from functools import cache


@cache
def get_api_key():
    # Fill out the key below
    key = ''
    return key


@cache
def get_headers():
    api_key = get_api_key()
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    return headers


def list_repos(username):
    url = f"https://api.bitbucket.org/2.0/repositories/{username}"
    try:
        response = requests.get(url, headers=get_headers())
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error listing repositories: {e}")
        return None


def create_repo(username, repo_name, is_private=True):
    url = f"https://api.bitbucket.org/2.0/repositories/{username}/{repo_name}"
    data = {"scm": "git", "is_private": is_private}
    try:
        response = requests.post(url, headers=get_headers(), json=data)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error creating repository: {e}")
        return None


def delete_repo(username, repo_name):
    url = f"https://api.bitbucket.org/2.0/repositories/{username}/{repo_name}"
    try:
        response = requests.delete(url, headers=get_headers())
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error deleting repository: {e}")
        return None
