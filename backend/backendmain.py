from flask import Flask, send_from_directory, jsonify
import requests
import os
from dotenv import load_dotenv
from flask_cors import CORS
import base64
import re
from flask_pymongo import PyMongo

app = Flask(__name__)
load_dotenv()
token = os.environ.get('GITHUB_TOKEN')
CORS(app, origins=["http://localhost:3001"])

# Load MongoDB URI from environment variables
mongo_uri = os.environ.get('MONGO_URI')
if not mongo_uri:
    raise ValueError("No MongoDB URI found in environment variables")

# Debug: Print the MongoDB URI to ensure it is loaded correctly
print("MongoDB URI:", mongo_uri)

app.config["MONGO_URI"] = mongo_uri
mongo = PyMongo(app)

# Debug: Check if mongo.db is None
if mongo.db is None:
    print("Failed to connect to MongoDB")

headers = {'Authorization': f'token {token}'}

@app.route('/download_resume')
def download_resume():
    return send_from_directory(directory='static', filename='resume.pdf', as_attachment=True)

def fetch_from_database():
    repos_database = mongo.db.repo.find()
    repos_database_names = {item['name']: True for item in repos_database}
    response = requests.get('https://api.github.com/users/DaniyalAhm/repos', headers=headers) 
    repos = response.json()
    for repo in repos:
        if repo[ 'name'] not in repos_database_names:

            dbrepos = list(mongo.db.repo.find(repo['name']))


            print(f"Adding new repository: {repo['name']}")
            add_repo(repo)
            repos_database_names[repo['name']] = True
        elif dbrepos ['commit'] != get_latest_commit(repo['name']):
            
            print(f"Updating repository: {repo['name']}")
            mongo.db.repo.delete_one({'name': repo['name']})
            add_repo(repo)


    full_data = list(mongo.db.repo.find())
    result = []
    for repo in full_data:
        if repo['Display'] == True:
            result.append(repo)
            




    return result
def get_latest_commit(repo_name):
    url = f'https://api.github.com/repos/DaniyalAhm/{repo_name}/commits'
    commits_response = requests.get(url, headers=headers)
    commits = commits_response.json()

    if len(commits) > 0:
        return commits[0]['sha']
    return ''



def add_repo(repo):
    description = ''
    Display = False
    check = ' <!-- DISPLAY=TRUE -->'
    readme_response = requests.get(f'https://api.github.com/repos/DaniyalAhm/{repo["name"]}/readme', headers=headers)
    if readme_response.status_code == 200:
        readme_content = readme_response.json().get('content', '')
        readme_content = base64.b64decode(readme_content).decode('utf-8')
        if check in readme_content:
            Display = True
            readme_content = readme_content.replace(check, '')

        clean_readme_content = clean_html(readme_content)


        url = f'https://api.github.com/repos/DaniyalAhm/{repo}/commits'
        commits_response = requests.get(url, headers=headers)
        commits = commits_response.json()
        if len(commits) > 0:
            commit = commits[0]
            commit_sha = commit['sha']

        description = summarizer(clean_readme_content)
        description = description.replace('#', '')

    repo_info = {
        'commit':commit_sha,
        'name': repo['name'],
        'url': repo['html_url'],
        'description': description,
        'Display': Display
    }



    mongo.db.repo.insert_one(repo_info)

@app.route('/repos', methods=['GET'])
def repos():
    repos = fetch_from_database()
    for repo in repos:
        repo['_id'] = str(repo['_id'])
    return jsonify(repos)

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def summarizer(text):
    # Load model directly
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

    tokenizer = AutoTokenizer.from_pretrained("Falconsai/text_summarization")
    model = AutoModelForSeq2SeqLM.from_pretrained("Falconsai/text_summarization")

    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary

if __name__ == '__main__':
    app.run(debug=True)
