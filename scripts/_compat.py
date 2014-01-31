# -*- coding: utf8 -*-

import sys

PY2 = sys.version_info[0] == 2

if PY2:
    unichr = unichr
    text_type = unicode
    string_types = (str, unicode)

    from cStringIO import StringIO as BytesIO
    from StringIO import StringIO

    from urllib import urlretrieve
else:
    unichr = chr
    text_type = str
    string_types = (str,)

    from io import StringIO, BytesIO

    from urllib.request import urlretrieve
