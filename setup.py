import file_iterator
from setuptools import setup,find_packages

setup(
    name='file_iterator',
    version='1.0.0',
    author='Vladimir Grablyk',
    author_email='v.grablyk@nicetu.spb.ru',
    url='http://nicetu.spb.ru',
    description='Разработка класса-итератора по файловой системе на Python',
    long_description="",
    zip_safe=False,
    packages = find_packages(include=['file_iterator', 'file_iterator.*']),
)
