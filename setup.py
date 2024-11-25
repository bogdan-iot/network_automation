from setuptools import find_packages, setup

setup(
    name='network-automation',
    version='0.1.0',
    packages=['src'],
    description='Network Automation Library',
    long_description="This is a library for Network Automation",
    author='Bogdan Radu',
    setup_requires=["pytest"]
)
