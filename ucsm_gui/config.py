import sys
import yaml

from os.path import expanduser


DEFAULT_CONFIG_PATH = "{}/.ucsm_config.yaml".format(expanduser('~'))


def load(path=DEFAULT_CONFIG_PATH):
    try:
        with open(path) as p:
            try:
                config = yaml.safe_load(p)
                # jsonschema.validate(config, CONFIG_SCHEMA)
                return config
            except yaml.YAMLError:
                sys.exit("Unable to load config file")
    except IOError:
        if path is DEFAULT_CONFIG_PATH:
            return
        sys.exit("Config file does not exist at {}".format(path))
