import jsonschema
import mock
import pytest
import tempfile
import ucsm_gui


VALID_CONFIG = """
---
TEST-HOST:
  hostname: 127.0.0.1
  username: me
  password: password
"""

VALID_RESPONSE = {'TEST-HOST': {'hostname': '127.0.0.1',
                                'username': 'me',
                                'password': 'password'}}

INVALID_CONFIG = """
---
TEST-HOST:
  hostname: IM_INVALID
"""

INVALID_YAML = """
--
TEST-HOST
username me
  password: password
"""


def generate_config_fixture(conf):
    @pytest.yield_fixture
    def mock_config():
        with mock.patch("ucsm_gui.config.open") as mock_open:
            f = tempfile.SpooledTemporaryFile()
            f.write(conf.encode())
            f.flush()
            f.seek(0)
            mock_open.return_value = f
            yield mock_open
            f.close()
    return mock_config


mock_invalid_config = generate_config_fixture(INVALID_CONFIG)
mock_invalid_yaml_config = generate_config_fixture(INVALID_YAML)
mock_valid_config = generate_config_fixture(VALID_CONFIG)


def test_invalid_yaml_config(mock_invalid_yaml_config):
    with pytest.raises(SystemExit):
        ucsm_gui.config.load(path='invalidyaml')
    mock_invalid_yaml_config.assert_called_with('invalidyaml')


def test_invalid_config(mock_invalid_config):
    with pytest.raises(jsonschema.ValidationError):
        ucsm_gui.config.load(path='invalidconf')
    mock_invalid_config.assert_called_with('invalidconf')


def test_valid_config(mock_valid_config):
    assert ucsm_gui.config.load(path='validconf') == VALID_RESPONSE
    mock_valid_config.assert_called_with('validconf')


@mock.patch('ucsm_gui.config.open')
def test_default_config_path(mock_open):
    mock_open.side_effect = [IOError]
    ucsm_gui.config.load()
    mock_open.assert_called_with(ucsm_gui.config.DEFAULT_CONFIG_PATH)


def test_config_file_does_not_exist():
    with pytest.raises(SystemExit):
        ucsm_gui.config.load('/var/lib/i/do/not/exist.yaml')
