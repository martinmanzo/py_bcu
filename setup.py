from setuptools import setup

setup(
    name='py_bcu',
    version='1.0.3',
    packages=['py_bcu'],
    package_dir={'': '.'},
    url='https://github.com/martinmanzo/py_bcu/',
    license='MIT',
    author='Martin Manzo',
    author_email='',
    description='Interact with the BCU\'s (Banco Central del Uruguay) webservices.',
    install_requires=[
        'zeep==4.0.0'
    ]
)
