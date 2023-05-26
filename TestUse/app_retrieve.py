from lib import ZipModule, Bitify, FrameGenerator, FrameVideo, time, settings, shutil


file_dir = "TestUse/op/generated/"

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
origin = f'{file_dir}metadata.json'
shutil.copy(origin, op_dir)
toc = time.perf_counter()
print(f"copy metadata done: {toc - tic:0.4f} seconds")

tic = time.perf_counter()
img_arr = v.extractFrames(file_dir)
toc = time.perf_counter()
print(f"video to frames done: {toc - tic:0.4f} seconds")

tic = time.perf_counter()
fbits = f.framesToBits(op_dir, img_arr)
toc = time.perf_counter()
print(f"frames to bits done: {toc - tic:0.4f} seconds")

tic = time.perf_counter()
b.bitsToFile(fbits, f'{op_dir}{OPz}.zip')
toc = time.perf_counter()
print(f"bit to file done: {toc - tic:0.4f} seconds")

tic = time.perf_counter()
z.unzip('TEST', f'{op_dir}{OPz}.zip', op_dir)
toc = time.perf_counter()
print(f"unzip done: {toc - tic:0.4f} seconds")