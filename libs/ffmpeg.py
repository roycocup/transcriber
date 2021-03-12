import os
import subprocess
import re
import shutil

class Ffmpeg():
    
    def format(self, file_name, format):
        new_file_name = f"{file_name}.{format}"
        os.system(f"ffmpeg -y-i {file_name} {new_file_name}")
        return new_file_name
    
    def probe_channels(self, file_name):
        out = subprocess.Popen(["ffprobe", "-i", file_name, "-show_entries", "stream=channels"],
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT)
        stdout,stderr = out.communicate()
        res = re.findall(r'\[STREAM\][a-z\=\\n]*(\d)+', str(stdout))
        if res: 
            return res[0]
        else:
            raise Exception("Unable to find channels")
    
    def change_channels(self, file_name, audio_channels):
        tmp_file_name = f"tmp-{file_name}"
        subprocess.call(["ffmpeg", "-y","-i",file_name,"-ac",audio_channels, tmp_file_name])
        os.remove(file_name)
        shutil.move(src=tmp_file_name, dst=file_name)
    

