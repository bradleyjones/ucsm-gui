import mock
import pytest

from ucsm_gui import command_line


CONFIG = {'RANDOM_NAME': {'hostname': 'host1',
                          'username': 'test',
                          'password': 'password'}}


HOST_DICT = {'username': 'test',
             'password': 'password',
             'hostname': 'host1'}


def test_get_host_from_conf_by_key():
    hostname, hostinfo = command_line._get_host_from_conf(CONFIG,
                                                          'RANDOM_NAME')
    assert hostname == HOST_DICT.get('hostname')
    assert hostinfo == HOST_DICT


def test_get_host_from_conf_by_hostname():
    hostname, hostinfo = command_line._get_host_from_conf(CONFIG, 'host1')
    assert hostname == HOST_DICT.get('hostname')
    assert hostinfo == HOST_DICT


def test_get_host_from_conf_does_not_exist():
    hostname, hostinfo = command_line._get_host_from_conf(CONFIG, 'FAIL')
    assert hostname == 'fail'
    assert hostinfo == {}


def test_get_username_from_dict_valid():
    assert command_line._get_username(HOST_DICT) == HOST_DICT.get('username')


@mock.patch('click.prompt')
def test_get_username_prompt(mock_prompt):
    mock_prompt.return_value = 'testuser'
    assert command_line._get_username({}) == 'testuser'


def test_get_password_from_dict_valid():
    assert command_line._get_password(HOST_DICT) == HOST_DICT.get('password')


@mock.patch('click.prompt')
def test_get_password_prompt(mock_prompt):
    mock_prompt.return_value = 'testpass'
    assert command_line._get_username({}) == 'testpass'
