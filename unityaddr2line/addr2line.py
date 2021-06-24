import re
import os

a = """
libunity.0x2f65f4
libunity.0x2fb707
libunity.0x2f64fd
libunity.0x2e813f
libunity.0x2e83d5
libunity.0x301319
libunity.0x30152f
libunity.0x302781
libunity.0x2ff6d3
libunity.0x2ef2df
libunity.0x2ef405
libunity.0x647668
libunity.0x3009b7
libunity.0x2dd419
libunity.0x2dd491
libunity.0x40c5a1
libunity.0x40c4e5
libunity.0x40c48d
libunity.0x4032d5
libunity.0x4036db
libunity.0x403971
libunity.0xa5c3b
libunity.0x153c89
libunity.0x1537a1
libunity.0x1534eb
libunity.0x354bd7
libunity.0x3550a3
libunity.0x34b56d
libunity.0x34b589
libunity.0x34b71f
libunity.0x42476d
"""

temp = re.findall("libunity\.[0-9,a-z]*",a)

for i in range(len(temp)):
    temp[i] = re.sub("libunity\.","",temp[i])
# os.system("pwd")
os.system("unityaddr2line.sh " + " ".join(temp))
