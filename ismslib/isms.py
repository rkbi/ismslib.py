import time
import urllib
import requests
import xmltodict
import json
import binascii


class ISMS:
    """
       Send Bulk, Promotional, OTP and Notification SMS through SSLWireless SMS API using a very simple programming interface.
       """

    debug = False
    username = ''
    password = ''
    sid = ''
    body = ''
    recipient = ''
    msisdn = ''
    response = {'error': False, 'msg': '', 'json': ''}

    def set_config(self, c):
        self.username = c['username']
        self.password = c['password']
        self.sid = c['sid']
        return self

    def set_body(self, b):
        self.body = b
        return self

    def make_unicode(self):
        self.body = binascii.hexlify(self.body.encode('utf-16-be')).upper()
        return self

    def set_recipient(self, msisdn):
        self.recipient = msisdn
        return self

    def __get_params(self):
        params = {
            'user': self.username,
            'pass': self.password,
            'sid': self.sid,
            'sms': self.body,
            'msisdn': self.msisdn,
            'csmsid': str(round(time.time() * 1000)),
        }
        urllib.parse.urlencode(params)
        return params

    def __handle_error(self, reply):
        login = reply.get('LOGIN')
        if login == 'FAIL':
            self.response['error'] = True
            self.response['msg'] = 'Login FAILED. Check username and password. Also make sure this server IP is whitelisted at SSLWireless end.'

        parameter = reply.get('PARAMETER')
        if parameter != 'OK':
            self.response['error'] = True
            self.response[
                'msg'] = 'Parameters missing. Please check if all parameters are passing. You can set "<obj>.debug = True" to see all parameters'

        pushapi = reply.get('PUSHAPI')
        if pushapi == 'INACTIVE':
            self.response['error'] = True
            self.response[
                'msg'] = 'Push API is not activated for your user. Please contact with your KAM (Key Account Manager)'

        stakeholder_id = reply.get('STAKEHOLDERID')
        if stakeholder_id == 'INVALID':
            self.response['error'] = True
            self.response['msg'] = 'Invalid Stakeholder ID (SID). Please use the exact SID provided by SSLWireless.'

        permitted = reply.get('PERMITTED')
        if permitted == 'FAIL':
            self.response['error'] = True
            self.response[
                'msg'] = 'Stakeholder not permitted. Please contact with your KAM (Key Account Manager)'

    def __send_with_get(self):
        params = self.__get_params()
        response = requests.get(
            'https://sms.sslwireless.com/pushapi/dynamic/server.php', params=params)
        # TODO: change the variable name of 'r'
        r = xmltodict.parse(response.text)
        self.response['json'] = json.dumps(r)
        self.__handle_error(r.get('REPLY'))

    def set_debug(self, d):
        self.debug = d
        return self

    def send(self):
        print(self.__get_params()) if self.debug else print("")
        if type(self.recipient) is int or type(self.recipient) is str:
            self.msisdn = self.recipient
            self.__send_with_get()
        elif type(self.recipient) is list:
            for msisdn in self.recipient:
                self.msisdn = msisdn
                self.__send_with_get()
        else:
            self.response['error'] = True
            self.response['msg'] = 'Please only pass string or List as recipient'

        return self.response
