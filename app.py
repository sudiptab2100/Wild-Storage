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

def encode_to_video(settings):
    ip_dir = settings['ip_files']
    op_dir = settings['op_generated']
    height = settings['height']
    width = settings['width']
    exp = settings['expansion_factor']
    OPz = settings['zip_name']

    z = ZipModule()
    b = Bitify()
    f = FrameGenerator(height, width, exp)
    v = FrameVideo()

    tic = time.perf_counter()
    z.zip(OPz, ip_dir, op_dir)
    toc = time.perf_counter()
    print(f"zip done: {toc - tic:0.4f} seconds")

    tic = time.perf_counter()
    fbits = b.fileToBits(f'{op_dir}{OPz}.zip')
    toc = time.perf_counter()
    print(f"bitify done: {toc - tic:0.4f} seconds")

    tic = time.perf_counter()
    img_array = f.storeFrames(fbits, op_dir)
    toc = time.perf_counter()
    print(f"frame generator done: {toc - tic:0.4f} seconds")

    tic = time.perf_counter()
    v.framesToVideo(op_dir, img_array)
    toc = time.perf_counter()
    print(f"frames to video done: {toc - tic:0.4f} seconds")

def decode_from_video(settings):
    pass

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
        encode_to_video(settings)
    elif answer == 'Decode video to file':
        decode_from_video(settings)