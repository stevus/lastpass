# lastpass

Since the Lastpass UI is very difficult to navigate, I found a python lastpass
wrapper and extended it's example to print out all accounts along with info.

## Python Environment Usage / Using VirtualEnv

### Installing VirturalEnv

If it is not already installed, install it using the following command(s):

```
sudo pip install virtualenv
```

### Create Virtual Environment

```
virtualenv -p /usr/bin/python3 venv
```

### Entering the VirtualEnv

```
source venv/bin/activate
```

### Exiting the VirtualEnv

```
deactivate
```

### Creating / Installing Requirements.txt

```
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
```
