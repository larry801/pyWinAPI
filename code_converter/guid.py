# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2016 EventGhost Project <http://www.eventghost.net/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function, absolute_import

import ctypes
from ctypes.wintypes import DWORD, WORD, BYTE

POINTER = ctypes.POINTER

_ole32 = ctypes.oledll.ole32
_StringFromCLSID = _ole32.StringFromCLSID
_CoTaskMemFree = ctypes.windll.ole32.CoTaskMemFree
_CLSIDFromString = _ole32.CLSIDFromString


# noinspection PyTypeChecker,PyCallingNonCallable
class _GUID(ctypes.Structure):
    _fields_ = [
        ('Data1', DWORD),
        ('Data2', WORD),
        ('Data3', WORD),
        ('Data4', BYTE * 8)
    ]

    def __cmp__(self, other):
        if isinstance(other, GUID):
            return cmp(bytes(self), bytes(other))
        return -1

    def __eq__(self, other):
        return isinstance(other, GUID) and bytes(self) == bytes(other)

    def __init__(self, *guid):
        """a144ed38 - 8e12 -4de4 - 9d 96 -e6 47 40 b1 a5 24}
        Data1 = 0xa144ed38
        Data2 = 0x8e12
        Data3 = 0x4de4
        data4[0] = -0x9d
        data4[1] = 0x96
        data4[2] = 0xe6
        data4[3] = 0x47
        data4[4] = 0x40
        data4[5] = 0xb1
        data4[6] = 0xa5
        data4[7] = 0x24
        """

        if not guid:
            guid = None

        elif len(guid) == 1:
            guid = guid[0]

        else:
            guid = list(hex(itm)[2:].replace('L', '') for itm in guid)

            l, w1, w2 = guid[:3]

            while len(l) < 8:
                l = '0' + l

            while len(w1) < 4:
                w1 = '0' + w1

            while len(l) < 4:
                w2 = '0' + w2

            for i, itm in enumerate(guid[3:]):
                if len(itm) < 2:
                    itm = '0' + itm
                guid[i + 3] = itm.upper()

            guid = '{{{0}-{1}-{2}-{3}{4}-{5}{6}{7}{8}{9}{10}}}'.format(
                l.upper(),
                w1.upper(),
                w2.upper(),
                *guid[3:]
            )

        ctypes.Structure.__init__(self)
        if guid is not None:
            _CLSIDFromString(unicode(guid), ctypes.byref(self))

    def __str__(self):
        p = ctypes.c_wchar_p()
        _StringFromCLSID(ctypes.byref(self), ctypes.byref(p))
        result = p.value
        _CoTaskMemFree(p)
        return result


TEMPLATE = '''{indent}{var_name} = {func_name}(
{hex_codes}
{indent})'''


def EXTERN_GUID(*args):
    return _GUID(*args)


def parse_guid(indent, guid):
    line = ' '.join(g.strip() for g in guid)
    if line.startswith('#'):
        return ''

    if 'EXTERN_GUID' in line:
        func_name = 'EXTERN_GUID'

    elif 'DEFINE_GUIDSTRUCT' in line:
        func_name = 'DEFINE_GUIDSTRUCT'

    elif 'DEFINE_GUID' in line:
        func_name = 'DEFINE_GUID'

    elif 'DEFINE_OLEGUID' in line:
        func_name = 'DEFINE_OLEGUID'

    elif 'DEFINE_DEVPROPKEY' in line:
        func_name = 'DEFINE_DEVPROPKEY'

    elif 'DEFINE_PROPERTYKEY' in line:
        func_name = 'DEFINE_PROPERTYKEY'

    elif 'DEFINE_GUIDNAMED' in line:
        func_name = 'DEFINE_GUIDNAMED'

    elif 'GUID_BUILDER' in line:
        func_name = 'GUID_BUILDER'

    elif line.strip().startswith('OUR_GUID_ENTRY'):
        func_name = 'OUR_GUID_ENTRY'
    else:
        return False

    if func_name in ('DEFINE_GUIDSTRUCT', 'DEFINE_GUIDNAMED'):
        line = line.replace(func_name + '(', '').replace(')', '')
        line = line.replace(';', '').strip()
        guid_str, var_name = line.split(',', 1)
        var_name = var_name.strip()
        hex_codes = indent + '    ' + guid_str.strip()

    elif func_name == 'GUID_BUILDER':
        # define  LIBID_ADOR25 GUID_BUILDER(LIBID_ADOR25,00000305,0000,0010,80,00,00,AA,00,6D,2E,A4)
        line = line.strip()[line.find('GUID_BUILDER(') + 13:-1]
        line = list(item.strip() for item in line.split(','))
        var_name = line[0]
        hex_codes = line[1:]
        for i, item in enumerate(hex_codes[:]):
            if item.startswith('0x'):
                item = item[2:]
            hex_codes[i] = item.upper()

        hex_codes = '\n'.join(
            indent + '    0x' + code.replace('L', '') + ','
            for code in hex_codes
        )

    else:
        line = line.replace(func_name + '(', '').replace(')', '')
        line = line.replace(';', '').strip()

        try:
            var_name, hex_codes = line.split(',', 1)
        except:
            print(guid)
            raise
        var_name = var_name.strip()
        hex_codes = hex_codes.strip()

        if not hex_codes:
            return ''

        hex_codes = hex_codes.split(',')
        codes = hex_codes[:11]

        if 'PROPKEY' in func_name or 'PROPERTYKEY' in func_name:
            try:
                codes += [hex(int(hex_codes[-1]))]
            except ValueError:
                pass

        hex_codes = '\n'.join(
            indent + '    0x' + code.strip()[2:].upper().replace('L', '') + ','
            for code in codes
        )[:-1]

    return (
        TEMPLATE.format(
            indent=indent,
            var_name=var_name.strip(),
            func_name=func_name,
            hex_codes=hex_codes
        )
    )

#
#
# class GUID(object):
#
#     def __init__(self, importer, data):
#         self.importer = importer
#         self._guids = []
#         self.lines = {}
#         self.all = set()
#         start = None
#         builder = False
#         print "\n\n-- GUID -----------------------------------------------\n\n"
#         for i, line in enumerate(data[:]):
#             if line.startswith('EXTERN_GUID'):
#                 print line
#                 start = i
#                 new_importer = importer.add_importer('guiddef_h')
#                 new_importer.add('EXTERN_GUID')
#
#             elif line.startswith('DEFINE_GUID'):
#                 start = i
#                 new_importer = importer.add_importer('guiddef_h')
#                 new_importer.add('DEFINE_GUID')
#
#             elif line.startswith('DEFINE_OLEGUID'):
#                 start = i
#                 new_importer = importer.add_importer('guiddef_h')
#                 new_importer.add('DEFINE_OLEGUID')
#
#             elif line.startswith('DEFINE_DEVPROPKEY'):
#                 start = i
#                 new_importer = importer.add_importer('devpropdef_h')
#                 new_importer.add('DEFINE_DEVPROPKEY')
#
#             elif line.startswith('DEFINE_PROPERTYKEY'):
#                 start = i
#                 new_importer = importer.add_importer('propkeydef_h')
#                 new_importer.add('DEFINE_PROPERTYKEY')
#
#             elif line.startswith('DEFINE_GUIDSTRUCT'):
#                 start = i
#                 new_importer = importer.add_importer('guiddef_h')
#                 new_importer.add('DEFINE_GUIDSTRUCT')
#             elif line.startswith('DEFINE_GUIDNAMED'):
#                 start = i
#                 new_importer = importer.add_importer('guiddef_h')
#                 new_importer.add('DEFINE_GUIDNAMED')
#             elif 'GUID_BUILDER' in line:
#                 start = i
#                 builder = True
#                 new_importer = importer.add_importer('adoguids_h')
#                 new_importer.add('GUID_BUILDER')
#
#             if start is not None:
#                 if builder and line.strip().endswith(')'):
#                     self.lines[start] = data[start:i + 1]
#                     print self.lines[start]
#                     start = None
#                     builder = False
#
#                 elif not builder and line.rstrip().endswith(';'):
#                     self.lines[start] = data[start:i + 1]
#                     print self.lines[start]
#                     start = None
#
#     def process(self):
#         # if self._guids:
#         #     for g in self._guids:
#         #         yield g['line_num'], g['code']
#
#         for line_num, lines in self.lines.items()[:]:
#             line = ' '.join(lines)
#             if 'EXTERN_GUID' in line:
#                 func_name = 'EXTERN_GUID'
#
#             elif 'DEFINE_GUIDSTRUCT' in line:
#                 func_name = 'DEFINE_GUIDSTRUCT'
#
#             elif 'DEFINE_GUID' in line:
#                 func_name = 'DEFINE_GUID'
#
#             elif 'DEFINE_OLEGUID' in line:
#                 func_name = 'DEFINE_OLEGUID'
#
#             elif 'DEFINE_DEVPROPKEY' in line:
#                 func_name = 'DEFINE_DEVPROPKEY'
#
#             elif 'DEFINE_PROPERTYKEY' in line:
#                 func_name = 'DEFINE_PROPERTYKEY'
#
#             elif 'DEFINE_GUIDNAMED' in line:
#                 func_name = 'DEFINE_GUIDNAMED'
#
#             elif 'GUID_BUILDER' in line:
#                 func_name = 'GUID_BUILDER'
#             else:
#                 continue
#
#             if func_name in ('DEFINE_GUIDSTRUCT', 'DEFINE_GUIDNAMED'):
#                 line = line.replace(func_name + '(', '').replace(')', '')
#                 line = line.replace(';', '').strip()
#                 guid_str, var_name = line.split(',', 1)
#                 var_name = var_name.strip()
#                 hex_codes = '    ' + guid_str.strip()
#
#             elif func_name == 'GUID_BUILDER':
#                 # define  LIBID_ADOR25 GUID_BUILDER(LIBID_ADOR25,00000305,0000,0010,80,00,00,AA,00,6D,2E,A4)
#                 line = line.strip()[line.find('GUID_BUILDER(') + 13:-1]
#                 line = list(item.strip() for item in line.split(','))
#                 var_name = line[0]
#                 hex_codes = line[1:]
#                 for i, item in enumerate(hex_codes[:]):
#                     if item.startswith('0x'):
#                         item = item[2:]
#                     hex_codes[i] = item.upper()
#
#                 hex_codes = '\n'.join(
#                     '    0x' + code + ','
#                     for code in hex_codes
#                 )
#
#             else:
#                 line = line.replace(func_name + '(', '').replace(')', '')
#                 line = line.replace(';', '').strip()
#                 var_name, hex_codes = line.split(',', 1)
#                 var_name = var_name.strip()
#                 hex_codes = hex_codes.strip()
#
#                 hex_codes = hex_codes.split(',')
#                 codes = hex_codes[:11]
#
#                 if 'PROPKEY' in func_name or 'PROPERTYKEY' in func_name:
#                     try:
#                         codes += [hex(int(hex_codes[-1]))]
#                     except ValueError:
#                         pass
#
#                 hex_codes = '\n'.join(
#                     '    0x' + code.strip()[2:].upper() + ','
#                     for code in codes
#                 )[:-1]
#
#             yield line_num, TEMPLATE.format(
#                 var_name=var_name.strip(),
#                 func_name=func_name,
#                 hex_codes=hex_codes
#             )
#
#             self.all.add(var_name)
#
#     def __getitem__(self, item):
#         namespace = dict(
#             EXTERN_GUID=EXTERN_GUID
#         )
#         if not self._guids:
#             for line_num, code in self.process():
#                 try:
#                     exec(code, {}, namespace)
#                 except SyntaxError:
#                     print code
#                     continue
#                 for iid_name, iid in namespace.items():
#                     if isinstance(iid, _GUID):
#                         self._guids += [
#                             dict(
#                                 code=code,
#                                 guid=str(iid),
#                                 name=iid_name,
#                                 line_num=line_num
#                             )
#                         ]
#         for g in self._guids:
#             if item.upper() in (g['guid'].upper(), g['name'].upper()):
#                 return g['name']
#
#         raise KeyError(item)
#
