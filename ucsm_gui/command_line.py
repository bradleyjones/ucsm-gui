import click
import ucsm_gui

from ucsm_gui import config as cfg


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def _get_username(conf, host):
    username = False
    if host in conf:
        username = conf[host].get('username', False)
    if not username:
        username = click.prompt('Enter username')
    return username


def _get_password(conf, host):
    # Look up password from config file first
    password = False
    if host in conf:
        password = conf[host].get('password', False)
    if not password:
        password = click.prompt('Enter password', hide_input=True)
    return password


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--config', '-c', help='Path to config file')
@click.argument('host')
@click.argument('username', required=False)
@click.argument('password', required=False)
def main(config, host, username, password):
    """ Launch UCSM GUI
    """
    conf = {}
    if config:
        conf = cfg.load(config)
    else:  # Try to load from the default config path
        conf = cfg.load()

    if username and password:
        ucsm_gui.launch(host, username, password)
    if username:
        password = _get_password(conf, host)
        ucsm_gui.launch(host, username, password)

    username = _get_username(conf, host)
    password = _get_password(conf, host)
    ucsm_gui.launch(host, username, password)
