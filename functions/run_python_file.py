import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
        target_path = os.path.abspath(os.path.join(working_directory, file_path))
        abs_working_dir = os.path.abspath(working_directory)

        if not target_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(target_path):
            return f'Error: File "{file_path}" not found.'
        
        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        process = subprocess.run(["python", target_path] + args, capture_output=True, cwd=working_directory, timeout=30, text=True)
        
        output = ""
        if process.stdout:
            output += f"STDOUT:\n{process.stdout}"
        if process.stderr:
            output += f"STDERR:\n{process.stderr}"
        if not process.stdout and not process.stderr:
            output = "No output produced."
        if process.returncode != 0:
            output = f"Process exited with code {process.returncode}"
        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file, processes errors and outputs.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path given to reach the python file, if something isn't right (for example the .py at the end), it exits the function",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Arguments passed along to the function, defaultly empty",
            ),
        },
    ),
)