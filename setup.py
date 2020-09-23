from setuptools import setup

setup(
    name='py_bcu',
    version='1.0.2',
    packages=['py_bcu'],
    package_dir={'': '.'},
    url='https://github.com/martinmanzo/py_bcu/',
    license='MIT',
    author='Martin Manzo',
    author_email='',
    description='Interact with the BCU\'s (Banco Central del Uruguay) webservices.',
    install_requires=[
        'zeep==3.4.0'
    ]
)
