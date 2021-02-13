import os

class Ffmpeg():
    
    def format(self, file_name, format):
        new_file_name = f"{file_name}.{format}"
        os.system(f"ffmpeg -i {file_name} {new_file_name}")
        return new_file_name

