"""
Created on Wed April 23 01:10:55 2017
@author: vicz
"""
print '''
 +-+-+ +-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+-+                                           
 |I|P| |2| |H|o|s|t| |C|o|n|v|e|r|t|e|r|                                           
 +-+-+ +-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+                                           
           |b|y| |v|i|c|z|                                                         
           +-+-+ +-+-+-+-+                   
'''

import socket

ips=open('ip.txt').readlines()

for ip in ips:
    try:
      print ip.strip(),socket.gethostbyaddr(ip.strip())
    except:
      print "Unsuccesfull"
