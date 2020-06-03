"""
infinity
--------

All-in-one infinity value for Python. Can be compared to any object.
"""
from setuptools import setup, find_packages
import os
import re
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
PY3 = sys.version_info[0] == 3


def get_version():
    filename = os.path.join(HERE, 'infinity.py')
    with open(filename) as f:
        contents = f.read()
    pattern = r"^__version__ = '(.*?)'$"
    return re.search(pattern, contents, re.MULTILINE).group(1)


extras_require = {
    'test': [
        'pytest>=2.2.3',
        'Pygments>=1.2',
        'six>=1.4.1',
        'flake8>=2.4.0',
        'isort>=4.2.2',
    ],
}


setup(
    name='infinity',
    version=get_version(),
    url='https://github.com/kvesteri/infinity',
    license='BSD',
    author='Konsta Vesterinen',
    author_email='konsta@fastmonkeys.com',
    description=(
        'All-in-one infinity value for Python. Can be compared to any object.'
    ),
    long_description=__doc__,
    packages=find_packages('.'),
    py_modules=['infinity'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    dependency_links=[],
    install_requires=[
        'total_ordering>=0.1'
        if sys.version_info[0] == 2 and sys.version_info[1] < 7 else ''
    ],
    extras_require=extras_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
