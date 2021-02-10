from ffmpeg import FFmpeg

class Audioformatter:
    
    def __init__(self, file_name):
        self.file_name = file_name
    
    def format(self, file_type=None):
        result = FFmpeg().option('y').input(self.file_name).output(f'output.{file_type}')
        print(result)
