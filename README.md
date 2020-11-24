# Usage

1. Set ```username```, ```password``` and ```sid``` values in ```config.py``` file
2. In your sender script, add ```import ismslib```
3. Use ```ismslib.sendSMSWithGet``` or ```ismslib.sendSMSWithPost``` to send sms

# Example
```python
import ismslib

# Sending with GET API
ismslib.sendSMSWithGet('8801234567890', 'Test SMS With GET')

# Sending with POST API
ismslib.sendSMSWithPost('8801234567890', 'Test SMS With POST')
```