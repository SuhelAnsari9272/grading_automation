import requests
import pandas as pd

def read_file_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
def is_file_present(files_list, file_name):
    for file_info in files_list:
        if file_info['name'] == file_name:
            return "Yes", 1
    return "No", 0


if __name__ == "__main__":
    repo_name = "SuhelAnsari9272/assignment_1"  # Replace with actual GitHub repository name
    #api_key = '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'
    url = f"https://api.github.com/repos/{repo_name}/contents"

    files_list = read_file_from_url(url)
    if files_list is not None:
        assignment_1, marks_1 = is_file_present(files_list,'assignment_1.py')
        assignment_2, marks_2 = is_file_present(files_list,'assignment_2.py')
        assignment_3, marks_3 = is_file_present(files_list,'assignment_3.py')

    sub_csv = pd.read_csv(r'D:\assignement automation\grading_automation\submission.csv')
    user_name = repo_name.split(sep='/')[0]
    new_data = {'name':user_name,'assingment1_submitted':assignment_1,'assingment2_submitted':assignment_2, 'assingment3_submitted':assignment_3,  
                'assingment1_marks':marks_1,'assingment2_marks':marks_2,'assingment3_marks':marks_3}
    new_df = pd.DataFrame(new_data,index=[0])
    sub_csv = pd.concat([sub_csv,new_df], ignore_index=True)

    sub_csv.to_csv(r'D:\assignement automation\grading_automation\submission.csv', index=False)
