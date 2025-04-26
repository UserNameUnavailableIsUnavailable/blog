import tarfile
import os
import shutil
import paramiko

project_dir = os.path.dirname(os.path.abspath(__file__))

with tarfile.open(os.path.join(project_dir, "blog.tar.gz"), "w:gz", dereference=False) as tar:
    for root, _, files in os.walk(os.path.join(project_dir, "blog")):
        rel = os.path.relpath(root, project_dir)
        for file in files:
            fullname = os.path.join(root, file)
            arcname = os.path.join(rel, file).replace("\\", "/")
            if os.path.islink(fullname):
                target = os.readlink(fullname).replace("\\", "/")
                tar_info = tarfile.TarInfo(name=arcname)
                tar_info.type = tarfile.SYMTYPE
                tar_info.linkname = target
                tar.addfile(tar_info)
            else:
                tar.add(fullname, arcname=arcname)
    # tar.add(os.path.join(project_dir, "blog"), arcname="blog", recursive=True)

host_name = "blog.macrohard.fun"
user_name = "ubuntu"
home_dir = ""

if (os.name == "nt"):
    home_dir = os.environ["USERPROFILE"]
else:
    home_dir = os.environ["HOME"]

ssh_key_path = os.path.join(home_dir, ".ssh", "id_rsa")

private_key = paramiko.RSAKey.from_private_key_file(ssh_key_path)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host_name, username=user_name, pkey=private_key)
sftp = client.open_sftp()
sftp.put(os.path.join(project_dir, "blog.tar.gz"), "/tmp/blog.tar.gz")
sftp.close()
client.close()