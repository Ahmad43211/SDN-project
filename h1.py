from scapy.all import *


    
'''A script to generate packets to destination 10.0.0.9, using the source ip of the sending node using UDP
you can run this script from any node you want'''

        
    
def generatePackets():
    
    x=IP(dst='10.0.0.9')/UDP()
    send(x*1000)
    
 
if __name__ == '__main__':
    generatePackets()