from libs.ffmpeg import Ffmpeg

class Audioformatter:
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def format_to(self, file_type=None):
        Ffmpeg().format(file_name=self.file_name, format=file_type)

    def probe_channels(self):
        return Ffmpeg().probe_channels(self.file_name)
    
    def change_channels(self, num_channels):
        return Ffmpeg().change_channels(self.file_name, num_channels)
