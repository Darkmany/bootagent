import os
from .config import MAX_CHARS

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