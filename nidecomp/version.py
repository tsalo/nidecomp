from __future__ import absolute_import, division, print_function

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 0
_version_micro = 1  # use '' for first of series, number for 1 and above
_version_extra = 'a'

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "NiDecomp"
# Long description will go up on the pypi page
long_description = """

NiDecomp
========

Decomposition-based denoising methods for fMRI data.
"""

NAME = "NiDecomp"
MAINTAINER = "NiDecomp developers"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/tsalo/NiDecomp"
DOWNLOAD_URL = "http://github.com/tsalo/NiDecomp.git"
LICENSE = "MIT"
AUTHOR = "NiDecomp developers"
AUTHOR_EMAIL = "http://github.com/tsalo/NiDecomp"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
REQUIRES = ["nibabel", "numpy", "scipy", "pandas", "statsmodels", "nipype",
            "scikit-learn", "nilearn"],
ENTRY_POINTS = {}

EXTRAS_REQUIRES = {}
