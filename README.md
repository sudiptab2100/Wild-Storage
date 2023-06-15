# Wild-Storage

Wild-Storage lets you use YouTube as a Infinite Cloud Storage. It embeds any files(Images, Videos, Documents, etc) into a video. The video can be uploaded to YouTube and the file can be retrieved from the video. A expansion & compression technique is used to defeat YouTube's compression algorithm. The file can be retrieved from the video without any loss of data.

## Demo Video ([YouTube Link](https://youtu.be/NbeWh011qjs))

![ezgif com-gif-maker](https://gateway.pinata.cloud/ipfs/Qmdo9ZW5uk6NDYWj8K6oNBABDNtBYZZagAxF9UmoxUQFwM)

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
<img src="https://tomato-semantic-alligator-932.mypinata.cloud/ipfs/QmNx7xX1pn3ngduQU5n9GKC8NwfH7GRQXfGB4mFuxphtqa">

### Retrieve File From Video

<img src="https://tomato-semantic-alligator-932.mypinata.cloud/ipfs/QmUMXUJZ11mgpp8oEmGPeTenK4669uwJesUVJmK1UDQwvV">

## Expansion And Compression

<img src="https://tomato-semantic-alligator-932.mypinata.cloud/ipfs/Qma8CRjSV7Azkp3uMfda1aWDNHGNQgy1haC6fcuuWHMJ8Y">

## Python Wrapped C++ Library

Wild-Storage was a complete Python Implementation. Beign a very slow interpreted language it was taking too much time to process files. Later I moved some heavy task codebase to C++ and wrapped those in Python using [ctypes](https://docs.python.org/3/library/ctypes.html). This helped to process the files ~3x faster.

## Credits

This project is inspired by [Infinite-Storage-Glitch](https://github.com/DvorakDwarf/Infinite-Storage-Glitch) which is a Rust implementation. I liked the concept and tried to implement in my favourite language Python. The working of both may not be same.
