from flask import Flask, send_from_directory
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS



app = Flask(__name__)
load_dotenv()
token = os.environ.get('GITHUB_TOKEN')  
CORS(app, origins=["http://172.17.0.2:3001"])  # Allow requests from React app's IP and port

@app.route('/download_resume')
def download_resume():
    return send_from_directory(directory='static', filename='resume.pdf', as_attachment=True)





@app.route('/repos', methods=['GET'])
def resume():
    headers = {'Authorization': f'token {token}'}
    response = requests.get('https://api.github.com/users/DaniyalAhm/repos', headers=headers)
    
    # Debugging: Print response status code and content
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")

    repos = response.json()
    repos = {}
    for repo in repos:
        print(f"Name: {repo['name']}, URL: {repo['html_url']}")
        repos[repo['name']] = repo['html_url']

    print(repos)

    return repos

if __name__ == '__main__':
    app.run(debug=True)