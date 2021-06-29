# [ismslib](https://pypi.org/project/ismslib/)
#### Very simple and easy to use Python 3 library for integrating SSLWireless SMS API.


## Installation
#### using virtual environment (pipenv)
```shell script
pipenv install ismslib
```
#### using pip globally
```shell script
python3 -m pip install ismslib
```


## Example
```python
from ismslib import ISMS

# Contact with SSLWireless Key Account Manager for these credentials
config = {
    "username": '<user>',
    "password": '<pass>',
    "sid": '<SID>',
}

response = ISMS.set_config(config)\
                .set_body("আসসালামু আলাইকুম").make_unicode()\
                .set_recipient(['88018XXXXXXXX', '88019XXXXXXXX'])\
                .send()

print(response) if response['error'] else print('success')

```


## Usage
### 1. First we import the library
```python
 from ismslib import ISMS
```
### 2. Set Credentials
Create a dictionary with user credentials obtained from SSLWireless.
```python
config = {
    "username": '',  # Please add your username provided by SSLWireless
    "password": '',  # Please add your password provided by SSLWireless
    "sid": '',  # Please add your SID provided by SSLWireless
}
```
### 3. Set data
##### Call needed methods with valid data
```python
ISMS.set_config(config) # Set config values
ISMS.set_body("আসসালামু আলাইকুম") #Set SMS body text, Can be English or Unicode Bangla
ISMS.make_unicode() # Use for Bangla SMS, otherwise is not needed
ISMS.set_recipient(['88018XXXXXXXX', '88019XXXXXXXX']) # list of mobile numbers to send to
ISMS.set_debug(True) # __DO NOT USE IN PRODUCTION__. Prints useful information on console.
response = ISMS.send() # Finally send SMS.
```

##### optionally, methods can be chained together 
```python
response = ISMS.set_config(config)\
                .set_body("আসসালামু আলাইকুম").make_unicode()\
                .set_recipient(['88018XXXXXXXX', '88019XXXXXXXX'])\
                .set_debug()\
                .send()
```

### 4. Check the returned response
We can print out the response in console
```python
print(response) if response['error'] else print('success')
```


## Return values
##### "send()" returns a dictionary containing 3 values
```python
{'error': True, 'msg': 'Login FAILED. Please check your username and password.', 'json': '{"REPLY": {"PARAMETER": "OK", "LOGIN": "FAIL"}}'}
```
##### 1. error [boolean] : False if SMS sent successfully, True on error
##### 2. msg [string] : Error message. Explains the reason of failure.
##### 3. json [json string] : Raw API response, it's there if needed.

## Contribution
> Star ⭐ this repo if you find it useful. Any feedback is much appreciated. For official support / user credentials, contact your Key Account Manager (KAM). 
