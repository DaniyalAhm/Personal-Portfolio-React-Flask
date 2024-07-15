import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get('GITHUB_TOKEN')
print(token)
def resume():
    headers = {'Authorization': f'token {token}'}
    response = requests.get('https://api.github.com/users/DaniyalAhm/repos', headers=headers)
    
    # Debugging: Print response status code and content
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")

    repos = response.json()
    for repo in repos:
        print(f"Name: {repo['name']}, URL: {repo['html_url']}")

if __name__ == '__main__':
    resume()
