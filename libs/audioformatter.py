from libs.ffmpeg import Ffmpeg

class Audioformatter:
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def format_to(self, file_type=None):
        Ffmpeg().format(file_name=self.file_name, format=file_type)
