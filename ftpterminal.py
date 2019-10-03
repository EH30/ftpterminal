import ftplib
import sys
import os, re


current_dir = "/>"

def check_system():
    if sys.platform == "linux" or sys.platform == "linux2":
        os.system("clear")
        return "linux"
    elif sys.platform == "win32":
        os.system("cls")
        return "win32"

check_system()

ftpserver = str(input("FTP Hostname: "))
username = str(input("Username: "))
pwd = str(input("Password: "))

def cd(dir):
    return ftp.cwd(dir) 


def upload(filename):
    
    opnr = open(filename, "rb")
    ftp.storbinary("STOR ehfile.txt", opnr)


def filedownload(namefile):

    filename = namefile

    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

    ftp.quit()
    localfile.close()



def start():    
    global username, pwd, ftpserver, ftp, current_dir
    
    ftp = ftplib.FTP(ftpserver)
    ftp.login(username, pwd)
    check_system()
    pattern_cd = r"cd"
    pattern_upload = r"upload"
    pattern_download = r"download"

    while True:
        user_input = str(input(current_dir)) 


        if re.search(pattern_cd, user_input):
            directory_current = cd(user_input.strip("cd "))
            current_dir = directory_current.lstrip("'250 OK. Current directory is ") + "/>"
        elif user_input == "ls":
            ftp.retrlines("LIST")
        elif re.search(pattern_upload, user_input):
            upload(user_input.strip("upload "))
        elif user_input == "clear":
            check_system()
        elif re.search(pattern_download, user_input):
            filedownload(user_input.strip("download "))
        else:
            print("ERROR")


#ftp.cwd("htdocs")
#ftp.retrlines("LIST")

if __name__ == "__main__":
    start()
