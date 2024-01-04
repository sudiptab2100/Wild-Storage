from DataProccessing.zip_module import ZipModule
from DataProccessing.bitify import Bitify
from DataProccessing.frame_generator import FrameGenerator
from DataProccessing.video import FrameVideo
import time
import shutil
import json
from PyInquirer import prompt
import os


def create_dir(settings):
    if not os.path.exists(settings['data_dir']):
        os.mkdir(settings['data_dir'])
        os.mkdir(settings['ip_files'])
        os.mkdir(settings['op_generated'])
        os.mkdir(settings['op_retrieved'])

def delete_dir(settings):
    if os.path.exists(settings['data_dir']):
        shutil.rmtree(settings['data_dir'])

questions = [
    {
        'type': 'rawlist',
        'name': 'operation',
        'message': 'Choose operation:',
        'choices': [
            'Encode file to video',
            'Decode video to file',
            'Clean',
            'Exit'
        ]
    }
]
cleaning_confirmation = [
    {
        'type': 'confirm',
        'name': 'confirm',
        'message': 'Do you want to continue cleaning?'
    }
]

while True:
    settings = json.load(open('settings.json'))
    answer = prompt(questions)['operation']
    if answer == 'Exit':
        break
    elif answer == 'Clean':
        confirmation = prompt(cleaning_confirmation)['confirm']
        if confirmation:
            print('Cleaning...')
            delete_dir(settings)
            create_dir(settings)
            print('Done!')
    elif answer == 'Encode file to video':
        pass
    elif answer == 'Decode video to file':
        pass