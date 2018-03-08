import click
import ucsm_gui


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--config', '-c', help='Path to config file')
@click.argument('host')
@click.argument('username', required=False)
@click.argument('password', required=False)
def main(config, host, username, password):
    """ Launch UCSM GUI
    """
    if username and password:
        ucsm_gui.launch(host, username, password)
    if username:
        password = click.prompt('Enter password', hide_input=True)
        ucsm_gui.launch(host, username, password)

    # TODO Look up host from config file
    username = click.prompt('Enter username')
    password = click.prompt('Enter password', hide_input=True)
    ucsm_gui.launch(host, username, password)
