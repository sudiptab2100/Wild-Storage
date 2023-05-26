# Wild-Storage

### Virtual Environment Set Up

#### Create Virtual Environment

```console
python3 -m venv env
```

#### Activate Virtual Environment

```console
source env/bin/activate
```

#### Install Required Packages

```console
pip install -r requirements.txt
```


### Compile C++ Library & Generate Python Bindings

```console
g++ -fPIC -shared DataProccessing/cLibs/helper.cpp -o DataProccessing/cLibs/c_lib.so
```


### DataProcessing Working

#### Embed File Into Video
<img src="https://ipfs.io/ipfs/QmPu9dK4EZPwoBkQGRzcggkXzyXUQy7bWQGWWtP6HiPVbb">

#### Retrieve File From Video

<img src="https://ipfs.io/ipfs/QmVqEF5QpY6ywYRw9XUHJCv13VtLJ42e3JVH8XYr9adWRm">
<!-- ![Embed To Video](https://ipfs.io/ipfs/QmPu9dK4EZPwoBkQGRzcggkXzyXUQy7bWQGWWtP6HiPVbb=1920x1280)  -->
