
from setuptools import setup, find_packages


setup(
    name='funcobs-pytorch',
    version='0.1.0',
    author='Hassan A. Kingravi',
    author_email='hkingravi@gmail.com',
    description='Function observers using PyTorch',
    url='https://github.com/hkingravi/funcobs-pytorch',
    packages=find_packages(exclude=['*.test', 'test']),
    install_requires=[]
)
