import mock

from click.testing import CliRunner
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
    assert command_line._get_password({}) == 'testpass'


def test_cli_no_args():
    runner = CliRunner()
    result = runner.invoke(command_line.main, [])
    assert result.exit_code == 2
    assert 'Missing argument "host"' in result.output


# Test config file + host via cli, username & password passed in via stdin
@mock.patch('ucsm_gui.launch')
@mock.patch('ucsm_gui.config.load')
def test_cli_config_host(mock_config_load, mock_launch):
    mock_config_load.return_value = {}
    mock_launch.return_value = True
    runner = CliRunner()
    result = runner.invoke(command_line.main,
                           ['-c', '/path/to/config/file', 'testhost'],
                           input='username\npassword\n')
    assert result.exit_code == 0
    assert mock_config_load.called_once_with('/path/to/config/file')
    assert mock_launch.called_once_with('testhost', 'username', 'password')


# Test host via cli, username & password passed in via stdin
@mock.patch('ucsm_gui.launch')
def test_cli_host(mock_launch):
    mock_launch.return_value = True
    runner = CliRunner()
    result = runner.invoke(command_line.main,
                           ['testhost'],
                           input='username\npassword\n')
    assert result.exit_code == 0
    assert mock_launch.called_once_with('testhost', 'username', 'password')


# Test host & username via cli, password passed in via stdin
@mock.patch('ucsm_gui.launch')
def test_cli_host_username(mock_launch):
    mock_launch.return_value = True
    runner = CliRunner()
    result = runner.invoke(command_line.main,
                           ['testhost', 'username'],
                           input='password\n')
    assert result.exit_code == 0
    assert mock_launch.called_once_with('testhost', 'username', 'password')


# Test host, username & password passed in via cli
@mock.patch('ucsm_gui.launch')
def test_cli_host_username_password(mock_launch):
    mock_launch.return_value = True
    runner = CliRunner()
    result = runner.invoke(command_line.main,
                           ['testhost', 'username', 'password'])
    assert result.exit_code == 0
    assert mock_launch.called_once_with('testhost', 'username', 'password')
