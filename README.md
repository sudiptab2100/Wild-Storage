# Wild-Storage

Wild-Storage lets you use YouTube as a Infinite Cloud Storage. It embeds any files(Images, Videos, Documents, etc) into a video. The video can be uploaded to YouTube and the file can be retrieved from the video. A exapansion & compression technique is used to defeat YouTube's compression algorithm. The file can be retrieved from the video without any loss of data.

This project is inspired by [Infinite-Storage-Glitch](https://github.com/DvorakDwarf/Infinite-Storage-Glitch) which is a Rust implementation.

## Virtual Environment Set Up

### Create Virtual Environment

```console
python3 -m venv env
```

### Activate Virtual Environment

```console
source env/bin/activate
```

### Install Required Packages

```console
pip install -r requirements.txt
```

## Compile C++ Library & Generate Python Bindings

```console
g++ -fPIC -shared DataProccessing/cLibs/helper.cpp -o DataProccessing/cLibs/c_lib.so
```

## DataProcessing Working

### Embed File Into Video
<img src="https://ipfs.io/ipfs/QmPu9dK4EZPwoBkQGRzcggkXzyXUQy7bWQGWWtP6HiPVbb">

### Retrieve File From Video

<img src="https://ipfs.io/ipfs/QmVqEF5QpY6ywYRw9XUHJCv13VtLJ42e3JVH8XYr9adWRm">

## Expansion And Compression

<img src="https://ipfs.io/ipfs/Qma8CRjSV7Azkp3uMfda1aWDNHGNQgy1haC6fcuuWHMJ8Y">

## Python Wrapped C++ Library

Wild-Storage was a complete Python Implementation. Beign a very slow interpreted language it was taking too much time to process files. Later I moved some heavy task codebase to C++ and wrapped those in Python using [ctypes](https://docs.python.org/3/library/ctypes.html). This helped to process the files ~3x faster.
