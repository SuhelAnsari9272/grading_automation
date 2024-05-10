import requests

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

def get_content(repo_name,contents):
        for item in contents:
            if item['type']=='file':
                file_url = f"https://raw.githubusercontent.com/{repo_name}/main/{item['name']}"
                file_contents = read_file_from_url(file_url)
                if file_contents:
                    print(f"Contents of {item['name']}:")
                    print(file_contents)
                    #print(type(file_contents))
                else:
                    print(f"Failed to retrieve contents of {item['name']}")



if __name__ == "__main__":
    repo_name = "SuhelAnsari9272/assignment_1"  # Replace with actual GitHub repository name
    api_key = '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'
    contents = get_repository_contents(repo_name)
    get_content(repo_name=repo_name, contents= contents) 