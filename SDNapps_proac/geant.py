from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import Link, Intf, TCLink
import subprocess

def Test_topo():
    net = Mininet(controller=RemoteController,link=TCLink)

    info("*** Add Controller ***\n")
    net.addController("c0",controller=RemoteController,ip='192.168.72.22')

    info("*** Add Switch ***\n")
    s1 = net.addSwitch("s1")
    s2 = net.addSwitch("s2")
    s3 = net.addSwitch("s3")
    s4 = net.addSwitch("s4")
    s5 = net.addSwitch("s5")
    s6 = net.addSwitch("s6")
    s7 = net.addSwitch("s7")
    s8 = net.addSwitch("s8")
    s9 = net.addSwitch("s9")
    s10 = net.addSwitch("s10")
    s11 = net.addSwitch("s11")
    s12 = net.addSwitch("s12")
    s13 = net.addSwitch("s13")
    s14 = net.addSwitch("s14")
    s15 = net.addSwitch("s15")
    s16 = net.addSwitch("s16")
    s17 = net.addSwitch("s17")
    s18 = net.addSwitch("s18")
    s19 = net.addSwitch("s19")
    s20 = net.addSwitch("s20")
    s21 = net.addSwitch("s21")
    s22 = net.addSwitch("s22")
    s23 = net.addSwitch("s23")

    info("*** Add Host ***\n")
    h1 = net.addHost("h1",mac="00:00:00:00:00:01")
    h2 = net.addHost("h2",mac="00:00:00:00:00:02")
    h3 = net.addHost("h3",mac="00:00:00:00:00:03")
    h4 = net.addHost("h4",mac="00:00:00:00:00:04")
    h5 = net.addHost("h5",mac="00:00:00:00:00:05")
    h6 = net.addHost("h6",mac="00:00:00:00:00:06")
    h7 = net.addHost("h7",mac="00:00:00:00:00:07")
    h8 = net.addHost("h8",mac="00:00:00:00:00:08")
    h9 = net.addHost("h9",mac="00:00:00:00:00:09")
    h10 = net.addHost("h10",mac="00:00:00:00:00:10")
    h11 = net.addHost("h11",mac="00:00:00:00:00:11")
    h12 = net.addHost("h12",mac="00:00:00:00:00:12")
    h13 = net.addHost("h13",mac="00:00:00:00:00:13")
    h14 = net.addHost("h14",mac="00:00:00:00:00:14")
    h15 = net.addHost("h15",mac="00:00:00:00:00:15")
    h16 = net.addHost("h16",mac="00:00:00:00:00:16")
    h17 = net.addHost("h17",mac="00:00:00:00:00:17")
    h18 = net.addHost("h18",mac="00:00:00:00:00:18")
    h19 = net.addHost("h19",mac="00:00:00:00:00:19")
    h20 = net.addHost("h20",mac="00:00:00:00:00:20")
    h21 = net.addHost("h21",mac="00:00:00:00:00:21")
    h22 = net.addHost("h22",mac="00:00:00:00:00:22")
    h23 = net.addHost("h23",mac="00:00:00:00:00:23")

    info("*** Add Link ***\n")
    net.addLink(s1,h1)
    net.addLink(s2,h2)
    net.addLink(s3,h3)
    net.addLink(s4,h4)
    net.addLink(s5,h5)
    net.addLink(s6,h6)
    net.addLink(s7,h7)
    net.addLink(s8,h8)
    net.addLink(s9,h9)
    net.addLink(s10,h10)
    net.addLink(s11,h11)
    net.addLink(s12,h12)
    net.addLink(s13,h13)
    net.addLink(s14,h14)
    net.addLink(s15,h15)
    net.addLink(s16,h16)
    net.addLink(s17,h17)
    net.addLink(s18,h18)
    net.addLink(s19,h19)
    net.addLink(s20,h20)
    net.addLink(s21,h21)
    net.addLink(s22,h22)
    net.addLink(s23,h23)

    net.addLink(s1,s3,bw=100)
    net.addLink(s1,s7,bw=100)
    net.addLink(s1,s16,bw=100)
    net.addLink(s2,s4,bw=100)
    net.addLink(s2,s7,bw=100)
    net.addLink(s2,s12,bw=100)
    net.addLink(s2,s13,bw=100)
    net.addLink(s2,s18,bw=25)
    net.addLink(s2,s23,bw=25)
    net.addLink(s3,s10,bw=100)
    net.addLink(s3,s11,bw=25)
    net.addLink(s3,s14,bw=1.55)
    net.addLink(s3,s21,bw=100)
    net.addLink(s4,s16,bw=100)
    net.addLink(s5,s8,bw=25)
    net.addLink(s5,s16,bw=25)
    net.addLink(s6,s7,bw=1.55)
    net.addLink(s6,s19,bw=1.55)
    net.addLink(s7,s17,bw=100)
    net.addLink(s7,s19,bw=25)
    net.addLink(s7,s21,bw=100)
    net.addLink(s8,s9,bw=25)
    net.addLink(s9,s15,bw=25)
    net.addLink(s9,s16,bw=100)
    net.addLink(s10,s11,bw=25)
    net.addLink(s10,s12,bw=100)
    net.addLink(s10,s16,bw=100)
    net.addLink(s10,s17,bw=100)
    net.addLink(s12,s22,bw=100)
    net.addLink(s13,s14,bw=1.55)
    net.addLink(s13,s17,bw=100)
    net.addLink(s13,s19,bw=25)
    net.addLink(s15,s20,bw=25)
    net.addLink(s17,s20,bw=100)
    net.addLink(s17,s23,bw=25)
    net.addLink(s18,s21,bw=25)
    net.addLink(s20,s22,bw=25)


    info("*** Network Start ***\n")
    net.start()
    # CLI(net)
    # net.stop()
    return net
def generate(net):
    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')
    h5 = net.get('h5')
    h6 = net.get('h6')
    h7 = net.get('h7')
    h8 = net.get('h8')
    h9 = net.get('h9')
    h10 = net.get('h10')
    h11 = net.get('h11')
    h12 = net.get('h12')
    h13 = net.get('h13')
    h14 = net.get('h14')
    h15 = net.get('h15')
    h16 = net.get('h16')
    h17 = net.get('h17')
    h18 = net.get('h18')
    h19 = net.get('h19')
    h20 = net.get('h20')
    h21 = net.get('h21')
    h22 = net.get('h22')
    h23 = net.get('h23')

    #h1.cmd('ping 10.0.0.2 -c 1')
    h1.popen('ping 10.0.0.2 -c 1')
    h2.popen('ping 10.0.0.1 -c 1')
    h3.popen('ping 10.0.0.1 -c 1')
    h4.popen('ping 10.0.0.1 -c 1')
    h5.popen('ping 10.0.0.1 -c 1')
    h6.popen('ping 10.0.0.1 -c 1')
    h7.popen('ping 10.0.0.1 -c 1')
    h8.popen('ping 10.0.0.1 -c 1')
    h9.popen('ping 10.0.0.1 -c 1')
    h10.popen('ping 10.0.0.1 -c 1')
    h11.popen('ping 10.0.0.1 -c 1')
    h12.popen('ping 10.0.0.1 -c 1')
    h13.popen('ping 10.0.0.1 -c 1')
    h14.popen('ping 10.0.0.1 -c 1')
    h15.popen('ping 10.0.0.1 -c 1')
    h16.popen('ping 10.0.0.1 -c 1')
    h17.popen('ping 10.0.0.1 -c 1')
    h18.popen('ping 10.0.0.1 -c 1')
    h19.popen('ping 10.0.0.1 -c 1')
    h20.popen('ping 10.0.0.1 -c 1')
    h21.popen('ping 10.0.0.1 -c 1')
    h22.popen('ping 10.0.0.1 -c 1')
    h23.popen('ping 10.0.0.1 -c 1')

    print("################################################")

    h1.popen('sh 23nodos/TM-00/Servers/server_01.sh')
    h2.popen('sh 23nodos/TM-00/Servers/server_02.sh')
    h3.popen('sh 23nodos/TM-00/Servers/server_03.sh')
    h4.popen('sh 23nodos/TM-00/Servers/server_04.sh')
    h5.popen('sh 23nodos/TM-00/Servers/server_05.sh')
    h6.popen('sh 23nodos/TM-00/Servers/server_06.sh')
    h7.popen('sh 23nodos/TM-00/Servers/server_07.sh')
    h8.popen('sh 23nodos/TM-00/Servers/server_08.sh')
    h9.popen('sh 23nodos/TM-00/Servers/server_09.sh')
    h10.popen('sh 23nodos/TM-00/Servers/server_10.sh')
    h11.popen('sh 23nodos/TM-00/Servers/server_11.sh')
    h12.popen('sh 23nodos/TM-00/Servers/server_12.sh')
    h13.popen('sh 23nodos/TM-00/Servers/server_13.sh')
    h14.popen('sh 23nodos/TM-00/Servers/server_14.sh')
    h15.popen('sh 23nodos/TM-00/Servers/server_15.sh')
    h16.popen('sh 23nodos/TM-00/Servers/server_16.sh')
    h17.popen('sh 23nodos/TM-00/Servers/server_17.sh')
    h18.popen('sh 23nodos/TM-00/Servers/server_18.sh')
    h19.popen('sh 23nodos/TM-00/Servers/server_19.sh')
    h20.popen('sh 23nodos/TM-00/Servers/server_20.sh')
    h21.popen('sh 23nodos/TM-00/Servers/server_21.sh')
    h22.popen('sh 23nodos/TM-00/Servers/server_22.sh')
    h23.popen('sh 23nodos/TM-00/Servers/server_23.sh')

    h1.popen('sh 23nodos/TM-00/Clients/client_01.sh')
    h2.popen('sh 23nodos/TM-00/Clients/client_02.sh')
    h3.popen('sh 23nodos/TM-00/Clients/client_03.sh')
    h4.popen('sh 23nodos/TM-00/Clients/client_04.sh')
    h5.popen('sh 23nodos/TM-00/Clients/client_05.sh')
    h6.popen('sh 23nodos/TM-00/Clients/client_06.sh')
    h7.popen('sh 23nodos/TM-00/Clients/client_07.sh')
    h8.popen('sh 23nodos/TM-00/Clients/client_08.sh')
    h9.popen('sh 23nodos/TM-00/Clients/client_09.sh')
    h10.popen('sh 23nodos/TM-00/Clients/client_10.sh')
    h11.popen('sh 23nodos/TM-00/Clients/client_11.sh')
    h12.popen('sh 23nodos/TM-00/Clients/client_12.sh')
    h13.popen('sh 23nodos/TM-00/Clients/client_13.sh')
    h14.popen('sh 23nodos/TM-00/Clients/client_14.sh')
    h15.popen('sh 23nodos/TM-00/Clients/client_15.sh')
    h16.popen('sh 23nodos/TM-00/Clients/client_16.sh')
    h17.popen('sh 23nodos/TM-00/Clients/client_17.sh')
    h18.popen('sh 23nodos/TM-00/Clients/client_18.sh')
    h19.popen('sh 23nodos/TM-00/Clients/client_19.sh')
    h20.popen('sh 23nodos/TM-00/Clients/client_20.sh')
    h21.popen('sh 23nodos/TM-00/Clients/client_21.sh')
    h22.popen('sh 23nodos/TM-00/Clients/client_22.sh')
    h23.popen('sh 23nodos/TM-00/Clients/client_23.sh')



    #print(h1.cmd('ping 10.0.0.2 -s 1000 -c 1'))
    

if __name__ == "__main__":
    setLogLevel("info")
    net = Test_topo()

    while 1:
        input = raw_input('CLI/GEN/QUIT')
        if input.upper() == 'CLI':
            CLI(net)
        elif input.upper() == 'GEN':
            generate(net)
        elif input.upper() == 'QUIT':
            net.stop()
            break
