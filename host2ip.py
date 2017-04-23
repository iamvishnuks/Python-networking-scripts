"""
Created on Wed April 23 01:10:55 2017
@author: vicz
"""
print '''
 +-+-+-+-+ +-+ +-+-+ +-+-+-+-+-+-+-+-+-+                                           
 |H|o|s|t| |2| |I|P| |C|o|n|v|e|r|t|e|r|                                           
 +-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+                                           
           |b|y| |v|i|c|z|                                                         
           +-+-+ +-+-+-+-+ 

'''
import socket

hostnames=open('host.txt').readlines()

for host in hostnames:
    try:
      print host.strip(),socket.gethostbyname(host.strip())
    except:
      print "Unsuccesfull"
