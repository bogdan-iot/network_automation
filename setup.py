from setuptools import find_packages, setup

setup(
    name='network_automation',
    packages=find_packages(include=['network_automation']),
    version='0.1.0',
    description='Network Automation Library',
    author='Bogdan Radu',
    setup_requires=['pytest>=8.3'],
    tests_require=['pytest>=8.3'],
    test_suite='tests'
)
