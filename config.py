import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

BOOTSTRAP_SERVER = config["BOOTSTRAP_SERVER"]
TOPIC = config["TOPIC"]
SLEEP = config["SLEEP"]
DATETIME_FORMAT = config["DATETIME_FORMAT"]
JSON_FORMAT = config["JSON_FORMAT"]
EVENT = config["EVENT"]