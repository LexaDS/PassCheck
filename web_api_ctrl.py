from home_dir.webapictrl.Gyt import G
from subprocess import *
import time
import shutil
import os
import stat
# we will be cloning the repo
G.git_clone()

# we have attributed the path that we wil generally work with to a variable
x='C:\\Users\\Alexandra\\PycharmProjects\\projects\\home_dir\\webapictrl\\MyAPI'

# we are running the api.py script
Popen('python {}\\api.py'.format(x))
time.sleep(3)
# we are running the klient.py script
Popen('python {}\\klient.py'.format(x))
time.sleep(3)
# we are terminating api.py
Popen('python {}api.py'.format(x)).terminate()
shutil.rmtree(x,ignore_errors=True)

# we are deleting the cloned repo using shutil lib
dir = x
def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)
for i in os.listdir(dir):
    if i.endswith('git'):
        tmp = os.path.join(dir, i)
        while True:
            call(['attrib', '-H', tmp])
            break
        shutil.rmtree(tmp, onerror=on_rm_error)






