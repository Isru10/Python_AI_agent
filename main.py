import os 
import sys
from dotenv import load_dotenv

from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info

from functions.get_file_content import schema_get_file_content

from functions.run_python_file import schema_run_python_file

from functions.write_file import schema_write_file



from call_functions import call_function



def main():


    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    system_prompt = (""" you are a helpfull ai coding agent. when a user asks a question make a function call plan. 
                     you can perform the followig operations: 
                     
                     -list files and direcories 
                     -read content of a file 
                     -write or overwrite content to a file ( creating or update)
                     -run a python file with optional args 
when a user asks about code project they are referring to the working directory so you should typically start by looking at tje project files and figuring out how to run the project and how to run its tests, you will always want to test the tests and the actual project to verify that behaviour is working.
                     all paths you provide should be relative to the working directory. you dont need to specify the working directory in your function calls as it is automatically injected for security reasons. """)
    if len(sys.argv)<2 :
        print("I need a prompt")
        sys.exit(1)

    verbose_flag = False
    if len(sys.argv)==3 and sys.argv[2]=="--verbose":
        verbose_flag = True

    prompt = sys.argv[1]

    messages = [
        types.Content(role="user",parts=[types.Part(text=prompt)])
    ]

    available_functions  = types.Tool(
        function_declarations =[

            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file
        ]
    )

    config = types.GenerateContentConfig(
        tools = [available_functions],
        system_instruction= system_prompt,
    )



    max_iters = 20 

    for i in range(0, max_iters):

        response = client.models.generate_content(
            model="gemini-2.0-flash-001", contents=messages, config= config 
        )



        if response is None or response.usage_metadata is None:
            print("response is malformed.")
            return
        

        
        if verbose_flag:
            print(f"user prompt:{prompt}")
            print(f"Prompt Tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Generation Tokens: {response.usage_metadata.candidates_token_count}")
    


        if response.candidates:
            for candidate in response.candidates:
                if candidate is None or candidate.content is None:
                    continue 
                messages.append(candidate.content)
    
        if response.function_calls:
            for function_call_part in response.function_calls:
                # print(f"calling function: {function_call_part.name} ({function_call_part})") 
                result = call_function(function_call_part,verbose_flag)
                messages.append(result)
                print("Function Call Result:", result)

        else:
            print("Response:", response.text)
            return


main()

# print(get_files_info("calculator","pkg"))