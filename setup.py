from setuptools import setup

setup(
    name='distracting_control',
    py_modules=['distracting_control'],
    version='1.0.0',
    install_requires=[
        'dm-control',
        'absl-py',
        'numpy',
        'mock',
        'pillow'
    ],
    description="The Distracting Control Suite",
)
