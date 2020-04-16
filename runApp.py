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
from customtopology import customTopology
POXDIR = environ[ 'HOME' ] + '/pox'



    
    

def topoglogyWithControllers():
    topo = customTopology()
    c0 = RemoteController( 'c0', port=5000 )
    c1 = RemoteController( 'c1', port=5001 )
    net = Mininet( topo=topo)

    
    

    print(dict(net))
    print(net['s1'])
    
    info( "*** Creating 2 controllers\n" )
    

    info( "*** Creating 6 switches\n" )
    
    
    info( "*** Creating 24 hosts\n" )
    

    info( "*** Starting network\n" )
    net.start()
    #c0.start()
    #c1.start()
    net['s1'].start( [  c0 ] )
    net['s2'].start( [  c0 ] )
    net['s3'].start( [ c0 ] )
    net['s4'].start( [ c1 ] )
    net['s5'].start( [ c1 ] )
    net['s6'].start( [ c1 ] )
    info( "*** Testing network\n" )
    net.pingAll()
        
    

    info( "*** Running CLI\n" )
    CLI( net )

    info( "*** Stopping network\n" )
    net.stop()
topos = { 'mytopo': ( lambda: topoglogyWithControllers()) }
