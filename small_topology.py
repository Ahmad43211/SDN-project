from mininet.topo import Topo


class customSmall( Topo):
    #def __init__(self):
        #Topo.__init__(self)
     def build(self):
        s1= self.addSwitch( 's1')
        s2= self.addSwitch( 's2')
       
    
        
        hosts1 = [ self.addHost( 'h%d' % n ) for n in  range( 1, 3 ) ]

        hosts2 = [ self.addHost( 'h%d' % n ) for n in  range( 3, 5 ) ]
  
        
    
        for h in hosts1:
            self.addLink( s1, h )
        
        for h in hosts2:
            self.addLink( s2, h )

        
        #net.addLink(s7, s1)
        self.addLink( s1, s2 )
     
