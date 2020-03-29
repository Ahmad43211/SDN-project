

from mininet.topo import Topo


class customTopology( Topo):
    #def __init__(self):
        #Topo.__init__(self)
     def build(self):
        s1= self.addSwitch( 's1')
        s2= self.addSwitch( 's2')
        s3= self.addSwitch( 's3')
        s4= self.addSwitch( 's4')
        s5= self.addSwitch( 's5')
        s6= self.addSwitch( 's6')
    
    
        hosts1 = [ self.addHost( 'h%d' % n ) for n in  range( 1, 5 ) ]

        hosts2 = [ self.addHost( 'h%d' % n ) for n in  range( 5, 9 ) ]
        hosts3 = [ self.addHost( 'h%d' % n ) for n in  range( 9, 13 ) ]
        hosts4 = [ self.addHost( 'h%d' % n ) for n in  range( 13, 17 ) ]
        hosts5 = [ self.addHost( 'h%d' % n ) for n in  range( 17, 21 ) ]
        hosts6 = [ self.addHost( 'h%d' % n ) for n in  range( 21, 25 ) ]
        
    
        for h in hosts1:
            self.addLink( s1, h )
        for h in hosts2:
            self.addLink( s2, h )
        for h in hosts3:
            self.addLink( s3, h )
        for h in hosts4:
            self.addLink( s4, h )
        for h in hosts5:
            self.addLink( s5, h )
        for h in hosts6:
            self.addLink( s6, h )
        
        #net.addLink(s7, s1)
        self.addLink( s1, s2 )
        self.addLink( s2, s3 )
        self.addLink( s3, s4 )
        self.addLink( s4, s5 )
        self.addLink( s5, s6)
