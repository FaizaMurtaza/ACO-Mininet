#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call


def myNetwork():

    net = Mininet(topo=None,
                  build=False,
                  ipBase='10.0.0.0/8', autoStaticArp=False)

    info('*** Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           ip='127.0.0.1',
                           port=6633)

    info('*** Add switches\n')
    Vancouver = net.addSwitch('sw1', cls=OVSKernelSwitch)
    Seatlle = net.addSwitch('sw2', cls=OVSKernelSwitch)
    Portland = net.addSwitch('sw3', cls=OVSKernelSwitch)
    Sunnyvale = net.addSwitch('sw4', cls=OVSKernelSwitch)
    Tacoma = net.addSwitch('sw5', cls=OVSKernelSwitch)
    Saltlakecity = net.addSwitch('sw6', cls=OVSKernelSwitch)
    Losangeles = net.addSwitch('sw7', cls=OVSKernelSwitch)
    Minneapois = net.addSwitch('sw8', cls=OVSKernelSwitch)
    Denver = net.addSwitch('sw9', cls=OVSKernelSwitch)
    Cheyenne = net.addSwitch('sw10', cls=OVSKernelSwitch)
    Tulsa = net.addSwitch('sw11', cls=OVSKernelSwitch)
    Phoenix = net.addSwitch('sw12', cls=OVSKernelSwitch)
    Chicago = net.addSwitch('sw13', cls=OVSKernelSwitch)
    Columbia = net.addSwitch('sw14', cls=OVSKernelSwitch)
    STlouis = net.addSwitch('sw15', cls=OVSKernelSwitch)
    Ashburn = net.addSwitch('sw16', cls=OVSKernelSwitch)
    Jackson = net.addSwitch('sw17', cls=OVSKernelSwitch)
    Router37 = net.addSwitch('sw18', cls=OVSKernelSwitch)
    Elpaso = net.addSwitch('sw19', cls=OVSKernelSwitch)
    Atlanta = net.addSwitch('sw20', cls=OVSKernelSwitch)
    Houston = net.addSwitch('sw21', cls=OVSKernelSwitch)
    Jacksonville = net.addSwitch('sw22', cls=OVSKernelSwitch)
    Miami = net.addSwitch('sw23', cls=OVSKernelSwitch)
    Cleverland = net.addSwitch('sw24', cls=OVSKernelSwitch)
    Pittsburgh = net.addSwitch('sw25', cls=OVSKernelSwitch)
    Raleigh = net.addSwitch('sw26', cls=OVSKernelSwitch)
    Washingtondc = net.addSwitch('sw27', cls=OVSKernelSwitch)
    Newyorkcity = net.addSwitch('sw28', cls=OVSKernelSwitch)
    Boston = net.addSwitch('sw29', cls=OVSKernelSwitch)
    Albany = net.addSwitch('sw30', cls=OVSKernelSwitch)

    info('*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.1.0.1',
                     mac='00:00:00:00:00:01', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.1.0.2',
                     mac='00:00:00:00:00:02', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.1.0.3',
                     mac='00:00:00:00:00:03', defaultRoute=None)
    h4 = net.addHost('h3', cls=Host, ip='10.1.0.4',
                     mac='00:00:00:00:00:04', defaultRoute=None)
    h5 = net.addHost('h3', cls=Host, ip='10.1.0.5',
                     mac='00:00:00:00:00:05', defaultRoute=None)

    # Chicago
    hub1 = net.addHost('s1', cls=Host, ip='10.0.0.1',
                       mac='00:00:00:00:00:11', defaultRoute=None)
    hub2 = net.addHost('s2', cls=Host, ip='10.0.0.2',
                       mac='00:00:00:00:00:12', defaultRoute=None)
    hub3 = net.addHost('s3', cls=Host, ip='10.0.0.3',
                       mac='00:00:00:00:00:13', defaultRoute=None)
    hub4 = net.addHost('s4', cls=Host, ip='10.0.0.4',
                       mac='00:00:00:00:00:14', defaultRoute=None)

    info('*** Add links\n')

    # linked hosts with switch
    net.addLink(Vancouver, h2)
    net.addLink(Sunnyvale, h1)
    net.addLink(Chicago, h4)
    net.addLink(Phoenix, h3)
    net.addLink(Boston, h5)

    # Linked between Switches
    net.addLink(Tacoma, Minneapois)
    net.addLink(Minneapois, Chicago)
    net.addLink(Chicago, Cleverland)
    net.addLink(Cleverland, Albany)
    net.addLink(Chicago, Columbia)
    net.addLink(Columbia, STlouis)
    net.addLink(STlouis, Ashburn)
    net.addLink(Ashburn, Jackson)
    net.addLink(Jackson, Router37)
    net.addLink(Router37, Elpaso)
    net.addLink(Ashburn, Atlanta)
    net.addLink(Atlanta, Jacksonville)
    net.addLink(Jacksonville, Miami)
    net.addLink(Jacksonville, Houston)
    net.addLink(Houston, Elpaso)
    net.addLink(Seatlle, Portland)
    net.addLink(Portland, Sunnyvale)
    net.addLink(Sunnyvale, Saltlakecity)
    net.addLink(Sunnyvale, Losangeles)
    net.addLink(Saltlakecity, Denver)
    net.addLink(Denver, Cheyenne)
    net.addLink(Elpaso, Phoenix)
    net.addLink(Phoenix, Tulsa)
    net.addLink(Cleverland, Pittsburgh)
    net.addLink(Pittsburgh, Washingtondc)
    net.addLink(Washingtondc, Raleigh)
    net.addLink(Washingtondc, Newyorkcity)
    net.addLink(Newyorkcity, Boston)
    net.addLink(Atlanta, Raleigh)

    # links between switch and Controller
    # HUB1
    net.addLink(hub1, Vancouver)
    net.addLink(hub1, Seatlle)
    net.addLink(hub1, Tacoma)

    # HUB2
    net.addLink(hub2, Losangeles)
    net.addLink(hub2, Phoenix)
    net.addLink(hub2, Cheyenne)

    # HUB3
    net.addLink(hub3, Tulsa)
    net.addLink(hub3, Denver)
    net.addLink(hub3, Chicago)

    # HUB4

    net.addLink(hub4, Albany)
    net.addLink(hub4, Boston)

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches\n')
    net.get('sw1').start([c0])
    net.get('sw2').start([c0])
    net.get('sw3').start([c0])
    net.get('sw4').start([c0])
    net.get('sw5').start([c0])
    net.get('sw6').start([c0])
    net.get('sw7').start([c0])
    net.get('sw8').start([c0])
    net.get('sw9').start([c0])
    net.get('sw10').start([c0])
    net.get('sw11').start([c0])
    net.get('sw12').start([c0])
    net.get('sw13').start([c0])
    net.get('sw14').start([c0])
    net.get('sw15').start([c0])
    net.get('sw16').start([c0])
    net.get('sw17').start([c0])
    net.get('sw18').start([c0])
    net.get('sw19').start([c0])
    net.get('sw20').start([c0])
    net.get('sw21').start([c0])
    net.get('sw22').start([c0])
    net.get('sw23').start([c0])
    net.get('sw24').start([c0])
    net.get('sw25').start([c0])
    net.get('sw26').start([c0])
    net.get('sw27').start([c0])
    net.get('sw28').start([c0])
    net.get('sw29').start([c0])
    net.get('sw30').start([c0])

    info('*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()
