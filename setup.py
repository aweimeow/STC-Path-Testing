import setuptools
from distutils.core import setup

setup(
  name='STC_Path_Testing',
  packages=['STC_Path_Testing'],
  version='0.1',
  description='Software Testing Homework for Path Testing',
  author='aweimeow(Wei-You Chen)',
  author_email='aweimemow.tw@gmail.com',
  url='https://github.com/aweimeow/STC-Path-Testing',
  download_url=('https://github.com/aweimeow/'
                'STC-Path-Testing/archive/0.1.tar.gz'),
  keywords=[],
  classifiers=[],
  setup_requires=['pytest-runner'],
  tests_require=['pytest'],
)
