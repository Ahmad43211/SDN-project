from scapy.all import *
 

'''You can run this script from any node you want, and the source ip will apear as 10.0.0.1 
even if you send it from a node with a source ip of 10.0.0.2, it spoofs ip.
'''
        
    
def generatePackets():
    
    x=IP(src='10.0.0.1',dst='10.0.0.9')/UDP()


    send(x*10000)
    
 
if __name__ == '__main__':
    generatePackets()