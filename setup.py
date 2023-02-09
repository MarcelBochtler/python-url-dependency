import json

from setuptools import setup

with open("version.json", 'r') as f:
    version = f.read()

version = json.loads(version)

setup(
    name='example',
    version='0.0.1',
    install_requires=[
        f"common-py @ git+https://sourcecode.socialcoding.bosch.com/scm/ivs/ivs_cloud_services_common_py.git@{version['common']}"
    ]
)
