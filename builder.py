import shutil
import os
import sys
import subprocess
import time
from typing import Dict, List

templates = {
    'README.txt': 'README.md',
    'setup.txt': 'setup.py',
    'install.txt': 'install.bat'
}

params = {}

def clean_old_dist():
    try:
        shutil.rmtree('./dist', ignore_errors=True)
    except FileNotFoundError as e:
        pass

def get_local(directory:str):
    return os.path.join(os.path.dirname(__file__), directory)

def create_from_template(source:str, target:str, params:Dict[str, str]):
    data = ''
    with open(get_local(os.path.join('templates', source)), 'r', encoding = 'latin1') as r:
        data = r.read()
    for k in params:
        data = data.replace(f"[{k}]", params[k])
    with open(get_local(target), 'w', encoding = 'latin1') as r:
         r.write(data)

def get_version(versionFile:str = 'version.txt') -> List[int]:
    result:List[int] = [0, 0, 0]
    try:
        with open(versionFile, 'r', encoding='latin1') as f:
            result = [int(i) for i in f.read().split('.')]
    except:
        pass
    return result

def set_version(versionFile:str = 'version.txt', versionData: List[int] = None):
    version = '.'.join([str(i) for i in (versionData or [0, 0, 0])])
    with open(versionFile, 'w', encoding='latin1') as f:
        f.write(version)

def load_version(versionFile:str = 'version.txt'):
    versionData = get_version(versionFile)
    params['version'] = '.'.join([str(i) for i in (versionData or [0, 0, 0])])

def increment_version(versionFile:str = 'version.txt'):
    versionData:List[int] = get_version(versionFile)
    versionData[2]+=1
    set_version(versionFile, versionData)    
    version = '.'.join([str(i) for i in (versionData or [0, 0, 0])])
    print(f'Version set to : {version}')
    params["version"] = version

def generate_files():
    for t in templates:
        print(f'\tGenerating {templates[t]} from {t}')
        create_from_template(t, templates[t], params)

def list_availables():
    for i in actions:
        print(f'\t{i}')

def build():
    res = 0
    if os.name == 'nt':
        res = os.system('py -m build') 
    elif os.name == 'posix':
        res = os.system('python3 -m build')
    if res != 0:
        exit(res)

def pip(command:str):
    pipCommand = ''
    if os.name == 'nt':
        pipCommand = 'pip'
    elif os.name == 'posix':
        pipCommand = 'pip3'
    return os.system(f'{pipCommand} {command}')

def uninstall():
    return pip('uninstall -y threadsnake')

def install(src:str = 'dist'):
    uninstall()
    wheel = [i for i in os.listdir(src) if i.endswith('.whl')][0]
    print(wheel)
    return pip(f'install {src}/{wheel} --no-cache-dir')


def test():
    p = subprocess.Popen([sys.executable, 'test-server.py'], cwd='./test/', shell=False)
    p.wait(1000)
    #p = subprocess.call([sys.executable, 'test-server.py'], cwd = './test/', shell=True)
    #command = f'{py} test/test-server.py {testPort}'

actions = {
    "BUILD": build,
    "INCREMENT_VERSION": increment_version,
    "LOAD_VERSION": load_version,
    "CLEAN_DIST": clean_old_dist,
    "GENERATE_FILES": generate_files,
    "HELP": list_availables,
    "TEST": test,
    "INSTALL": install,
    "UNINSTALL": uninstall
}

actionsQueue = []

for i in sys.argv:
    if i in actions:
        actionsQueue.insert(0, (i, actions[i]))
        
while len(actionsQueue) > 0:
    i = actionsQueue.pop()
    print(f'TASK BEGIN: {i[0]}')
    i[1]()
    print(f'TASK END: {i[0]}')