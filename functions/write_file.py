import os
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: "{file_path}" is not in the working dir'

    parent_dir = os.path.dirname(abs_file_path) 
    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f'Error creating parent directories: {parent_dir}'
        


    if not os.path.isfile(abs_file_path):

        pass
        # parent_dir = os.path.dirname(abs_file_path)
        # try:
        #     os.makedirs(parent_dir)
        # except Exception as e:
        #     return f'Error creating parent directories: {parent_dir}'
    try:
        with open(abs_file_path,'w') as f :
            f.write(content) 
        return f'Success: File "{file_path}" written successfully.'
    except Exception as e:
        return f'failed to write to a file : {file_path} , Exception: {e}'
    







schema_write_file = types.FunctionDeclaration(
    name = "write_file",
    description = "overwwrites existing file or writes to a new file if it does not exist and create a required parent dirs safely constrained to the current working directory.  ",
    parameters  = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type  = types.Type.STRING,
                description = "The path to the file to write ",

            ),


            "content": types.Schema(
                type  = types.Type.STRING,
                description = "The content to write to the file as a string",

            )
        }
    )
)