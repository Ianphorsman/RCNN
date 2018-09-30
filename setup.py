from setuptools import setup

setup(
    name='rcnn-models',
    description="RCNN Model implementations",
    url="https://github.com/Ianphorsman/RCNN",
    author='Ian Horsman',
    author_email='ianphorsman@gmail.com',
    license='MIT',
    version='0.0.1',
    packages=['model'],
    install_requires=['numpy', 'pandas', 'tensorflow-gpu']
)