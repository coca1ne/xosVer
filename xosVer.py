#!/usr/bin/python
#coding=utf-8
#
#	xosVer
#

__version__ = '2.0.1 (http://Her0in.org)'
__author__  = 'Coca1ne'

__doc__ = """
xosVer 

 by Her0in Team

https://github.com/Coca1ne/xosVer

"""
import os,sys,socket,binascii,subprocess,re

from optparse import OptionError
from optparse import OptionParser


payload = {
    "SMB_CMD_NEGOTIATE":("\x00\x00\x00\x85\xff\x53\x4d\x42\x72\x00\x00\x00\x00\x18\x53\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfe\x00\x00\x00\x00\x00\x62\x00\x02\x50\x43\x20\x4e\x45\x54\x57\x4f\x52\x4b\x20\x50\x52\x4f\x47\x52\x41\x4d\x20\x31\x2e\x30\x00\x02\x4c\x41\x4e\x4d\x41\x4e\x31\x2e\x30\x00\x02\x57\x69\x6e\x64\x6f\x77\x73\x20\x66\x6f\x72\x20\x57\x6f\x72\x6b\x67\x72\x6f\x75\x70\x73\x20\x33\x2e\x31\x61\x00\x02\x4c\x4d\x31\x2e\x32\x58\x30\x30\x32\x00\x02\x4c\x41\x4e\x4d\x41\x4e\x32\x2e\x31\x00\x02\x4e\x54\x20\x4c\x4d\x20\x30\x2e\x31\x32\x00"),
    "SMB_CMD_SESSION_SETUP_ANDX":("\x00\x00\x00\xec\xff\x53\x4d\x42\x73\x00\x00\x00\x00\x18\x07\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfe\x00\x00\x40\x00\x0c\xff\x00\xec\x00\x04\x11\x32\x00\x00\x00\x00\x00\x00\x00\x4a\x00\x00\x00\x00\x00\xd4\x00\x00\xa0\xb1\x00\x60\x48\x06\x06\x2b\x06\x01\x05\x05\x02\xa0\x3e\x30\x3c\xa0\x0e\x30\x0c\x06\x0a\x2b\x06\x01\x04\x01\x82\x37\x02\x02\x0a\xa2\x2a\x04\x28\x4e\x54\x4c\x4d\x53\x53\x50\x00\x01\x00\x00\x00\x97\x82\x08\xe2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x01\x28\x0a\x00\x00\x00\x0f\x00\x57\x00\x69\x00\x6e\x00\x64\x00\x6f\x00\x77\x00\x73\x00\x20\x00\x32\x00\x30\x00\x30\x00\x32\x00\x20\x00\x53\x00\x65\x00\x72\x00\x76\x00\x69\x00\x63\x00\x65\x00\x20\x00\x50\x00\x61\x00\x63\x00\x6b\x00\x20\x00\x32\x00\x20\x00\x32\x00\x36\x00\x30\x00\x30\x00\x00\x00\x57\x00\x69\x00\x6e\x00\x64\x00\x6f\x00\x77\x00\x73\x00\x20\x00\x32\x00\x30\x00\x30\x00\x32\x00\x20\x00\x35\x00\x2e\x00\x31\x00\x00\x00\x00\x00"),
    "SMB_CMD_SESSION_SETUP_ANDX_WITH_NTLMSSP":("\x00\x00\x01\xc7\xff\x53\x4d\x42\x73\x00\x00\x00\x00\x18\x01\x28\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x5a\xde\x00\x08\x29\x94\x0c\xff\x00\x00\x00\xdf\xff\x02\x00\x01\x00\x00\x00\x00\x00\x69\x01\x00\x00\x00\x00\x5c\xd0\x00\x80\x8c\x01\xa1\x82\x01\x65\x30\x82\x01\x61\xa2\x82\x01\x5d\x04\x82\x01\x59\x4e\x54\x4c\x4d\x53\x53\x50\x00\x03\x00\x00\x00\x18\x00\x18\x00\x40\x00\x00\x00\xce\x00\xce\x00\x58\x00\x00\x00\x12\x00\x12\x00\x26\x01\x00\x00\x00\x00\x00\x00\x38\x01\x00\x00\x20\x00\x20\x00\x38\x01\x00\x00\x00\x00\x00\x00\x58\x01\x00\x00\x05\x02\x88\xa2\xee\xf0\xe5\x28\x7b\xa2\x82\xff\x1e\xa3\xc6\x6f\xe5\x6a\x93\x4b\xa4\xc4\x6d\xaa\x02\xf1\x91\x53\xc2\x46\x0c\x00\x84\x86\x6e\xa4\x12\xef\x94\xcf\x7e\xe9\x1b\x3e\x01\x01\x00\x00\x00\x00\x00\x00\x71\x42\x58\x8f\xc9\xd0\xd0\x01\xa4\xc4\x6d\xaa\x02\xf1\x91\x53\x00\x00\x00\x00\x02\x00\x16\x00\x53\x00\x55\x00\x52\x00\x46\x00\x41\x00\x43\x00\x45\x00\x50\x00\x52\x00\x4f\x00\x33\x00\x01\x00\x16\x00\x53\x00\x55\x00\x52\x00\x46\x00\x41\x00\x43\x00\x45\x00\x50\x00\x52\x00\x4f\x00\x33\x00\x04\x00\x16\x00\x53\x00\x75\x00\x72\x00\x66\x00\x61\x00\x63\x00\x65\x00\x50\x00\x72\x00\x6f\x00\x33\x00\x03\x00\x16\x00\x53\x00\x75\x00\x72\x00\x66\x00\x61\x00\x63\x00\x65\x00\x50\x00\x72\x00\x6f\x00\x33\x00\x07\x00\x08\x00\x71\x42\x58\x8f\xc9\xd0\xd0\x01\x09\x00\x22\x00\x63\x00\x69\x00\x66\x00\x73\x00\x2f\x00\x31\x00\x39\x00\x32\x00\x2e\x00\x31\x00\x36\x00\x38\x00\x2e\x00\x31\x00\x36\x00\x2e\x00\x31\x00\x00\x00\x00\x00\x00\x00\x00\x00\x57\x00\x4f\x00\x52\x00\x4b\x00\x47\x00\x52\x00\x4f\x00\x55\x00\x50\x00\x45\x00\x79\x00\x50\x00\x44\x00\x31\x00\x77\x00\x56\x00\x65\x00\x69\x00\x34\x00\x30\x00\x59\x00\x5a\x00\x65\x00\x6a\x00\x76\x00\x00\x57\x69\x6e\x64\x6f\x77\x73\x20\x32\x30\x30\x30\x20\x32\x31\x39\x35\x00\x57\x69\x6e\x64\x6f\x77\x73\x20\x32\x30\x30\x30\x20\x35\x2e\x30\x00"),
    "SMB_CMD_SESSION_SETUP_ANDX_NO_NTLMSSP":("\x00\x00\x00\x6b\xff\x53\x4d\x42\x73\x00\x00\x00\x00\x18\x01\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x5a\xde\x00\x00\x29\x94\x0d\xff\x00\x00\x00\xdf\xff\x02\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00\x00\x2e\x00\x00\x57\x4f\x52\x4b\x47\x52\x4f\x55\x50\x00\x57\x69\x6e\x64\x6f\x77\x73\x20\x32\x30\x30\x30\x20\x32\x31\x39\x35\x00\x57\x69\x6e\x64\x6f\x77\x73\x20\x32\x30\x30\x30\x20\x35\x2e\x30\x00")}

def xosVer(ipAddr,timeout,IsSave):
    osInfo = []
    try:
        print ("%-30s %-30s" % ("IP:", ipAddr))
        if IsSave:fp = open(IsSave, 'a+')
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ipAddr, 445))
        s.sendall(payload["SMB_CMD_NEGOTIATE"])
        data = binascii.b2a_hex(s.recv(1024))
        
        s.sendall(payload["SMB_CMD_SESSION_SETUP_ANDX"])
        data = binascii.b2a_hex(s.recv(1024))
        osInfo.append(getHostInfo(data))
        s.sendall(payload["SMB_CMD_SESSION_SETUP_ANDX_WITH_NTLMSSP"])
        data = binascii.b2a_hex(s.recv(1024))
        
        s.sendall(payload["SMB_CMD_SESSION_SETUP_ANDX_NO_NTLMSSP"])
        data = binascii.b2a_hex(s.recv(1024))
        osInfo.append(getOSInfo(data))

        print ("%-30s %-30s" % ("NetBIOS Domain Name:", osInfo[0][0]))
        print ("%-30s %-30s" % ("NetBIOS Computer Name:", osInfo[0][1]))
        print ("%-30s %-30s" % ("DNS Domain Name:", osInfo[0][2]))
        print ("%-30s %-30s" % ("DNS Computer Name:", osInfo[0][3]))
        print ("%-30s %-30s" % ("DNS Tree Name:", osInfo[0][4]))
        print ("%-30s %-30s" % ("Native OS:", osInfo[1][0]))
        print ("%-30s %-30s" % ("Native LAN Manager:", osInfo[1][1]))
        print ("%-30s %-30s" % ("Primary Domain:", osInfo[1][2]))

        if IsSave:
            print >> fp, ("%-30s %-30s" % ("IP:", ipAddr))
            print >> fp, ("%-30s %-30s" % ("NetBIOS Domain Name:", osInfo[0][0]))
            print >> fp, ("%-30s %-30s" % ("NetBIOS Computer Name:", osInfo[0][1]))
            print >> fp, ("%-30s %-30s" % ("DNS Domain Name:", osInfo[0][2]))
            print >> fp, ("%-30s %-30s" % ("DNS Computer Name:", osInfo[0][3]))
            print >> fp, ("%-30s %-30s" % ("DNS Tree Name:", osInfo[0][4]))
            print >> fp, ("%-30s %-30s" % ("Native OS:", osInfo[1][0]))
            print >> fp, ("%-30s %-30s" % ("Native LAN Manager:", osInfo[1][1]))
            print >> fp, ("%-30s %-30s" % ("Primary Domain:", osInfo[1][2]))
            print >> fp, ("------------------------------------------------------")
    except Exception, e:
        print ("%-30s %-30s" % ("Error:", e))
        if IsSave:
            print >> fp, ("IP: %s  Error: %s" % (ipAddr, e))
            print >> fp, ("------------------------------------------------------")
    finally:
        s.close()
    if IsSave:fp.close()
    print ("------------------------------------------------------")
def getHostInfo(data):
    try:
        if not data.strip():
            raise
        net_bios_header_len = 4
        smb_header_len      = 32
        smb_cmd_ex_len      = 7
        
        iPos = (smb_header_len + net_bios_header_len + smb_cmd_ex_len) * 2

        blobHex = data[iPos:iPos + 4]
        if blobHex[2:] == "00":
            blobHex = blobHex[0:2]
        blob_len = int(blobHex, 16)
        iPos    += 8
        secBlob  = data[iPos:iPos + blob_len * 2]
        token    = secBlob[secBlob.find('4e544c4d53535000'):]
        
        iPos     = token.find('0000000000000000')
        iPos    += 16
        info     = token[iPos:]
        
        iLen     = int(info[:4].replace('00', ''), 16)
        offset   = int(info[8:12].replace('00', ''), 16)
        info     = token[offset * 2:]
        
        infos    = u""
        for i in xrange(0,len(info), 2):
            infos += r"\x" + info[i:i + 2]

        info    = infos.split(r"\x00\x00")
        info    = info[0].replace('00', '').replace(r'\x', '')        
        try:
            iPos    = 2
            iLen    = int(info[iPos:iPos + 2], 16)
            net_BIOS_domain     = binascii.a2b_hex(info[iPos + 2:iLen + iPos + 2])
        except Exception, e:
            net_BIOS_domain = "Unknown"
            
        try:
            iPos   += iLen + 4
            iLen    = int(info[iPos:iPos + 2], 16)
            net_BIOS_computer   = binascii.a2b_hex(info[iPos + 2:iLen + iPos + 2])
        except Exception, e:
            net_BIOS_computer = "Unknown"
            
        try:
            iPos    += iLen + 4
            iLen     = int(info[iPos:iPos + 2], 16)
            dns_domain   = binascii.a2b_hex(info[iPos + 2:iLen + iPos + 2])
        except Exception, e:
            dns_domain = "Unknown"

        try:        
            iPos    += iLen + 4
            iLen     = int(info[iPos:iPos + 2], 16)
            dns_computer   = binascii.a2b_hex(info[iPos + 2:iLen + iPos + 2])
        except Exception, e:
            dns_computer = "Unknown"
        
        try:
            iPos    += iLen + 4
            iLen     = int(info[iPos:iPos + 2], 16)
            dns_tree = binascii.a2b_hex(info[iPos + 2:iLen + iPos + 2])
        except Exception, e:
            dns_tree = "Unknown"
        return net_BIOS_domain, net_BIOS_computer, dns_domain, dns_computer, dns_tree
    except Exception, e:
        return "Unknown","Unknown","Unknown","Unknown","Unknown"

def getOSInfo(data):
    try:
        if not data.strip():
            raise
        info  = data[45 * 2:]
        infos = u""
        for i in xrange(0, len(info), 2):
                infos += r"\x" + info[i:i + 2]
        try:
            osOffset = infos.find(r"\x00") + 4
            os       = infos[:osOffset].replace("00", "").replace(r"\x", "")
            os       = binascii.a2b_hex(os)
        except Exception, e:
            print e
            os = "Unknown"
      
        try: 
            lmOffset = infos.find(r"\x00", osOffset) + 4 
            lm       = infos[osOffset:lmOffset].replace("00", "").replace(r"\x", "")
            lm = binascii.a2b_hex(lm)
        except:
            lm = "Unknown"

        try:
            domain   = binascii.a2b_hex(infos[lmOffset:].replace("00", "").replace(r"\x", ""))
        except:
            domain = "Unknown"
        return os, lm, domain
    except:
        return "Unknown","Unknown","Unknown"

def main():
    print (r"                             ")
    print (r"            \ \    / /       ")
    print (r"__  _____  __\ \  / /__ _ __ ")
    print (r"\ \/ / _ \/ __\ \/ / _ \ '__|")
    print (r" >  < (_) \__ \\  /  __/ |   ")
    print (r"/_/\_\___/|___/ \/ \___|_|   ")
    print (r"                             ")

    IS_WIN = subprocess.mswindows
    _      = os.path.normpath(sys.argv[0])
    usage  = "%s%s <options>" % ("python" if not IS_WIN else "", \
         "\"%s\"" % _ if " " in _ else _)
    print ("Version: {0}".format(__version__))
    parser = OptionParser(usage=usage)
    try:
        parser.add_option("--hh", dest="help",
                            action="store_true",
                            help="Show help message and exit")
        parser.add_option("-i", dest="ip",
                            help="Single IP scan  mode  (eg:192.168.1.11)")
        parser.add_option("-p", dest="ips",
                            help="Batch  IP scan  mode  (eg:192.168.1.10/20)")
        parser.add_option("-o", dest="output",
                            help="Save results to a file",
                            default = False)
        parser.add_option("--timeout", dest="timeout", type="int",
                           help="Seconds to wait before timeout connection "
                           "(default 2)", default = 2)
        
        args = []
        for arg in sys.argv:
            args.append(arg)
        (args, _) = parser.parse_args(args)
        if not any((args.ip, args.ips)):
            errMsg = "use -h for help"
            parser.error(errMsg)
        for i in xrange(len(sys.argv)):
            try:
                if sys.argv[i] == '-i':
                    reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
                    for ip in reip.findall(args.ip):ip				
                    xosVer(ip, args.timeout, args.output)
                elif sys.argv[i] == '-p':
                    reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])/\d{1,3}')
                    for ip in reip.findall(args.ips):ip
                    ip   = ip.split('/')
                    exIp = ip[0][:ip[0].rfind('.') + 1]
                    sIp  = int(ip[0][ip[0].rfind('.') + 1:], 10)
                    eIp  = int(ip[1], 10) + 1
                    for i in xrange(sIp, eIp):
                        xosVer(exIp + str(i), args.timeout, args.output)
            except Exception, e:
                    print ("\r\noption %s invalid value: %s" % (sys.argv[i], sys.argv[i + 1]))
                    print ("\r\nuse -h for help")
    except (OptionError,TypeError), e:
        parser.error(e)
    
if __name__ == "__main__":
        main()
