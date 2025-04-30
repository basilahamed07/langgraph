# import csv
# import requests
# import time

# models_prompts = {
#     "qwen2.5-coder:14b": [
#         "Write a Python function to sort a list of dictionaries by a key.",
#         "Generate a SQL query to find duplicate records in a table.",
#         "Optimize the following Python code for speed.",
#         "Explain the difference between merge sort and quicksort.",
#         "Write a regex pattern to validate email addresses."
#     ],
#     "deepseek-r1:14b": [
#         "Summarize the key findings of a research paper on the ethical implications of space exploration.",
#         "Generate a detailed prompt for training a chatbot to assist with space tourism and cosmic travel",
#         "Compare the performance of different space telescope architectures in observing distant galaxies",
#         "Explain how reinforcement learning could be used to optimize interplanetary missions",
#         "Analyze the sentiment of a given review from an astronaut about living aboard a space station"
#     ]
#     # "asis-workorder": [
#     #     "Generate a work order for repairing an industrial machine.",
#     #     "Extract key details from a maintenance log.",
#     #     "Classify work orders based on urgency and type.",
#     #     "Summarize a list of completed work orders for a monthly report.",
#     #     "Suggest optimizations for scheduling work orders efficiently."
#     # ],
#     # "ifac-x-workorder-model": [
#     #     "Create a workflow for tracking equipment repairs.",
#     #     "Predict maintenance needs based on historical data.",
#     #     "Generate an automated email notification for pending work orders.",
#     #     "Translate a work order into a structured data format.",
#     #     "Identify bottlenecks in the work order processing pipeline."
#     # ],
#     # "sakthivel-bulkpromotions-model": # not working
#     #      [
#     #         "Generate promotional email content for a flash sale.",
#     #         "Suggest personalized discount offers based on user behavior.",
#     #         "Create social media ad copy for a new product launch.",
#     #         "Analyze customer response data for a recent promotion.",
#     #         "Draft a bulk SMS campaign for a seasonal discount event."
#     #     ],
#     # "poc---document-generator": 
#     #      [
#     #         "Generate a formal business proposal template.",
#     #         "Convert meeting notes into a structured report.",
#     #         "Create a contract agreement with customizable clauses.",
#     #         "Summarize a legal document in plain language.",
#     #         "Draft a project status report based on task updates."
#     #     ],
#     # "super-man": [
#     #     "Write a short story where Superman faces a moral dilemma.",
#     #     "Generate a dialogue between Superman and Lex Luthor.",
#     #     "Describe the scientific plausibility of Superman's abilities.",
#     #     "Rewrite a famous Superman comic scene with a twist.",
#     #     "Create a training regimen for someone who wants to be like Superman."
#     # ]
# }


# chatgroq = ["qwen-2.5-coder-32b","deepseek-r1-distill-qwen-32b"]

# from langchain_groq import ChatGroq

# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
#     # other params...
# )

# # Sakthivel_BulkPromotions_Model = "This is exclusively for the Bulk Promotions POC"
# # POC_DOC_GENERATOR = "POC - Document Generator"

# # models_name = ["qwen2.5-coder:14b","deepseek-r1:14b","ASIS WorkOrder Model","IFAC-X WorkOrder Model","Sakthivel-BulkPromotions-Model","POC - Document Generator","super man","super-man"]

# index = 0
# def process_responses(models_prompts, token, url):
#     with open('responses.csv', mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(["open_web_ui_time_taken","open_web_ui_question", "open_web_ui_answer", "chatgroq_time_taken","chatgroq_question", "chatgroq_answer"])
        
#         for model, prompts in models_prompts.items():
#             for question in prompts:
#                 headers = {
#                     'Authorization': f'Bearer {token}',
#                     'Content-Type': 'application/json'
#                 }
#                 payload = {
#                     'model': model,
#                     'messages': [{'role': 'user', 'content': question}]
#                 }
                
#                 response = requests.post(url, headers=headers, json=payload)
#                 if response.status_code == 200:
#                     try:
#                         data = response.json()  # Parsing JSON response
#                         print("")
#                         print("")
#                         print("")
                        
#                         print(data)
#                         print("")
                        
#                         # Get response details, with fallback to 'N/A' if not present
#                         # response_id = data.get("id", "N/A")
#                         # Correct handling for nested structure in 'choices'
#                         answer = data.get("choices", [{}])[0].get("message", {}).get("content", "N/A")
                        
#                         # Ensure answer content is sanitized (removing unwanted characters)
#                         answer = answer.replace("\n", " ").replace("\r", " ").strip()
                        
#                         # Extract time taken and tokens used from 'usage' field
#                         time_taken = data.get("usage", {}).get("approximate_total", "N/A")
#                         # tokens_used = data.get("usage", {}).get("total_tokens", "N/A")
#                         #get the responde from the chatgroq
#                         llm = ChatGroq(
#                             model=chatgroq[index],
#                             temperature=0,
#                             max_tokens=None,
#                             timeout=None,
#                             max_retries=2,
#                             groq_api_key="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"# other params...
#                             )
                        
#                         response = llm.invoke(question)
#                         answer = data.get("choices", [{}])[0].get("message", {}).get("content", "N/A")
                        
#                         # Ensure answer content is sanitized (removing unwanted characters)
#                         answer1 = response.content.replace("\n", " ").replace("\r", " ").strip()
                        
#                         # Extract time taken and tokens used from 'usage' field
#                         time_taken1 = response.response_metadata["token_usage"]["total_time"]
#                         # Writing to CSV file
#                         writer.writerow([time_taken,question, answer,time_taken1,question,answer1])
#                         print("")
#                         # print(f"Processed: {response_id}")
#                         print("")
#                         print("")
#                     except Exception as e:
#                         print(f"Error processing response: {e}")
#                         writer.writerow(["Error", question, "Error parsing JSON", "N/A", "N/A"])
#                 else:
#                     print(f"Error: {response.status_code}")
#                     writer.writerow(["Error", question, "Error with request", "N/A", "N/A"])
                
#                 time.sleep(1)  # Avoid rate limits

# if __name__ == '__main__':
#     process_responses(models_prompts,"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjE5ZTFlNWUxLWQ2YjktNGFhZS1hMGJmLTUwN2M2ZmQ2ZmExNyJ9.P4ucoUuSXADyqUZZuDHTA3u5A1yutrVM2xnBqS6P8_E",url="http://18.208.244.147:8080/api/chat/completions")






# url = 'http://18.208.244.147:8080/api/chat/completions'

# # import requests
# # import csv
# # import time

# # def process_responses(models_prompts, token, url):
# #     with open('responses.csv', mode='w', newline='', encoding='utf-8') as file:
# #         writer = csv.writer(file)
# #         writer.writerow(["id", "question", "answer", "time_taken", "tokens_used"])
        
# #         for model, prompts in models_prompts.items():
# #             for question in prompts:
# #                 headers = {
# #                     'Authorization': f'Bearer {token}',
# #                     'Content-Type': 'application/json'
# #                 }
# #                 payload = {
# #                     'model': model,
# #                     'messages': [{'role': 'user', 'content': question}]
# #                 }
                
# #                 response = requests.post(url, headers=headers, json=payload)
# #                 if response.status_code == 200:
# #                     try:
# #                         data = response.json()  # Parsing JSON response
# #                         print(data)
                        
# #                         # Get response details, with fallback to 'N/A' if not present
# #                         response_id = data.get("id", "N/A")
# #                         # Correct handling for nested structure in 'choices'
# #                         answer = data.get("choices", [{}])[0].get("message", {}).get("content", "N/A")
                        
# #                         # Ensure answer content is sanitized (removing unwanted characters)
# #                         answer = answer.replace("\n", " ").replace("\r", " ").strip()
                        
# #                         # Extract time taken and tokens used from 'usage' field
# #                         time_taken = data.get("usage", {}).get("approximate_total", "N/A")
# #                         tokens_used = data.get("usage", {}).get("total_tokens", "N/A")
                        
# #                         # Writing to CSV file
# #                         writer.writerow([response_id, question, answer, time_taken, tokens_used])
                        
# #                         print(f"Processed: {response_id}")
# #                     except Exception as e:
# #                         print(f"Error processing response: {e}")
# #                         writer.writerow(["Error", question, "Error parsing JSON", "N/A", "N/A"])
# #                 else:
# #                     print(f"Error: {response.status_code}")
# #                     writer.writerow(["Error", question, "Error with request", "N/A", "N/A"])
                
# #                 time.sleep(1)  # Avoid rate limits

# # # Example usage
# # models_prompts = {
# #     "deepseek-r1:14b": ["Why is the sky blue?", "What is the capital of France?"],
# # }

# # token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjE5ZTFlNWUxLWQ2YjktNGFhZS1hMGJmLTUwN2M2ZmQ2ZmExNyJ9.P4ucoUuSXADyqUZZuDHTA3u5A1yutrVM2xnBqS6P8_E"
# # process_responses(models_prompts, token)





import csv
import requests
import time
from langchain_groq import ChatGroq

# Model-specific prompts
model_prompt = {
    "qwen2.5-coder:14b": [
        """
        Write a Python function that sorts a list of dictionaries by multiple keys, where the primary key is in ascending order and the secondary key is in descending order. The function should handle missing keys gracefully by assuming a default value.
        """,
        """
        Optimize a given Python function that processes large numerical datasets to improve its time complexity, ensuring minimal memory usage.
        """,
        # """
        # Implement a thread-safe caching mechanism in Python that supports both LRU and LFU eviction policies.
        # """,
        # """
        # Generate a SQL query to efficiently find overlapping date ranges in a database table containing booking records.
        # """,
        # """
        # Write a regular expression pattern that validates IPv4 and IPv6 addresses, ensuring compliance with standard formats.
        # """
    ],

    "deepseek-r1:14b": [
        """
        Provide a comprehensive summary of the key findings in a research paper discussing the ethical implications of space exploration, specifically addressing issues such as planetary protection, space debris management, and the equitable use of extraterrestrial resources.
        """,
        """
        Analyze the impact of AI-driven decision-making in space mission planning, focusing on ethical concerns and biases in autonomous systems.
        """,
        # "
        # """
        # Explain the potential consequences of space militarization on international relations and the peaceful use of outer space.
        # """,
        # """
        # Investigate the psychological and social effects of long-duration space travel on astronauts and propose mitigation strategies.
        # """
    ]
}


# List of ChatGroq models
# chatgroq_models = ["qwen-2.5-coder-32b", "deepseek-r1-distill-qwen-32b"]
chatgroq_models = ["deepseek-r1:14b"]

# API Key for ChatGroq
GROQ_API_KEY = "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"

def process_responses(models_prompts, token, url):
    with open('responses.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            "open_web_ui_time_taken", "open_web_ui_question", "open_web_ui_answer",
            "chatgroq_time_taken", "chatgroq_question", "chatgroq_answer"
        ])
        
        # Iterate over each model and its associated prompts
        for model, prompts in models_prompts.items():
            for question in prompts:
                # Prepare headers and payload
                headers = {
                    'Authorization': f'Bearer {token}',
                    'Content-Type': 'application/json'
                }
                payload = {
                    'model': model,
                    'messages': [{'role': 'user', 'content': question}]
                }
                
                # Send request to the external API
                response = requests.post(url, headers=headers, json=payload)

                if response.status_code == 200:
                    try:
                        data = response.json()  # Parse JSON response
                        print("\nProcessing response:", data)

                        # Extract answer from the first API
                        answer = data.get("choices", [{}])[0].get("message", {}).get("content", "N/A").strip()

                        # Extract response time taken
                        time_taken = data.get("usage", {}).get("approximate_total", "N/A")

                        # Select the ChatGroq model (cycling through the list)
                        chatgroq_model = chatgroq_models[0] if "qwen2.5-coder" in model else chatgroq_models[1]

                        # Initialize ChatGroq with the selected model
                        llm = ChatGroq(
                            model=chatgroq_model,
                            temperature=0,
                            max_tokens=None,
                            timeout=None,
                            max_retries=2,
                            groq_api_key=GROQ_API_KEY
                        )

                        # Get response from ChatGroq
                        chatgroq_response = llm.invoke(question)

                        # Extract answer from ChatGroq
                        chatgroq_answer = chatgroq_response.content.strip()

                        # Extract response time from ChatGroq
                        chatgroq_time_taken = chatgroq_response.response_metadata["token_usage"]["total_time"]

                        # Write to CSV file
                        writer.writerow([time_taken, question, answer, chatgroq_time_taken, question, chatgroq_answer])

                        print("\nSuccessfully processed question:", question)
                        print("\n-------------------------\n")

                    except Exception as e:
                        print(f"Error processing response: {e}")
                        writer.writerow(["Error", question, "Error parsing JSON", "Error", question, "Error parsing JSON"])
                else:
                    print(f"Error: {response.status_code} for question: {question}")
                    writer.writerow(["Error", question, "Error with request", "Error", question, "Error with request"])
                
                # Sleep to prevent rate limiting
                time.sleep(1)

if __name__ == '__main__':
    process_responses(
        model_prompt,
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjQzNTJkM2M0LTBkMmYtNDJhMS1hYmZmLTE0NzZmYTZjOWVkZiJ9.3i2TnvUEUQIymyVYSyQ1ZUMJvf7OqtLEF-YKXC5EFFE",
        url="http://44.213.24.224:8080/api/chat/completions"
    )



