from setuptools import setup

setup(
	name = 'CoviTweets',
	version = '0.1',
	description = """
		CoviTweets es un módulo en python para la categorización de tweets relacionados con el Covid.
	""",
	author = 'Ernesto Martínez del Pino',
	packages = ['CoviTweets'],
	install_requires = [i.strip() for i in open('requirements.txt').readlines()],
	test_suite = 'tests'
)