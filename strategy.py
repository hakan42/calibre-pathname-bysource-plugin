#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

__license__ = 'GPL v3'
__copyright__ = '2011, Hakan Tandogan <hakan at gurkensalat.com>'
__docformat__ = 'restructuredtext en'

from calibre.customize import PathnamePlugin

from calibre.utils.filenames import ascii_filename

class PathnameBySourceStrategy(PathnamePlugin):

    def __init__(self, database):
        self.database = database

    def construct_path_name(self, book_id):
        print("PathnameBySourceStrategy: Me is %s" % PathnameBySourceStrategy.__name__)
        print("PathnameBySourceStrategy: self: %s" % (self))
        print("PathnameBySourceStrategy: db  : %s" % (self.database))
        print("PathnameBySourceStrategy: bkid: %s" % (book_id))
