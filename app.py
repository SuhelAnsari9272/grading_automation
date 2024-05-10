import os
import requests
import openai

def read_file_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

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

def get_content(repo_name,contents):
        for item in contents:
            if item['type']=='file':
                file_url = f"https://raw.githubusercontent.com/{repo_name}/main/{item['name']}"
                file_contents = read_file_from_url(file_url)
                if file_contents:
                    #print(f"Contents of {item['name']}:")
                    return file_contents
                else:
                    return f"Failed to retrieve contents of {item['name']}"


# Step 4: Integration with ChatGPT
def summary_assignment(assignment_text,api_key):
    
    # Call OpenAI API for evaluation
    summarization_prompt =  f"Is the following code correct? Code: '{assignment_text}'" 

    #feedback prompt
    feedback_prompt = 'Give the feedback about the code and give mark out of 100'
    
    # Retrieve feedback and marking from OpenAI's response
    feedback_response = openai.Completion.create(
        #engine="text-davinci-002",
        model = "gpt-3.5-turbo",
        prompt = feedback_prompt,
        max_tokens = 150,
        api_key = api_key )
    
    marking_response = openai.Completion.create(
        #engine="text-davinci-002",
        model= "gpt-3.5-turbo",
        prompt=feedback_prompt,
        max_tokens=150,
        api_key=api_key
    )

    # Extract and return the summary and sentiment analysis
    feedback = feedback_response.choices[0].text
    marking = marking_response.choices[0].text
    
    return {'feedback': feedback, 'marking': marking}

# Step 5: Evaluation Criteria (You can customize this)
def calculate_marking(feedback):
    # Implement your evaluation criteria here
    # For example, you could analyze the feedback and assign a score out of 100
    marking = 90  # Placeholder, replace with your scoring algorithm
    return marking

# Example usage
if __name__ == "__main__":
    repo_name = "SuhelAnsari9272/assignment_1"  # Replace with actual GitHub repository name
    api_key = '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'
    contents = get_repository_contents(repo_name)
    assignment_text = get_content(repo_name,contents)
    result = summary_assignment(assignment_text = assignment_text,api_key = api_key)
    print('feedback :' , result['feedback'])
    print('marking: ', result['marking'])