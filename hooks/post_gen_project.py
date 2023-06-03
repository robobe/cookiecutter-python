import subprocess

subprocess.call(['python', '-m', 'venv', 'venv'])

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])