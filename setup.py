#!/usr/bin/env python

from setuptools import setup, find_packages, Extension

version = file('VERSION').readline().strip()

ais_module = Extension('ais',
                    sources = ['ais_py.cpp',
                               'ais.cpp',
                               'ais1_2_3.cpp',
                               'ais4_11.cpp',
                               'ais5.cpp',
                               'ais6.cpp',
                               'ais7_13.cpp',
                               'ais8.cpp',
                               'ais8_001_22.cpp',
                               'ais9.cpp',
                               'ais10.cpp', # :
                               # 11 See 4 - ;
                               'ais12.cpp', # <
                               # 13 See 7 - =
                               'ais14.cpp', # >
                               'ais15.cpp', # ?
                               # 16
                               # 17
                               'ais18.cpp',
                               'ais19.cpp',
                               # 20
                               'ais21.cpp',
                               # 22
                               # 23
                               'ais24.cpp',
                               # 25
                               # 26
                               ])

setup (name = 'libais',
       version = version,
       description = 'Automatic Identification System decoding - ship tracking',
       author='Kurt Schwehr',
       author_email='schwehr@gmail.com',
       url='https://github.com/schwehr/libais',
       license='LGPL v3+',
       ext_modules = [ais_module],
       classifiers=[
            'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
            'Topic :: System :: Networking',
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'Topic :: Communications',
            'Topic :: Scientific/Engineering :: Information Analysis',
            'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
            'Topic :: Scientific/Engineering :: GIS',
    ],
       )
