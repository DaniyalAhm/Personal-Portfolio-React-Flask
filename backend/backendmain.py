from flask import Flask, send_from_directory, jsonify
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS



app = Flask(__name__)
load_dotenv()
token = os.environ.get('GITHUB_TOKEN')  
CORS(app, origins= ["http://localhost:3001"])
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
    formatted_repos = []
    for repo in repos:
        formatted_repos.append({
            'name': repo['name'],
            'url': repo['html_url'],
            'description': 'This is where I would put a description of the repo, if I had one.'


        })



    return jsonify(formatted_repos)

if __name__ == '__main__':
    app.run(debug=True)