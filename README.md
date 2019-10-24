# big-fiubrother-display
Big Fiubrother Display Application

### Prerequisites

- python3

### Install

In order to install big-fiubrother-display, a virtual environment is recommended. This can be achieved executing:

```
python3 -m venv big-fiubrother-display-venv
source big-fiubrother-display-venv/bin/activate
```

To install all the dependencies, execute the following command: 

```
python3 -m pip install -r requirements.txt
```

### Configuration

Before running, proper configuration should be considered. Inside the folder *config/* create a yaml file with the desired settings. By default, the application will try to load *config/development.yml*.

### Run

```
./run.py 
```
