from DataProccessing.zip_module import ZipModule
from DataProccessing.bitify import Bitify
from DataProccessing.frame_generator import FrameGenerator
from DataProccessing.video import FrameVideo
import time
import shutil
import json
from PyInquirer import prompt
import os
from pytube import YouTube
from pytube.cli import on_progress


def create_dir(settings):
    if not os.path.exists(settings['data_dir']):
        os.mkdir(settings['data_dir'])
        os.mkdir(settings['ip_files'])
        os.mkdir(settings['op_generated'])
        os.mkdir(settings['op_retrieved'])
        os.mkdir(settings['download_dir'])

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
    download_dir = settings['download_dir']
    op_dir = settings['op_retrieved']
    height = settings['height']
    width = settings['width']
    exp = settings['expansion_factor']
    OPz = settings['zip_name']
    
    z = ZipModule()
    b = Bitify()
    f = FrameGenerator(height, width, exp)
    v = FrameVideo()
    
    tic = time.perf_counter()
    img_arr = v.extractFrames(download_dir)
    toc = time.perf_counter()
    print(f"video to frames done: {toc - tic:0.4f} seconds")
    
    tic = time.perf_counter()
    fbits = f.framesToBits(download_dir, img_arr)
    toc = time.perf_counter()
    print(f"frames to bits done: {toc - tic:0.4f} seconds")
    
    tic = time.perf_counter()
    b.bitsToFile(fbits, f'{op_dir}{OPz}.zip')
    toc = time.perf_counter()
    print(f"bit to file done: {toc - tic:0.4f} seconds")
    
    tic = time.perf_counter()
    z.unzip('Files', f'{op_dir}{OPz}.zip', op_dir)
    toc = time.perf_counter()
    print(f"unzip done: {toc - tic:0.4f} seconds")

def download_and_decode_video(url, settings):
    yt_obj = YouTube(url, on_progress_callback=on_progress)
    yt_stream = yt_obj.streams.get_highest_resolution()
    yt_desc = yt_obj.description
    try:
        print('Downloading...')
        tic = time.perf_counter()
        yt_stream.download(filename='op.mp4', output_path=settings['download_dir'])
        toc = time.perf_counter()
        print()
        print(f"downloading done: {toc - tic:0.4f} seconds")
        with open(f'{settings["download_dir"]}metadata.json', 'w') as f:
            f.write(yt_desc)
        decode_from_video(settings)
    except:
        print('An error has occurred')

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
        yt_url = input('Enter the YouTube video URL: ')
        download_and_decode_video(yt_url, settings)