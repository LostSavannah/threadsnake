import os
import sys
from typing import Dict, List


templates = {
    'README.txt': 'README.md',
    'setup.txt': 'setup.py',
    'install.txt': 'install.bat'
}

params = {}

def clean_old_dist():
    try:
        os.rmdir('./dist')
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

actions = {
    "INCREMENT_VERSION": increment_version,
    "CLEAN_DIST": clean_old_dist,
    "GENERATE_FILES": generate_files,
    "HELP": list_availables
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