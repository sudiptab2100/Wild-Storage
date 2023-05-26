import sys
sys.path.insert(0, 'DataProccessing')

from zip_module import ZipModule
from bitify import Bitify
from frame_generator import FrameGenerator
from video import FrameVideo
import time
import shutil
import json
settings = json.load(open('TestUse/settings.json'))