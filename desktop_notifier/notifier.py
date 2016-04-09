import subprocess

def notification(message):
	subprocess.Popen(['notify-send', message])
	return

notification("Hello World")