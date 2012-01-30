#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai

__license__ = 'GPL v3'
__copyright__ = '2011, Hakan Tandogan <hakan at gurkensalat.com>'
__docformat__ = 'restructuredtext en'

import traceback

from calibre.customize import PathnamePlugin
from calibre.constants import filesystem_encoding
from calibre.utils.filenames import ascii_filename


class PathnameBySourceStrategy(PathnamePlugin):

    def __init__(self, database):
        self.database = database
        # TODO make prefix configurable
        self.source_prefix = _('Source')

    def construct_path_name(self, book_id):
        # print("PathnameBySourceStrategy: Me is %s" % PathnameBySourceStrategy.__name__)
        # print("PathnameBySourceStrategy: self: %s" % (self))
        # print("PathnameBySourceStrategy: db  : %s" % (self.database))
        # print("PathnameBySourceStrategy: bkid: %s" % (book_id))

        path_name_element = None

        try:
            tags = self.database.tags(book_id, index_is_id=True)
            print("PathnameBySourceStrategy: tags: '%s'" % (tags))
#            if series:
#                series_prefix = self.series_prefix
#                series_prefix = ascii_filename(series_prefix[:self.PATH_LIMIT]).decode(filesystem_encoding, 'ignore')
#                series_name = ascii_filename(series[:self.PATH_LIMIT]).decode(filesystem_encoding, 'ignore')
#                path_name_element = series_prefix + "/" + series_name
        except:
            traceback.print_exc()

        print("PathnameBySourceStrategy: path_name_element: '%s'" % (path_name_element))

        return path_name_element

#        prefix_source = prefs['prefix_source']
#        if prefix_source:
#            # print "Obtain Directory name from Tags"
#            tags = self.tags(id, index_is_id=True)
#            if tags:
#                source_p = _('Source')
#                # Catch-All
#                source_n = "from_somewhere_unknown"
#                # print "  Configured Tags are: %s" % tags
#                for split_tag in tags.split(','):
#                    print "    Split tag is: '%s'" % split_tag
#                    if split_tag.rfind('from_') > -1:
#                        source_n = split_tag
#                print "    Subdir '%s'" % source_n
#                path   = source_n + "/" + path

