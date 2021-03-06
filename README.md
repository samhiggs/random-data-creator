# Gererator of Random Data Sets
The repo is designed to wrap an API around numpy for easy generation of random statistical data
  
## Installation
Create, enter and update your virtual environment (cmd is for Windows powershell)
```
python -m venv rand-data-venv
rand-data-venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```
*note:* if you change the name, update the .gitignore.  

**optional**  
You can prevent `__pycache__` from being created by setting environment variable `PYTHONDONTWRITEBYTECODE=1`  
and restarting your shell or by starting the interpreter with a `-B` flag.
  

## Usage
```
import randomstatsgenerator as rsg

rsg.linear(noise=0, type='int', range=(0,100), step=1) #[0,  1, 2, 3, ... , 99]
```

## Tests
Using unittest framework  
```
python -m unittest #runs all unittests
```
or
```
python -m unittest test.*