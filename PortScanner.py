import socket;
import termcolor;


def scan(target, ports):
	print(termcolor.colored('\n' + ' Starting Scan for ' + str(target), 'green'));
	for port in range(1, ports):
		scan_port(target, port);


def scan_port(ipaddress, port):
	try:
		sock = socket.socket();
		sock.connect((ipaddress, port));
		print("[+] Port Opened " + str(port));
		sock.close();
	except:
		#print("[-] Port Closed " + str(port));
		pass;


targets = input("[*] Enter Targets To Scan (split them by ,): ");
ports = 1 + int(input("[*] Enter How Many Ports You Want to Scan: "));

if ',' in targets:
	print(termcolor.colored("[*] Scanning Multiple Targets", 'green'));
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports);
else:
	print(termcolor.colored("[*] Scanning the Target", 'green'));
	scan(targets, ports);
