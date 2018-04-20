import jsonschema
import sys
import yaml

from os.path import expanduser


DEFAULT_CONFIG_PATH = "{}/.ucsm_config.yaml".format(expanduser('~'))

CONFIG_SCHEMA = {
    "title": "Hosts",
    "type": "object",
    "patternProperties": {
        "^.+": {
            "type": "object",
            "properties": {
                "hostname": {
                    "type": "string",
                    "pattern": "^([a-zA-Z0-9\-\.])+$"
                },
                "username": {
                    "type": "string"
                },
                "password": {
                    "type": "string"
                }
            },
            "required": ["hostname"],
            "additionalProperties": False
        }
    }
}


def load(path=DEFAULT_CONFIG_PATH):
    try:
        with open(path) as p:
            try:
                config = yaml.safe_load(p)
                jsonschema.validate(config, CONFIG_SCHEMA)
                return config
            except yaml.YAMLError:
                sys.exit("Unable to load config file, error parsing YAML")
    except IOError:
        if path is DEFAULT_CONFIG_PATH:
            return {}
        sys.exit("Config file does not exist at {}".format(path))
