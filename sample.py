import os
import requests
from openai import OpenAI


def retrieve_assignment_files(contents):
    assignment_files = []
    for item in contents:
        if item['type'] == 'file':
            assignment_files.append(item['name'])
    return assignment_files

def get_repository_contents(repo_name):
    # GitHub API endpoint for repository contents
    url = f"https://api.github.com/repos/{repo_name}/contents"
    
    # Send GET request to GitHub API
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error accessing repository.")
        return None


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            return file_contents
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# file_path = "D:\assignement automation\grading_automation\Statistics_decision_solution_updated.ipynb"  # Change "example.txt" to your file path
# contents = read_file(file_path)

if __name__ == "__main__":
    repo_name = "SuhelAnsari9272/assignment_1"  # Replace with actual GitHub repository name
    api_key = 'sk-proj-RmUNBIwjypdHCtTcZ90IT3BlbkFJugpkPRs1f9TwQKMU5luE'
    contents = get_repository_contents(repo_name)
    if contents:
        assignment_files = retrieve_assignment_files(contents)
        file_path = r"D:\assignement automation\grading_automation\Statistics_decision_solution_updated.ipynb"
        #print("Assignment Files:", assignment_files)
        file_contents = read_file(file_path)
        print(file_contents)

        #evaluate_assignment()
        # feedback, marking = evaluate_assignment(assignment_files, api_key)
        # print("Feedback:", feedback)
        # print("Marking:", marking)