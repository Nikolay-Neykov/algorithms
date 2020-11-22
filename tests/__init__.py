from pathlib import Path

import yaml

resources_path = Path(__file__).parent / 'resources'


def read_yaml_resource(name):
    resource_path = Path(__file__).parent / 'resources' / name
    with open(resource_path) as f:
        return yaml.safe_load(f)
