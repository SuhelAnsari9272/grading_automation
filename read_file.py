import requests

def read_file_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
url = "https://raw.githubusercontent.com/SuhelAnsari9272/assignment_1/main/Statistics_decision_solution_updated.ipynb"
contents = read_file_from_url(url)
if contents:
    print(contents)

