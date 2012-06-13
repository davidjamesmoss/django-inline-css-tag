from setuptools import setup, find_packages

setup(name='inline-css',
	version='1.0',
	description='Django template tag to generate inline CSS for any HTML it surrounds.',
	author='David Moss',
	author_email='david@illansis.com',
	packages=find_packages(),
	install_requires=['setuptools','pynliner'],
)