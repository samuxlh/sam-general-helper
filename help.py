import os
import re

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
    command = "irm https://massgrave.dev/get | iex"
    os.system(command)

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
    elif i.startswith("secret"):
        activate()
    else:
        run = False
        break

