import os
import requests
from openai import OpenAI

def read_file_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

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

def evaluate_assignment(assignment_files,api_key):
    # Initialize OpenAI API
    openai = OpenAI(api_key = api_key)
    # sk-proj-RmUNBIwjypdHCtTcZ90IT3BlbkFJugpkPRs1f9TwQKMU5luE
    
    # Concatenate assignment files for evaluation
    # assignment_text = ""
    # for file in assignment_files:
    #     with open(file, 'r') as f:
    #         assignment_text += f.read() + '\n'
    
    # Call OpenAI API for evaluation
    evaluation_result = openai.complete(prompt=assignment_files, max_tokens=150)
    
    # Retrieve feedback and marking from OpenAI's response
    feedback = evaluation_result['choices'][0]['text']
    marking = calculate_marking(evaluation_result['choices'][0]['text'])
    
    return feedback, marking

def calculate_marking(feedback):
    # Implement your evaluation criteria here
    # For example, you could analyze the feedback and assign a score out of 100
    marking = 90  # Placeholder, replace with your scoring algorithm
    return marking


if __name__ == "__main__":
    repo_name = "SuhelAnsari9272/assignment_1"  # Replace with actual GitHub repository name
    api_key = 'sk-proj-RmUNBIwjypdHCtTcZ90IT3BlbkFJugpkPRs1f9TwQKMU5luE'
    contents = get_repository_contents(repo_name)
    if contents:
        # Iterate through each item in the repository contents
        for item in contents:
            # Check if the item is a file
            if item['type'] == 'file':
                # Construct the URL of the file
                file_url = f"https://raw.githubusercontent.com/{repo_name}/main/{item['name']}"
                # Read the contents of the file from the URL
                file_contents = read_file_from_url(file_url)
    
    feedback, marking = evaluate_assignment(file_contents,api_key)
    