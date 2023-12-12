import os
import re
import subprocess


def first_run():
    command = 'powershell -Command "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString(\'https://chocolatey.org/install.ps1\'))"'
    subprocess.run(command, shell=True)
    command = '''choco install googlechrome --version 119.0.6045.160 -y
    choco install git --version 2.43.0 -y
    choco install vscode --version 1.85.0 -y
    choco install gsudo --version 2.4.0 -y
    choco install steam --version 2.10.91.91221129 -y
    choco install geforce-game-ready-driver --version 546.29 -y
    choco install vcredist140 --version 14.38.33130 -y
    choco install 7zip --version 23.1.0 -y
    choco install dotnet3.5 --version 3.5.20160716 -y
    choco install microsoft-windows-terminal --version 1.18.3181 -y
    choco install qbittorrent -y
    choco install powertoys -y
    choco install epicgameslauncher -y
    choco install goggalaxy -y
    choco install stremio -y
    '''
    subprocess.run(command, shell=True)


def print_help():
    print("Comandos: sleep X, abort, exit, activate\n")


run = True


def sleep(arg):
    ms = (int(arg) * 60)
    command = f'cmd /c "shutdown -s -t {ms}"'
    os.system(command)
    print(f'Computer will sleep in {arg} minutes.')
    return


def abort_sleep():
    os.system('cmd /c "shutdown -a"')
    print('Sleep timer canceled')


def activate():
    install_command = 'powershell -Command "irm https://massgrave.dev/get | iex"'
    subprocess.run(install_command, shell=True)


def terminate():
    run = False
    command = "exit"
    os.system(command)


def download_video(arg):
    a = str(arg).split()
    command = f"""yt-dlp {a[1]}"""
    os.system(command)
    print('Vídeo baixado.')


while run == True:
    i = input(">")

    if i.startswith("sleep"):
        t = re.findall(r'\d+', i)
        sleep(t[0])
    elif i.startswith("abort"):
        abort_sleep()
    elif i.startswith("help"):
        print_help()
    elif i.startswith("yt"):
        download_video(i)
    elif i.startswith("exit"):
        terminate()
        break
    elif i.startswith("first_run"):
        first_run()
    elif i.startswith("secret"):
        activate()
    else:
        run = False
        break
