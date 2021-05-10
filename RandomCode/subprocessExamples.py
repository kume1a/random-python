import subprocess

a = subprocess.run("dir /L", shell=True, stdout=subprocess.PIPE, 
                   stderr=subprocess.PIPE, text=True)
# print(a.stdout)
# print(a.returncode)
# print(a.stderr)

# with open("command.txt", "w") as file:
#     subprocess.run("dir /L", shell=True, stdout=file, text=True)