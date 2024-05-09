import os
import requests
from openai import OpenAI

# Step 2: Access GitHub Repository
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

# Step 3: Retrieve Assignment Files
def retrieve_assignment_files(contents):
    assignment_files = []
    for item in contents:
        if item['type'] == 'file':
            assignment_files.append(item['name'])
    return assignment_files

# Step 4: Integration with ChatGPT
def evaluate_assignment(assignment_files,api_key):
    # Initialize OpenAI API
    openai = OpenAI(api_key = api_key)
    # sk-proj-RmUNBIwjypdHCtTcZ90IT3BlbkFJugpkPRs1f9TwQKMU5luE
    
    # Concatenate assignment files for evaluation
    assignment_text = ""
    for file in assignment_files:
        with open(file, 'r') as f:
            assignment_text += f.read() + '\n'
    
    # Call OpenAI API for evaluation
    evaluation_result = openai.complete(prompt=assignment_text, max_tokens=150)
    
    # Retrieve feedback and marking from OpenAI's response
    feedback = evaluation_result['choices'][0]['text']
    marking = calculate_marking(evaluation_result['choices'][0]['text'])
    
    return feedback, marking

# Step 5: Evaluation Criteria (You can customize this)
def calculate_marking(feedback):
    # Implement your evaluation criteria here
    # For example, you could analyze the feedback and assign a score out of 100
    marking = 90  # Placeholder, replace with your scoring algorithm
    return marking

# Example usage
if __name__ == "__main__":
    repo_name = "SuhelAnsari9272/assignment_1"  # Replace with actual GitHub repository name
    api_key = 'sk-proj-RmUNBIwjypdHCtTcZ90IT3BlbkFJugpkPRs1f9TwQKMU5luE'
    contents = get_repository_contents(repo_name)
    if contents:
        assignment_files = retrieve_assignment_files(contents)
        print("Assignment Files:", assignment_files)
        feedback, marking = evaluate_assignment(assignment_files, api_key)
        print("Feedback:", feedback)
        print("Marking:", marking)
