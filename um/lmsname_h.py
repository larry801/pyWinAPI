import ctypes
from pyWinAPI import *
from pyWinAPI.shared.wtypes_h import *
from pyWinAPI.shared.winapifamily_h import *
from pyWinAPI.shared.sdkddkver_h import *
from pyWinAPI.shared.guiddef_h import *


_LMSNAME_ = None

# /* + + BUILD Version: 0002 // Increment this if a change has global effects
# Copyright (c) 1991-1999 Microsoft Corporation Module Name: lmsname.h
# Abstract: This file contains service name strings. It is included by
# lmsvc.h. Environment: User Mode -Win32 --
if not defined(_LMSNAME_):
    _LMSNAME_ = VOID

    if _MSC_VER > 1000:
        pass
    # END IF

    from pyWinAPI.shared.winapifamily_h import * # NOQA

    if WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP):
        # Standard LAN Manager service names.
        SERVICE_WORKSTATION = TEXT("LanmanWorkstation")
        SERVICE_LM20_WORKSTATION = TEXT("WORKSTATION")
        WORKSTATION_DISPLAY_NAME = TEXT("Workstation")
        SERVICE_SERVER = TEXT("LanmanServer")
        SERVICE_LM20_SERVER = TEXT("SERVER")
        SERVER_DISPLAY_NAME = TEXT("Server")
        SERVICE_BROWSER = TEXT("BROWSER")
        SERVICE_LM20_BROWSER = SERVICE_BROWSER
        SERVICE_MESSENGER = TEXT("MESSENGER")
        SERVICE_LM20_MESSENGER = SERVICE_MESSENGER
        SERVICE_NETRUN = TEXT("NETRUN")
        SERVICE_LM20_NETRUN = SERVICE_NETRUN
        SERVICE_SPOOLER = TEXT("SPOOLER")
        SERVICE_LM20_SPOOLER = SERVICE_SPOOLER
        SERVICE_ALERTER = TEXT("ALERTER")
        SERVICE_LM20_ALERTER = SERVICE_ALERTER
        SERVICE_NETLOGON = TEXT("NETLOGON")
        SERVICE_LM20_NETLOGON = SERVICE_NETLOGON
        SERVICE_NETPOPUP = TEXT("NETPOPUP")
        SERVICE_LM20_NETPOPUP = SERVICE_NETPOPUP
        SERVICE_SQLSERVER = TEXT("SQLSERVER")
        SERVICE_LM20_SQLSERVER = SERVICE_SQLSERVER
        SERVICE_REPL = TEXT("REPLICATOR")
        SERVICE_LM20_REPL = SERVICE_REPL
        SERVICE_RIPL = TEXT("REMOTEBOOT")
        SERVICE_LM20_RIPL = SERVICE_RIPL
        SERVICE_TIMESOURCE = TEXT("TIMESOURCE")
        SERVICE_LM20_TIMESOURCE = SERVICE_TIMESOURCE
        SERVICE_AFP = TEXT("AFP")
        SERVICE_LM20_AFP = SERVICE_AFP
        SERVICE_UPS = TEXT("UPS")
        SERVICE_LM20_UPS = SERVICE_UPS
        SERVICE_XACTSRV = TEXT("XACTSRV")
        SERVICE_LM20_XACTSRV = SERVICE_XACTSRV
        SERVICE_TCPIP = TEXT("TCPIP")
        SERVICE_LM20_TCPIP = SERVICE_TCPIP
        SERVICE_NBT = TEXT("NBT")
        SERVICE_LM20_NBT = SERVICE_NBT
        SERVICE_LMHOSTS = TEXT("LMHOSTS")
        SERVICE_LM20_LMHOSTS = SERVICE_LMHOSTS
        SERVICE_TELNET = TEXT("Telnet")
        SERVICE_LM20_TELNET = SERVICE_TELNET
        SERVICE_SCHEDULE = TEXT("Schedule")
        SERVICE_LM20_SCHEDULE = SERVICE_SCHEDULE
        SERVICE_NTLMSSP = TEXT("NtLmSsp")
        SERVICE_DHCP = TEXT("DHCP")
        SERVICE_LM20_DHCP = SERVICE_DHCP
        SERVICE_NWSAP = TEXT("NwSapAgent")
        SERVICE_LM20_NWSAP = SERVICE_NWSAP
        NWSAP_DISPLAY_NAME = TEXT("NW Sap Agent")
        SERVICE_NWCS = TEXT("NWCWorkstation")
        SERVICE_DNS_CACHE = TEXT("DnsCache")
        SERVICE_W32TIME = TEXT("w32time")
        SERVCE_LM20_W32TIME = SERVICE_W32TIME
        SERVICE_KDC = TEXT("kdc")
        SERVICE_LM20_KDC = SERVICE_KDC
        SERVICE_RPCLOCATOR = TEXT("RPCLOCATOR")
        SERVICE_LM20_RPCLOCATOR = SERVICE_RPCLOCATOR
        SERVICE_TRKSVR = TEXT("TrkSvr")
        SERVICE_LM20_TRKSVR = SERVICE_TRKSVR
        SERVICE_TRKWKS = TEXT("TrkWks")
        SERVICE_LM20_TRKWKS = SERVICE_TRKWKS
        SERVICE_NTFRS = TEXT("NtFrs")
        SERVICE_LM20_NTFRS = SERVICE_NTFRS
        SERVICE_ISMSERV = TEXT("IsmServ")
        SERVICE_LM20_ISMSERV = SERVICE_ISMSERV
        SERVICE_NTDS = TEXT("NTDS")
        SERVICE_LM20_NTDS = SERVICE_NTDS
        SERVICE_ADWS = TEXT("ADWS")
        SERVICE_DSROLE = TEXT("DsRoleSvc")
        SERVICE_LM20_DSROLE = SERVICE_DSROLE
    # END IF  WINAPI_FAMILY_PARTITION(WINAPI_PARTITION_DESKTOP)
# END IF


