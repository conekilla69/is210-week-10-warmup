#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""Task_04 Bickingham"""


import data

BUCKINGHAM_NICKS  = {
                    'Lindsey Buckingham': (['guitar', 'vocals']),
                    'Stevie Nicks': (['vocals', 'tambourine'])

}
data.BANDS['Fleetwood Mac'].update(BUCKINGHAM_NICKS)
