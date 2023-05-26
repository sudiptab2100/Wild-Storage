from lib import ZipModule, Bitify, FrameGenerator, FrameVideo, time, settings


file_dir = "TestUse/test/"

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
z.zip(OPz, file_dir, op_dir)
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
