#!/usr/bin/env python

#from distutils.core import setup
#import py2exe
from detect import LINUX
from distribute_setup import use_setuptools
from setuptools import setup
from version import VERSION
use_setuptools()


try:
	import py2exe
except ImportError:
	py2exe = None


args = {
    'name': 'poclbm',
    'version': VERSION,
    'description': 'Bitcoin miner in python',
    'author': 'Momchil Georgiev',
    'author_email': 'pishtov@gmail.com',
    'url': 'https://github.com/m0mchil/poclbm/',
    'install_requires': ['pyserial>=2.6'],
    'scripts': ['poclbm.py'],
    'windows': [
        'script': 'guiminer.py',
        'icon_resources': [(0, "logo.ico")]
    ]
}

if LINUX:
	args['install_requires'].append('pyudev>=0.16')

if py2exe:
	args.update({
		# py2exe options
		'options': {'py2exe':
						{'optimize': 2,
						'bundle_files': 2,
						'compressed': True,
						'dll_excludes': ['OpenCL.dll', 'w9xpopen.exe', 'boost_python-vc90-mt-1_39.dll'],
						'excludes': ["Tkconstants", "Tkinter", "tcl", "curses", "_ssl", "pyexpat", "unicodedata", "bz2"],
						'includes': ["minerutil", "twisted.web.resource", "QueueReader"],

						},
					},
		'console': ['phoenix.py', 'poclbm.py', 'po_to_mo.py'],
		'data_files': ['phatk.cl', 'msvcp90.dll', 'phatk.cl', 'logo.ico', 'LICENSE.txt', 'servers.ini', 'README.txt', 'defaults.ini'],
		'zipfile': None,
	})

setup(**args)
