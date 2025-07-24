import os
from .config import MAX_CHARS

def get_files_info(working_directory, directory="."):

    try:

        target_path = os.path.abspath(os.path.join(working_directory, directory))
        abs_working_dir = os.path.abspath(working_directory)



        if not target_path.startswith(abs_working_dir):
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

        if not os.path.isdir(target_path):
            return (f'Error: "{directory}" is not a directory')
        
        file_list = os.listdir(target_path)
        files_info = []
        for file in file_list:
            info = f"- {file}: file_size={os.path.getsize(os.path.join(target_path, file))} bytes, is_dir={os.path.isdir(os.path.join(target_path, file))}"
            files_info.append(info)
        return "\n".join(files_info)
    
    except Exception as e:
        return f"Error: {e}"