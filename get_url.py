import requests
from openai import OpenAI

# Function to retrieve file content from GitHub
def retrieve_file_content(file_url):
    response = requests.get(file_url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error retrieving file content from {file_url}")
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

# Step 4: Integration with ChatGPT
def evaluate_assignment(files, api_key):
    # Initialize OpenAI API
    openai = OpenAI(api_key=api_key)
    
    # Concatenate assignment files for evaluation
    assignment_text = ""
    for file_url in files:
        file_content = retrieve_file_content(file_url)
        if file_content:
            assignment_text += file_content + '\n'
    
    if assignment_text:
        # Call OpenAI API for evaluation
        evaluation_result = openai.complete(prompt=assignment_text, max_tokens=150)
        
        # Retrieve feedback and marking from OpenAI's response
        feedback = evaluation_result['choices'][0]['text']
        marking = calculate_marking(evaluation_result['choices'][0]['text'])
        return feedback, marking
    else:
        print("No files to evaluate.")
        return None, None

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
        # Construct file URLs
        base_url = "https://raw.githubusercontent.com/"
        files = [f"{base_url}{repo_name}/main/{item['name']}" for item in contents if item['type'] == 'file']
        print(files)
        # if files:
        #     feedback, marking = evaluate_assignment(files, api_key)
        #     if feedback is not None and marking is not None:
        #         print("Feedback:", feedback)
        #         print("Marking:", marking)
        # else:
        #     print("No files found in the repository.")
