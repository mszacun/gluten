from setuptools import setup

setup(
    name='Gluten',
    url='https://gitlab.dynamic.nsn-net.net/szachun/gluten',
    author='Marcin Szachun, Michał Bieroński, Krystian Skibiński',
    packages=['gluten'],
    install_requires=['selenium', 'pytest'],
    version='0.1',
    license='MIT',
    description='Page object pattern selenium library',
)
