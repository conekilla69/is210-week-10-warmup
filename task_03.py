#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""Corrected"""

import data

CORRECTED = data.BANDS.copy()
CORRECTED['Dylan'] = {'Bob Dylan': ['vocals', 'guitar', 'harmonica']}
CORRECTED = data.BANDS.copy()
CORRECTED['Van Halen'] = {'Sammy Hagar': ['vocals']}
