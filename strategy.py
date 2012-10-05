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
        # TODO make default source configurable
        self.default_source = None

    def construct_path_name(self, book_id):
        print("  PbSourceS is %s" % (__name__))
        print("  PbSourceS: self : %s" % (self))
        print("  PbSourceS: database: %s" % (self.database))
        print("  PbSourceS: book id : %s" % (book_id))

        path_element = None

        try:
            metadata = self.database.get_metadata(book_id, index_is_id=True)
            print("    PbSourceS: metadata: '%s'" % (metadata))
            source = metadata.get(self.source_field_name)
            print("    PbSourceS: metadata.source: '%s'" % (source))

            # Special case for books which have no source set
            if source == None:
                source = self.default_source

            if source:
                source_prefix = self.source_prefix
                source_prefix = ascii_filename(source_prefix[:self.PATH_LIMIT]).decode(filesystem_encoding, 'ignore')
                source_name = ascii_filename(source[:self.PATH_LIMIT]).decode(filesystem_encoding, 'ignore')
                source_name = source_name.lower()
                # TODO: use a regex for whitespace, r = re.compile(r"^\s+", re.MULTILINE)
                source_name = source_name.replace(' ', '_')
                path_element = source_prefix + "_" + source_name
        except:
            traceback.print_exc()

        print("      PbSourceS: path_element: '%s'" % (path_element))

        return path_element
