#!/usr/bin/python

######
# THIS FILE IS ONLY AN EXAMPLE. PLEASE MODIFY AS REQUIRED.
# Contributor: Md. Rakibul Islam <rakibul.islam@sslwireless.com>
######

import ismslib

# Sending with GET API
response = ismslib.sendSMSWithGet('8801234567890', 'Test SMS With GET')
print(response)

# Sending with POST API
response = ismslib.sendSMSWithPost('8801234567890', 'Test SMS With POST')
print(response)
