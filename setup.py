try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import M

packages = [
    'M',
]

package_data = {
}

requires = [
]

classifiers = [
    'Packages',
    'Skeleton'
]

config = {
    'name': 'projectname',
    'version': M.__version__,
    'description': 'My Project',
    'author': 'fkymy',
    'url': 'https://github.com/fkymy/cpp',
    'packages': packages,
    'package_data': package_data,
    'install_requires': requires,
    'classifiers': classifiers
}

setup(**config)

