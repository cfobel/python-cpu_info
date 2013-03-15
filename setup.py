#!/usr/bin/env python

from distutils.core import setup

setup(name = "cpu_info",
    version = "0.0.1",
    description = "Wrapper around `cat /proc/cpuinfo`, parse to dictionary",
    keywords = "cpuinfo",
    author = "Christian Fobel",
    url = "https://github.com/cfobel/python-cpu_info",
    license = "GPL",
    long_description = """""",
    packages = ['cpu_info']
)
