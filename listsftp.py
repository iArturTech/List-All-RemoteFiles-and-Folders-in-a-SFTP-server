import paramiko
import stat

def list_remote_files(ftp, path=".", indent=0):
    files = ftp.listdir_attr(path)
    for file_attr in files:
        full_path = path + "/" + file_attr.filename if path != "." else file_attr.filename
        if stat.S_ISDIR(file_attr.st_mode):
            print("  " * indent + "Directory: " + full_path)
            list_remote_files(ftp, full_path, indent + 1)
        else:
            print("  " * indent + "File: " + full_path)

ssh_client = paramiko.SSHClient()


# remote server credentials
host = "HostName"
username = "username"
password = "passwordsftp"
port = 22 #add the port if not 22

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host, port=port, username=username, password=password)

ftp = ssh_client.open_sftp()

try:
    list_remote_files(ftp)
finally:
    ftp.close()
    ssh_client.close()
