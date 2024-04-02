from DataProccessing.zip_module import ZipModule
from DataProccessing.bitify import Bitify
from DataProccessing.frame_generator import FrameGenerator
from DataProccessing.video import FrameVideo
import time
import json
import os
from pytube import YouTube
from pytube.cli import on_progress
from art import *
import os


def create_dir(settings):
    if not os.path.exists(settings['data_dir']):
        os.mkdir(settings['data_dir'])
        os.mkdir(settings['ip_files'])
        os.mkdir(settings['op_generated'])
        os.mkdir(settings['op_retrieved'])
        os.mkdir(settings['download_dir'])

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


settings = json.load(open('settings.json'))
create_dir(settings)
yt_url = input('Enter the YouTube video URL: ')
if yt_url != '': download_and_decode_video(yt_url, settings)
else: decode_from_video(settings)