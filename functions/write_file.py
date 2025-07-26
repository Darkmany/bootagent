import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        target_path = os.path.abspath(os.path.join(working_directory, file_path))
        abs_working_dir = os.path.abspath(working_directory)



        if not target_path.startswith(abs_working_dir):
            return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

        with open(target_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites the contents of the file at the file_path with the content passed to the function",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path given to reach the file.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content given to overwrite the current content of the file",
            ),
        },
    ),
)