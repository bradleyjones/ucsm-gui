import mock
import pytest
import socket
import ucsm_gui
import urllib2

from ucsmsdk import ucsexception

@mock.patch('socket.gethostbyaddr')
def test_check_host_reachable(mock_gethost):
    mock_gethost.side_effect = [True, socket.herror, socket.gaierror]
    assert ucsm_gui._check_host_reachable('hostname') == True
    assert ucsm_gui._check_host_reachable('hostname') == False
    assert ucsm_gui._check_host_reachable('hostname') == False


@mock.patch('socket.gethostbyaddr')
def test_launch_exits_on_unreachable_host(mock_gethost):
    mock_gethost.side_effect = [socket.herror]
    with pytest.raises(SystemExit):
        ucsm_gui.launch('hostname', 'user', 'password')


@mock.patch('ucsmsdk.ucshandle.UcsHandle.login')
@mock.patch('socket.gethostbyaddr')
def test_launch_exits_on_exceptions_from_ucsmsdk_login(mock_gethost,
                                                       mock_login):
    mock_gethost.return_value = True
    mock_login.side_effect = [urllib2.URLError('url error'),
                              ucsexception.UcsException(500, 'ucs error')]
    with pytest.raises(SystemExit):
        ucsm_gui.launch('hostname', 'user', 'password')


@mock.patch('ucsmsdk.utils.ucsguilaunch.ucs_gui_launch')
@mock.patch('ucsmsdk.ucshandle.UcsHandle.login')
@mock.patch('socket.gethostbyaddr')
def test_launch_on_successful_login(mock_gethost, mock_login, mock_gui):
    mock_gethost.return_value = True
    mock_login.return_value = True
    ucsm_gui.launch('hostname', 'user', 'password')
    mock_gui.assert_called_once()
