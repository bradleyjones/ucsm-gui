import click


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--config', '-c', help='Path to config file')
@click.argument('host')
@click.argument('username', required=False)
@click.argument('password', required=False)
def main(config, host, username, password):
    """ Do some ucsm gui things
    """
    click.echo(click.get_current_context().get_help())
