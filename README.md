# Wild-Storage

Wild-Storage lets you use YouTube as a Infinite Cloud Storage. It embeds any files(Images, Videos, Documents, etc) into a video. The video can be uploaded to YouTube and the file can be retrieved from the video. A expansion & compression technique is used to defeat YouTube's compression algorithm. The file can be retrieved from the video without any loss of data.

## Demo Video ([YouTube Link](https://youtu.be/NbeWh011qjs))

![ezgif com-gif-maker](https://gateway.pinata.cloud/ipfs/Qmdo9ZW5uk6NDYWj8K6oNBABDNtBYZZagAxF9UmoxUQFwM)

## <del>Virtual Environment Set Up</del> ❌ (... Not Required Now)

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

## <del>Compile C++ Library & Generate Python Bindings</del> ❌ (... Not Required Now)

```console
g++ -fPIC -shared DataProccessing/cLibs/helper.cpp -o DataProccessing/cLibs/c_lib.so
```

## Wild-Storage CLI App ✅

### Make the script executable

```console
chmod +x cli_app
```

### Run CLI App

Make sure ```GCC``` compiler, ```Python 3```, ```pip```, Python ```venv``` is installed. \
Now open terminal in the project directory and run the following command to complete the necessary setup and run the app.

```console
./cli_app
```

<img src="https://tomato-semantic-alligator-932.mypinata.cloud/ipfs/QmQdnLR9RmjFDLxb39VpqC8N5se9wbhPBRaLsd65uALVBD?_gl=1*1jcg77v*_ga*MjA2MjA3MzczMS4xNzA0NTQzNDQ0*_ga_5RMPXG14TE*MTcwNDU0MzQ0My4xLjEuMTcwNDU0MzU2NC42MC4wLjA.">

## How to Use? ✅

Wait for the app to start.

### Create video from files

- Copy all your files into ```\data\input``` directory
- Select ```Encode file to video``` option on the app
- Wait for the process to complete
- <b>Generated video (```op.mp4```)</b> & <b>Metadata (```metadata.json```)</b> will be available in ```\data\generated``` directory
- Upload the video to <b>YouTube</b> and copy-paste the contents of ```metadata.json``` in <b>description</b> of the video
- Make sure the uploaded video is ```public``` / ```unlisted```

### Retrieve files from video

- Select ```Decode file from video``` option on the app
- Enter the youtube video url (Make sure the uploaded video is ```public``` / ```unlisted```)
- Wait for the process to complete
- The files will be available in ```\data\retrieved``` directory

### Cleaning up

- Select ```Clean``` option on the app to clean data directory

### Exit

- Select ```Exit``` option on the app to exit

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
