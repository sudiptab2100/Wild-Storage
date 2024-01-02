from DataProccessing.zip_module import ZipModule
from DataProccessing.bitify import Bitify
from DataProccessing.frame_generator import FrameGenerator
from DataProccessing.video import FrameVideo
import time
import shutil
import json
from PyInquirer import prompt


settings = json.load(open('settings.json'))

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
while True:
    answer = prompt(questions)['operation']
    print(answer)
    if answer == 'Exit':
        break