#PYTHON SCRIPT TO PING IP ADDRESSES
import subprocess
import ipaddress
from subprocess import Popen , PIPE
network = ipaddress.ip_network('192.168.218.64/26')
print(network)
print(network.hosts)
text_file = open("op.txt", "w")
for i in network.hosts():
    i=str(i)
    print(i)
    toping=Popen((['ping','-n','3',i]),stdout=PIPE)
    output=toping.communicate()[0]
    hostalive=toping.returncode
    if hostalive==0:
        text_file.write( str(i)+ "is reachable\n")
    else:
        text_file.write( str(i)+ "is unreachable\n")
text_file.close()


