import subprocess

def run_command(command):
    subprocess.run(["sh", "-c", command])

def task():
    run_command("black && isort")
