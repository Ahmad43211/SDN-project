#!/usr/bin/python

from mininet.link import TCLink
from scapy.all import *
from mininet.log import setLogLevel, info

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import Controller,OVSKernelSwitch,RemoteController
from os import environ
import sys
sys.path.append("//home//ahmad//mininet//custom//my_network")
from small_topology import customSmall
POXDIR = environ[ 'HOME' ] + '/pox'



    
    

def topoglogyWithControllers():
    topo = customSmall()
    #remember here i can use c0 in controller=c0
    c0 = RemoteController( 'c0', ip="127.0.0.1" )
    #c2 = RemoteController( 'c2', port=5001 )

    net = Mininet( controller=c0,switch=OVSKernelSwitch,topo=topo)

    
    

    print(dict(net))
    print(net['s1'])
    

    net.start()
    #c0.start()
    #c1.start()
    #net['s1'].start( [  c0 ] )
    #net['s2'].start( [  c0 ] )
    h1=net['h1']
    #h2=net['h2']
    print(h1)
    h1.cmd('sudo python3 scapy_training.py &')
    h1.cmd('sudo python3 scapy_training.py &')

    #h2.cmd('sudo python3 scay_training.py &')

    #h1.cmd('sudo & python3 scay2_training.py')


    #net.pingAll()
        
    
    #this is the command responsible for opening the mininet command terminal
    CLI( net )
    

    info( "*** Stopping network\n" )
    net.stop()
topos = { 'mytopo': ( lambda: topoglogyWithControllers()) }