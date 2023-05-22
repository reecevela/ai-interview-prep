import subprocess

def record_audio(file_name):
    command = ["ffmpeg", "-y", "-f", "alsa", "-i", "default", file_name]
    subprocess.run(command)