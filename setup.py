#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup
import glob
import os
from DistUtilsExtra.command import *

setup(name='stalone_tray_clock',
      version='1.0.0',
      description='Simples relógio para Stalonetray/Openbox',
      author='Alexandre C Vieira',
      author_email='acamargo.vieira@gmail.com',
      url='https://github.com/alexandrecvieira/stalone_tray_clock',
      scripts=[
          'stalone_tray_clock',
      ],
      cmdclass={}
      )
