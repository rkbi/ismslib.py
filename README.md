# ismslib
A very simple and easy to use Python 3 library for integrating SSLWireless SMS API.


## Installation
```shell script
python3 -m pip install ismslib
```


## Example
```python
from ismslib import ISMS

config = {
    "username": '<user>',
    "password": '<pass>',
    "sid": '<SID>',
}

response = ISMS.config(config)\
                .body("আসসালামু আলাইকুম").bn()\
                .recipient(['88018XXXXXXXX', '88019XXXXXXXX'])\
                .send()
```


## Usage
### 1. First we import the library
```python
 from ismslib import ISMS
```
### 2. Set Credentials
Create a dictionary with user credentials obtained from SSLWireless. It can optionally set in a separate config.py file and imported here.
```python
config = {
    "username": '',  # Please add your username provided by SSLWireless
    "password": '',  # Please add your password provided by SSLWireless
    "sid": '',  # Please add your SID provided by SSLWireless
}
```
### 3. Set data
##### Call needed methods with appropriate data
```python
ISMS.config(config) # Set config values
ISMS.body("আসসালামু আলাইকুম") #Set SMS body text, Can be English or Unicode Bangla
ISMS.bn() # Call only if the body text is in Bangla, otherwise omit
ISMS.recipient(['88018XXXXXXXX', '88019XXXXXXXX']) # can be a single valid mobile number as string or multiple numbers as an string array
ISMS.debug() # Prints useful information on console. Only useful when debugging, DO NOT USE IN PRODUCTION
response = ISMS.send() # Finally send SMS.
```

##### Methods can be chained together optionally
```python
response = ISMS.config(config)\
                .body("আসসালামু আলাইকুম").bn()\
                .recipient(['88018XXXXXXXX', '88019XXXXXXXX'])\
                .debug()\
                .send()
```

### 4. Check the returned response
##### We can print out the response in console for fun or use otherwise for profit
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
