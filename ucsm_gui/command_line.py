import click
import ucsm_gui

from ucsm_gui import config as cfg


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def _get_host_from_conf(conf, host):
    if host in conf:
        return conf[host]["hostname"], conf[host]
    return next(((conf[item]["hostname"], conf[item]) for item in conf
                if conf[item]["hostname"] == host), None)


def _get_username(host):
    username = host.get('username', False)
    if not username:
        username = click.prompt('Enter username')
    return username


def _get_password(host):
    password = host.get('password', False)
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

    host, host_details = _get_host_from_conf(conf, host)

    if username and password:
        ucsm_gui.launch(host, username, password)

    if username:
        password = _get_password(host_details)
        ucsm_gui.launch(host, username, password)

    username = _get_username(host_details)
    password = _get_password(host_details)
    ucsm_gui.launch(host, username, password)
