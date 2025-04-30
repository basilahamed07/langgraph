import requests
def process_responses(inputes,token, url):
    collection = []
    # Iterate over each model and its associated prompts
    question = [inputes]
    for trash in question:
        # Prepare headers and payload
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        payload = {
            'model': "deepseek-r1:14b",
            'messages': [{'role': 'user', 'content': trash}]
        }
        
        # Send request to the external API
        response = requests.post(url, headers=headers, json=payload)
        collection+=[response.json()]
    return collection



if __name__ == '__main__':
    while True:
        finals = process_responses(input("ENter the prompt"),"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjQzNTJkM2M0LTBkMmYtNDJhMS1hYmZmLTE0NzZmYTZjOWVkZiJ9.3i2TnvUEUQIymyVYSyQ1ZUMJvf7OqtLEF-YKXC5EFFE",url="http://44.213.24.224:8080/api/chat/completions"
        )

        for trash in finals: 
            print("responde start")
            print(trash)
            print("respond end")
