from distutils.core import setup
from setuptools import find_packages

setup(name='django-registration-templates',
      version='0.1.0',
      description='A set of registration templates for use with django-registration and Django',
      author='Ryan Kanno',
      author_email='ryankanno@localkinegrinds.com',
      packages=['registration_templates',],
      package_dir={'registration_templates': 'registration_templates'},
      package_data={'registration_templates': ['templates/**/*']},
      long_description=open('README.txt').read(),
      install_requires=[
        "Django >= 1.4.0",
        "django-registration >= 0.8.0"
      ]
)
