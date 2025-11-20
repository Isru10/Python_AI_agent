import os 
import subprocess
from google.genai import types

def run_python_file(working_directory:str, file_path:str,args = []):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: "{file_path}" is not in the working dir'
    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" is not a file'

    if not file_path.endswith(".py"):
        return f'Error : "{file_path}" is not a python file'
    
    try:

        final_args = ["python",file_path]
        final_args.extend(args)
        output = subprocess.run(final_args, cwd=abs_working_dir, timeout=30, capture_output=True)
        final_string =  f"""  
    STDOUT:{output.stdout}
    STDERR:{output.stderr}
"""
        

        if output.stdout =="" and output.stderr =="" :
            final_string = f' no output produced.\n'

        if output.returncode!=0:
            final_string+= f'Error: Python file "{file_path}" exited with code {output.returncode}'
        return final_string
    except Exception as e:
        return f'Error executing python file : {e}'
    




schema_run_python_file = types.FunctionDeclaration(
    name = "run_python_file",
    description = "runs a python file with python 3 interpreter. accepts additional cli args as an optional array working directory.",
    parameters  = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "directory": types.Schema(
                type  = types.Type.STRING,
                description = "the file to run within the working directory. ",

            ),


              "args": types.Schema(
                type  = types.Type.ARRAY,
                description = "an optional array of string to be used as cli args when running the python file. ",
                items = types.Schema(
                    type = types.Type.STRING
                )

            )
        }
    )
)