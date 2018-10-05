__REQUIRED_RPCNDR_H_VERSION__ = 0x1F4
__REQUIRED_RPCSAL_H_VERSION__ = 0x64
# from .rpc_h import * # NOQA
# from .rpcndr_h import * # NOQA
from .basetsd_h import * # NOQA
from .guiddef_h import * # NOQA

from .wtypes_h import (
    ENUM,
    USHORT,
    POINTER,
    BYTE,
    UCHAR,
    DWORD,
    LPWSTR,
    LONGLONG,
    GUID,
    ULONGLONG,
    UINT,
    WORD,
    LPVOID,
    BOOL,
    PVOID,
    LONG,
    VOID,
    WCHAR,
    UBYTE,
)
import ctypes


ULONG = ctypes.c_ulong

# INTerface __MIDL_itf_wtypesbase_0000_0000
# [local]
# +-------------------------------------------------------------------------

# Microsoft Windows
# Copyright (c) Microsoft Corporation. All rights reserved.

# --------------------------------------------------------------------------
# padding added after data member
# INTerface IWinTypesBase
# [unique][version][uuid]
# [string]
# [string]
# [string]
# [string]
# [string]
# [string]
# 0
OLECHAR = WCHAR
# [string]
# [string]


def OLESTR(str):
    return str


class _LARGE_INTEGER(ctypes.Structure):
    _fields_ = [
        ('QuadPart', LONGLONG),
    ]


LARGE_INTEGER = _LARGE_INTEGER


class _ULARGE_INTEGER(ctypes.Structure):
    _fields_ = [
        ('QuadPart', ULONGLONG),
    ]


ULARGE_INTEGER = _ULARGE_INTEGER
PULARGE_INTEGER = POINTER(_ULARGE_INTEGER)


class _FILETIME(ctypes.Structure):
    _fields_ = [
        ('dwLowDateTime', DWORD),
        ('dwHighDateTime', DWORD),
    ]


FILETIME = _FILETIME
PFILETIME = POINTER(_FILETIME)
LPFILETIME = POINTER(_FILETIME)


class _SYSTEMTIME(ctypes.Structure):
    _fields_ = [
        ('wYear', WORD),
        ('wMonth', WORD),
        ('wDayOfWeek', WORD),
        ('wDay', WORD),
        ('wHour', WORD),
        ('wMinute', WORD),
        ('wSecond', WORD),
        ('wMilliseconds', WORD),
    ]


SYSTEMTIME = _SYSTEMTIME
PSYSTEMTIME = POINTER(_SYSTEMTIME)
LPSYSTEMTIME = POINTER(_SYSTEMTIME)


class _SECURITY_ATTRIBUTES(ctypes.Structure):
    _fields_ = [
        ('nLength', DWORD),
        ('lpSecurityDescriptor', LPVOID),
        ('bInheritHandle', BOOL),
    ]


SECURITY_ATTRIBUTES = _SECURITY_ATTRIBUTES
PSECURITY_ATTRIBUTES = POINTER(_SECURITY_ATTRIBUTES)
LPSECURITY_ATTRIBUTES = POINTER(_SECURITY_ATTRIBUTES)
SECURITY_DESCRIPTOR_CONTROL = USHORT
PSECURITY_DESCRIPTOR_CONTROL = POINTER(USHORT)
PSID = PVOID


class _ACL(ctypes.Structure):
    _fields_ = [
        ('AclRevision', UCHAR),
        ('Sbz1', UCHAR),
        ('AclSize', USHORT),
        ('AceCount', USHORT),
        ('Sbz2', USHORT),
    ]


ACL = _ACL
PACL = POINTER(ACL)


class _SECURITY_DESCRIPTOR(ctypes.Structure):
    _fields_ = [
        ('Revision', UCHAR),
        ('Sbz1', UCHAR),
        ('Control', SECURITY_DESCRIPTOR_CONTROL),
        ('Owner', PSID),
        ('Group', PSID),
        ('Sacl', PACL),
        ('Dacl', PACL),
    ]


SECURITY_DESCRIPTOR = _SECURITY_DESCRIPTOR
PISECURITY_DESCRIPTOR = POINTER(_SECURITY_DESCRIPTOR)


class _COAUTHIDENTITY(ctypes.Structure):
    _fields_ = [
        ('User', POINTER(USHORT)),
        ('UserLength', ULONG),
        ('Domain', POINTER(USHORT)),
        ('DomainLength', ULONG),
        ('Password', POINTER(USHORT)),
        ('PasswordLength', ULONG),
        ('Flags', ULONG),
    ]


COAUTHIDENTITY = _COAUTHIDENTITY


class _COAUTHINFO(ctypes.Structure):
    _fields_ = [
        ('dwAuthnSvc', DWORD),
        ('dwAuthzSvc', DWORD),
        ('pwszServerPrincName', LPWSTR),
        ('dwAuthnLevel', DWORD),
        ('dwImpersonationLevel', DWORD),
        ('pAuthIdentityData', POINTER(COAUTHIDENTITY)),
        ('dwCapabilities', DWORD),
    ]


COAUTHINFO = _COAUTHINFO

SCODE = LONG
PSCODE = POINTER(SCODE)


class _OBJECTID(ctypes.Structure):
    _fields_ = [
        ('Lineage', GUID),
        ('Uniquifier', ULONG),
    ]


OBJECTID = _OBJECTID


class tagMEMCTX(ENUM):
    MEMCTX_TASK = 1
    MEMCTX_SHARED = 2
    MEMCTX_MACSYSTEM = 3
    MEMCTX_UNKNOWN = - 1
    MEMCTX_SAME = - 2


MEMCTX = tagMEMCTX

ROTREGFLAGS_ALLOWANYCLIENT = 0x1
APPIDREGFLAGS_ACTIVATE_IUSERVER_INDESKTOP = 0x1
APPIDREGFLAGS_SECURE_SERVER_PROCESS_SD_AND_BIND = 0x2
APPIDREGFLAGS_ISSUE_ACTIVATION_RPC_AT_IDENTIFY = 0x4
APPIDREGFLAGS_IUSERVER_UNMODIFIED_LOGON_TOKEN = 0x8
APPIDREGFLAGS_IUSERVER_SELF_SID_IN_LAUNCH_PERMISSION = 0x10
APPIDREGFLAGS_IUSERVER_ACTIVATE_IN_CLIENT_SESSION_ONLY = 0x20
APPIDREGFLAGS_RESERVED1 = 0x40
APPIDREGFLAGS_RESERVED2 = 0x80
APPIDREGFLAGS_RESERVED3 = 0x100
APPIDREGFLAGS_RESERVED4 = 0x200
APPIDREGFLAGS_RESERVED5 = 0x400
APPIDREGFLAGS_AAA_NO_IMPLICIT_ACTIVATE_AS_IU = 0x800
APPIDREGFLAGS_RESERVED7 = 0x1000
APPIDREGFLAGS_RESERVED8 = 0x2000
DCOMSCM_ACTIVATION_USE_ALL_AUTHNSERVICES = 0x1
DCOMSCM_ACTIVATION_DISALLOW_UNSECURE_CALL = 0x2
DCOMSCM_RESOLVE_USE_ALL_AUTHNSERVICES = 0x4
DCOMSCM_RESOLVE_DISALLOW_UNSECURE_CALL = 0x8
DCOMSCM_PING_USE_MID_AUTHNSERVICE = 0x10
DCOMSCM_PING_DISALLOW_UNSECURE_CALL = 0x20


class tagCLSCTX(ENUM):
    CLSCTX_INPROC_SERVER = 0x1
    CLSCTX_INPROC_HANDLER = 0x2
    CLSCTX_LOCAL_SERVER = 0x4
    CLSCTX_INPROC_SERVER16 = 0x8
    CLSCTX_REMOTE_SERVER = 0x10
    CLSCTX_INPROC_HANDLER16 = 0x20
    CLSCTX_RESERVED1 = 0x40
    CLSCTX_RESERVED2 = 0x80
    CLSCTX_RESERVED3 = 0x100
    CLSCTX_RESERVED4 = 0x200
    CLSCTX_NO_CODE_DOWNLOAD = 0x400
    CLSCTX_RESERVED5 = 0x800
    CLSCTX_NO_CUSTOM_MARSHAL = 0x1000
    CLSCTX_ENABLE_CODE_DOWNLOAD = 0x2000
    CLSCTX_NO_FAILURE_LOG = 0x4000
    CLSCTX_DISABLE_AAA = 0x8000
    CLSCTX_ENABLE_AAA = 0x10000
    CLSCTX_FROM_DEFAULT_CONTEXT = 0x20000
    CLSCTX_ACTIVATE_X86_SERVER = 0x40000
    CLSCTX_ACTIVATE_32_BIT_SERVER = CLSCTX_ACTIVATE_X86_SERVER
    CLSCTX_ACTIVATE_64_BIT_SERVER = 0x80000
    CLSCTX_ENABLE_CLOAKING = 0x100000
    CLSCTX_APPCONTAINER = 0x400000
    CLSCTX_ACTIVATE_AAA_AS_IU = 0x800000
    CLSCTX_RESERVED6 = 0x1000000
    CLSCTX_ACTIVATE_ARM32_SERVER = 0x2000000
    CLSCTX_PS_DLL = 0x80000000


CLSCTX = tagCLSCTX

CLSCTX_INPROC_SERVER = CLSCTX.CLSCTX_INPROC_SERVER
CLSCTX_INPROC_HANDLER = CLSCTX.CLSCTX_INPROC_HANDLER
CLSCTX_LOCAL_SERVER = CLSCTX.CLSCTX_LOCAL_SERVER
CLSCTX_INPROC_SERVER16 = CLSCTX.CLSCTX_INPROC_SERVER16
CLSCTX_REMOTE_SERVER = CLSCTX.CLSCTX_REMOTE_SERVER
CLSCTX_NO_CODE_DOWNLOAD = CLSCTX.CLSCTX_NO_CODE_DOWNLOAD
CLSCTX_NO_CUSTOM_MARSHAL = CLSCTX.CLSCTX_NO_CUSTOM_MARSHAL
CLSCTX_ENABLE_CODE_DOWNLOAD = CLSCTX.CLSCTX_ENABLE_CODE_DOWNLOAD
CLSCTX_NO_FAILURE_LOG = CLSCTX.CLSCTX_NO_FAILURE_LOG
CLSCTX_DISABLE_AAA = CLSCTX.CLSCTX_DISABLE_AAA
CLSCTX_ENABLE_AAA = CLSCTX.CLSCTX_ENABLE_AAA
CLSCTX_FROM_DEFAULT_CONTEXT = CLSCTX.CLSCTX_FROM_DEFAULT_CONTEXT
CLSCTX_ACTIVATE_X86_SERVER = CLSCTX.CLSCTX_ACTIVATE_X86_SERVER
CLSCTX_ACTIVATE_64_BIT_SERVER = CLSCTX.CLSCTX_ACTIVATE_64_BIT_SERVER
CLSCTX_ENABLE_CLOAKING = CLSCTX.CLSCTX_ENABLE_CLOAKING
CLSCTX_APPCONTAINER = CLSCTX.CLSCTX_APPCONTAINER
CLSCTX_ACTIVATE_AAA_AS_IU = CLSCTX.CLSCTX_ACTIVATE_AAA_AS_IU
CLSCTX_RESERVED6 = CLSCTX.CLSCTX_RESERVED6
CLSCTX_ACTIVATE_ARM32_SERVER = CLSCTX.CLSCTX_ACTIVATE_ARM32_SERVER
CLSCTX_PS_DLL = CLSCTX.CLSCTX_PS_DLL


CLSCTX_VALID_MASK = (
     CLSCTX_INPROC_SERVER |
     CLSCTX_INPROC_HANDLER |
     CLSCTX_LOCAL_SERVER |
     CLSCTX_INPROC_SERVER16 |
     CLSCTX_REMOTE_SERVER |
     CLSCTX_NO_CODE_DOWNLOAD |
     CLSCTX_NO_CUSTOM_MARSHAL |
     CLSCTX_ENABLE_CODE_DOWNLOAD |
     CLSCTX_NO_FAILURE_LOG |
     CLSCTX_DISABLE_AAA |
     CLSCTX_ENABLE_AAA |
     CLSCTX_FROM_DEFAULT_CONTEXT |
     CLSCTX_ACTIVATE_X86_SERVER |
     CLSCTX_ACTIVATE_64_BIT_SERVER |
     CLSCTX_ENABLE_CLOAKING |
     CLSCTX_APPCONTAINER |
     CLSCTX_ACTIVATE_AAA_AS_IU |
     CLSCTX_RESERVED6 |
     CLSCTX_ACTIVATE_ARM32_SERVER |
     CLSCTX_PS_DLL
)


class tagMSHLFLAGS(ENUM):
    MSHLFLAGS_NORMAL = 0
    MSHLFLAGS_TABLESTRONG = 1
    MSHLFLAGS_TABLEWEAK = 2
    MSHLFLAGS_NOPING = 4
    MSHLFLAGS_RESERVED1 = 8
    MSHLFLAGS_RESERVED2 = 16
    MSHLFLAGS_RESERVED3 = 32
    MSHLFLAGS_RESERVED4 = 64


MSHLFLAGS = tagMSHLFLAGS


class tagMSHCTX(ENUM):
    MSHCTX_LOCAL = 0
    MSHCTX_NOSHAREDMEM = 1
    MSHCTX_DIFFERENTMACHINE = 2
    MSHCTX_INPROC = 3
    MSHCTX_CROSSCTX = 4
    MSHCTX_RESERVED1 = 5


MSHCTX = tagMSHCTX


class _BYTE_BLOB(ctypes.Structure):
    _fields_ = [
        ('clSize', ULONG),
        ('abData', BYTE * 1),
    ]


BYTE_BLOB = _BYTE_BLOB
UP_BYTE_BLOB = POINTER(_BYTE_BLOB)


class _WORD_BLOB(ctypes.Structure):
    _fields_ = [
        ('clSize', ULONG),
        ('SHORT asData', UINT * 1),
    ]


WORD_BLOB = _WORD_BLOB
UP_WORD_BLOB = POINTER(_WORD_BLOB)


class _DWORD_BLOB(ctypes.Structure):
    _fields_ = [
        ('clSize', ULONG),
        ('alData', ULONG * 1),
    ]


DWORD_BLOB = _DWORD_BLOB
UP_DWORD_BLOB = POINTER(_DWORD_BLOB)


class _FLAGGED_BYTE_BLOB(ctypes.Structure):
    _fields_ = [
        ('fFlags', ULONG),
        ('clSize', ULONG),
        ('abData', BYTE * 1),
    ]


FLAGGED_BYTE_BLOB = _FLAGGED_BYTE_BLOB
UP_FLAGGED_BYTE_BLOB = POINTER(_FLAGGED_BYTE_BLOB)


class _FLAGGED_WORD_BLOB(ctypes.Structure):
    _fields_ = [
        ('fFlags', ULONG),
        ('clSize', ULONG),
        ('SHORT asData', UINT * 1),
    ]


FLAGGED_WORD_BLOB = _FLAGGED_WORD_BLOB
UP_FLAGGED_WORD_BLOB = POINTER(FLAGGED_WORD_BLOB)


class _BYTE_SIZEDARR(ctypes.Structure):
    _fields_ = [
        ('clSize', ULONG),
        ('pData', POINTER(BYTE)),
    ]


BYTE_SIZEDARR = _BYTE_SIZEDARR


class _SHORT_SIZEDARR(ctypes.Structure):
    _fields_ = [
        ('clSize', ULONG),
        ('pData', POINTER(UINT)),
    ]


WORD_SIZEDARR = _SHORT_SIZEDARR


class _LONG_SIZEDARR(ctypes.Structure):
    _fields_ = [
        ('clSize', ULONG),
        ('pData', POINTER(ULONG)),
    ]


DWORD_SIZEDARR = _LONG_SIZEDARR


class _HYPER_SIZEDARR(ctypes.Structure):
    _fields_ = [
        ('clSize', ULONG),
        ('pData', POINTER(VOID)), # hyper = VOID??
    ]


HYPER_SIZEDARR = _HYPER_SIZEDARR


class _SHORT_SIZEDARR(ctypes.Structure):
    _fields_ = [
        ('clSize', ULONG),
        ('pData', POINTER(USHORT)),
    ]


SHORT_SIZEDARR = _SHORT_SIZEDARR


class _LONG_SIZEDARR(ctypes.Structure):
    _fields_ = [
        ('clSize', ULONG),
        ('pData', POINTER(ULONG)),
    ]


LONG_SIZEDARR = _LONG_SIZEDARR



class tagBLOB(ctypes.Structure):
    _fields_ = [
        ('cbSize', ULONG),
        ('pBlobData', POINTER(BYTE)),
    ]


BLOB = tagBLOB
LPBLOB = POINTER(tagBLOB)


class _SID_IDENTIFIER_AUTHORITY(ctypes.Structure):
    _fields_ = [
        ('Value', UCHAR * 6),
    ]


SID_IDENTIFIER_AUTHORITY = _SID_IDENTIFIER_AUTHORITY
PSID_IDENTIFIER_AUTHORITY = POINTER(_SID_IDENTIFIER_AUTHORITY)


class _SID(ctypes.Structure):
    _fields_ = [
        ('Revision', BYTE),
        ('SubAuthorityCount', BYTE),
        ('IdentifierAuthority', SID_IDENTIFIER_AUTHORITY),
        ('SubAuthority', ULONG * 1),
    ]


SID = _SID
PISID = POINTER(_SID)


class _SID_AND_ATTRIBUTES(ctypes.Structure):
    _fields_ = [
        ('Sid', POINTER(SID)),
        ('Attributes', DWORD),
    ]


SID_AND_ATTRIBUTES = _SID_AND_ATTRIBUTES
PSID_AND_ATTRIBUTES = POINTER(_SID_AND_ATTRIBUTES)


__all__ = (
    'DCOMSCM_PING_USE_MID_AUTHNSERVICE', 'APPIDREGFLAGS_RESERVED8', 'tagBLOB',
    'APPIDREGFLAGS_ACTIVATE_IUSERVER_INDESKTOP', 'APPIDREGFLAGS_RESERVED3',
    'DCOMSCM_RESOLVE_USE_ALL_AUTHNSERVICES', 'APPIDREGFLAGS_RESERVED2', 'SID',
    'DCOMSCM_PING_DISALLOW_UNSECURE_CALL', 'APPIDREGFLAGS_RESERVED1', 'ACL',
    'APPIDREGFLAGS_IUSERVER_UNMODIFIED_LOGON_TOKEN', 'CLSCTX_VALID_MASK',
    'APPIDREGFLAGS_RESERVED7', 'APPIDREGFLAGS_RESERVED5', 'tagCLSCTX', 'PSID',
    'APPIDREGFLAGS_RESERVED4', 'DCOMSCM_RESOLVE_DISALLOW_UNSECURE_CALL',
    'APPIDREGFLAGS_SECURE_SERVER_PROCESS_SD_AND_BIND', 'tagMSHLFLAGS', 'PACL',
    'DCOMSCM_ACTIVATION_USE_ALL_AUTHNSERVICES', 'ROTREGFLAGS_ALLOWANYCLIENT',
    'APPIDREGFLAGS_AAA_NO_IMPLICIT_ACTIVATE_AS_IU', 'tagMSHCTX', 'tagMEMCTX',
    'DCOMSCM_ACTIVATION_DISALLOW_UNSECURE_CALL', 'FLAGGED_BYTE_BLOB', 'SCODE',
    'APPIDREGFLAGS_IUSERVER_ACTIVATE_IN_CLIENT_SESSION_ONLY', 'OBJECTID',
    'APPIDREGFLAGS_IUSERVER_SELF_SID_IN_LAUNCH_PERMISSION', 'COAUTHIDENTITY',
    'APPIDREGFLAGS_ISSUE_ACTIVATION_RPC_AT_IDENTIFY', 'SECURITY_DESCRIPTOR',
    'SECURITY_ATTRIBUTES', 'WORD_BLOB', 'COAUTHINFO', 'BYTE_SIZEDARR',
    'SYSTEMTIME', 'ULARGE_INTEGER', 'HYPER_SIZEDARR', 'FILETIME', 'OLECHAR',
    'SID_IDENTIFIER_AUTHORITY', 'SID_AND_ATTRIBUTES', 'LARGE_INTEGER',
    'UP_FLAGGED_BYTE_BLOB', 'PSCODE', 'PSECURITY_DESCRIPTOR_CONTROL',
    'SECURITY_DESCRIPTOR_CONTROL', 'UP_FLAGGED_WORD_BLOB', 'UP_BYTE_BLOB',
    'UP_WORD_BLOB', 'UP_DWORD_BLOB', 'FLAGGED_WORD_BLOB', 'DWORD_BLOB',
    'BYTE_BLOB', 'PFILETIME', 'LPFILETIME',
)
