from scapy.all import *


    
'''A script to generate packets to destination 10.0.0.9, using the source ip of the sending node using UDP
you can run this script from any node you want'''

        
    
def generatePackets():
    #for i in range(1,100):
    #for i in range(1,100):
    x=IP(dst='10.0.0.2')/ICMP()

    send(x*20)
    
 
if __name__ == '__main__':
    generatePackets()