from DataProccessing.zip_module import ZipModule
from DataProccessing.bitify import Bitify
from DataProccessing.frame_generator import FrameGenerator
from DataProccessing.video import FrameVideo
import time
import shutil
import json
from PyInquirer import prompt, style_from_dict, Token
import os
from pytube import YouTube
from pytube.cli import on_progress
from colorama import init as colorama_init, Fore, Style
from art import *
import os


ENCODE = ' Encode file to video'
DECODE = ' Decode video to file'
CLEAN = ' Clean'
RELOAD_TIME = ' Reload time'
EXIT = ' Exit'

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

qs_style = style_from_dict({
    Token.Text: '#FF9D00',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#f7c602 bold italic underline',
    Token.Pointer: '#FF9D00 bold reverse',
    Token.Answer: '#f7c602 bold',
})
questions = [
    {
        'type': 'list',
        'name': 'operation',
        'message': 'Choose operation:',
        'choices': [
            ENCODE,
            DECODE,
            CLEAN,
            RELOAD_TIME,
            EXIT
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

reload_time = 0
while True:
    # Clear console
    time.sleep(reload_time)
    os.system('cls' if os.name=='nt' else 'clear')
    
    # WILD-STORAGE Header
    t_wild = text2art(f'WILD', font='4max')
    t_storage = text2art(f'STORAGE', font='4max')
    print(f"\n\n{Fore.YELLOW}{t_wild}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{t_storage}{Style.RESET_ALL}\n")
    
    settings = json.load(open('settings.json'))
    create_dir(settings)
    try:
        answer = prompt(questions, style=qs_style)['operation']
        if answer == EXIT:
            break
        elif answer == CLEAN:
            confirmation = prompt(cleaning_confirmation)['confirm']
            if confirmation:
                print('Cleaning...')
                delete_dir(settings)
                create_dir(settings)
                print('Done!')
        elif answer == ENCODE:
            encode_to_video(settings)
        elif answer == DECODE:
            yt_url = input('Enter the YouTube video URL: ')
            download_and_decode_video(yt_url, settings)
        elif answer == RELOAD_TIME:
            reload_time = int(input('Enter the time in seconds: '))
    except:
        pass 