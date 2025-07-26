import os
from .config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:

        target_path = os.path.abspath(os.path.join(working_directory, file_path))
        abs_working_dir = os.path.abspath(working_directory)

        if not target_path.startswith(abs_working_dir):
            return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        
        if not os.path.isfile(target_path):
            return (f'Error: File not found or is not a regular file: "{file_path}"')



        with open(target_path) as f:
            file_contents = f.read(MAX_CHARS)
            if len(f.read()) > MAX_CHARS:
                return f'{file_contents} [...File "{file_path}" truncated at 10000 characters]'
            return file_contents

    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of the given file found in the file_path, the content will cut out after reaching 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read the file from, relative to the working directory. If not provided, does not read anything, instead gives an error.",
            ),
        },
    ),
)