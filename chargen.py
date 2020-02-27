#!/usr/bin/env python

"""
Copyright (c) 2006-2020 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import re
import random
import string

from lib.core.data import kb
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    """
    replaces <here> with 3 random generated chars - helpful when we need to generate unique entries for user names

    Tested against:
        * Microsoft SQL Server 2005
        * MySQL 4, 5.0 and 5.5
        * Oracle 10g
        * PostgreSQL 8.3, 8.4, 9.0

    Notes:
        * Useful to bypass very weak and bespoke web application firewalls
          that has poorly written permissive regular expressions

    >>> tamper('INSERT')
    'insert'
    """

    retVal = payload
    if payload:
        all_ascii_letters = string.ascii_letters
        random_chars = ''.join(random.choice(all_ascii_letters) for i in range(3))
        retVal = retVal.replace("<here>",random_chars)
    return retVal

