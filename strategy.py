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
        self.source_prefix = _('from')
        self.source_field_name = '#source'

    def construct_path_name(self, book_id):
        # print("PathnameBySourceStrategy: Me is %s" % PathnameBySourceStrategy.__name__)
        # print("PathnameBySourceStrategy: self: %s" % (self))
        # print("PathnameBySourceStrategy: db  : %s" % (self.database))
        # print("PathnameBySourceStrategy: bkid: %s" % (book_id))

        path_name_element = None

        try:
            metadata = self.database.get_metadata(book_id, index_is_id=True)
            # print("PathnameBySourceStrategy: metadata: '%s'" % (metadata))
            source = metadata.get(self.source_field_name)
            print("PathnameBySourceStrategy: metadata.source: '%s'" % (source))

            # Special case for books which have no source set
            if source == None:
                source = 'unknown'

            if source:
                source_prefix = self.source_prefix
                source_prefix = ascii_filename(source_prefix[:self.PATH_LIMIT]).decode(filesystem_encoding, 'ignore')
                source_name = ascii_filename(source[:self.PATH_LIMIT]).decode(filesystem_encoding, 'ignore')
                path_name_element = source_prefix + "_" + source_name
        except:
            traceback.print_exc()

        print("PathnameBySourceStrategy: path_name_element: '%s'" % (path_name_element))

        return path_name_element
