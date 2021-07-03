from ismslib import ISMS
import pytest


def test_set_config():
    config = {
        "username": '<user>',
        "password": '<pass>',
        "sid": '<SID>',
    }

    ISMS.set_config(config)
    assert ISMS.username == "<user>"
    assert ISMS.password == "<pass>"
    assert ISMS.sid == "<SID>"


def test_set_body():
    ISMS.set_body('Test SMS')

    assert ISMS.body == 'Test SMS'


def test_make_unicode():
    ISMS.set_body('Test SMS')
    ISMS.make_unicode()

    assert ISMS.body == b'005400650073007400200053004D0053'


def test_set_recipient():
    ISMS.set_recipient('88018XXXXXXXX')

    assert ISMS.recipient == '88018XXXXXXXX'


def test_set_debug():
    ISMS.set_debug(True)

    assert ISMS.debug


def test_send():
    config = {
        "username": '<user>',
        "password": '<pass>',
        "sid": '<SID>',
    }

    response = ISMS.set_config(config)\
        .set_body("আসসালামু আলাইকুম").make_unicode()\
        .set_recipient(['88018XXXXXXXX', '88019XXXXXXXX'])\
        .send()

    assert response['json'] != ''
