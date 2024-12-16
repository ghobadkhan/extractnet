#!/usr/bin/env python

# Copyright (c) 2012 SEOmoz
# Copyright (c) 2020 Pheme Pte Ltd
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os.path
import platform
from setuptools import setup, Extension
# have to import `Extension` after `setuptools.setup`
# from distutils.extension import Extension
import sys
import re, io
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import lxml
from numpy import get_include

def find_libxml2_include():
    include_dirs = []
    for d in ['/usr/include/libxml2', '/usr/local/include/libxml2']:
        if os.path.exists(os.path.join(d, 'libxml/tree.h')):
            include_dirs.append(d)
    return include_dirs

# set min MacOS version, if necessary
if sys.platform == 'darwin':
    os_version = '.'.join(platform.mac_ver()[0].split('.')[:2])
    # this seems to work better than the -mmacosx-version-min flag
    os.environ['MACOSX_DEPLOYMENT_TARGET'] = os_version

ext_modules = [
    Extension('extractnet.lcs',
              sources=["src/extractnet/lcs.pyx"],
              include_dirs=[get_include()],
              language="c++",
              define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")]),
    Extension('extractnet.blocks',
              sources=["src/extractnet/blocks.pyx"],
              include_dirs=(lxml.get_include() + find_libxml2_include()),
              language="c++",
              libraries=['xml2'],
              define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")]),
    Extension('extractnet.features._readability',
              sources=["src/extractnet/features/_readability.pyx"],
              include_dirs=[get_include()],
              extra_compile_args=['-std=c++11'],
              language="c++",
              define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")]),
    Extension('extractnet.features._kohlschuetter',
              sources=["src/extractnet/features/_kohlschuetter.pyx"],
              include_dirs=[get_include()],
              language="c++",
              define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")]),
    Extension('extractnet.features._weninger',
              sources=["src/extractnet/features/_weninger.pyx"],
              include_dirs=[get_include()],
              language="c++",
              define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")]),
]

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(ext_modules, language_level = "-3")
)
