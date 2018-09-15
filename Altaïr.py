import argparse

import requests

import time

import sys

import json



G = '\033[92m'

Y = '\033[93m'

R = '\033[91m'

W = '\033[0m'





def anim():

	array = ['[]']

	for i in range(1, 61):

		text = ''

		for j in range(i):

			text = text + '#'

		array.append('[' + text + ']')



	return array





def loading():

	animation = anim()



	for i in range(1, 61):

		time.sleep(0.1)

		sys.stdout.write("\r" + "Loading : " + animation[i % len(animation)] + ' ' + str(int(round(i * 5 / 3))) + '%')

		sys.stdout.flush()





def banner():

	print("-----------------------------------------------------------------------")

	print(G + "	 .--. .-.  .-.        _      	")

	print(G + "	: .; :: : .' `.      :_;     	")

	print(G + "	:    :: : `. .'.--.  .-..--. 	")

	print(G + "	: :: :: :_ : :' .; ; : :: ..'	")

	print(G + "	:_;:_;`.__;:_;`.__,_;:_;:_;  " + W + "v1.0 \n")





def menu():

	print("Usage : This tool is a python script used to get information gathering .")

	print("------------------------------------------------------------------------\n")

	print('Options : ')

	print('	-w, --whois		[Domain/IP]	Domain/IP whois \n')

	print('	-d, --dns		[Domain]	DNS lookup and cloudflare detector\n')

	print('	-t, --transfer		[Domain]	Scan zone Transfer\n')

	print('	-s, --scan		[Domain/IP]	Scan Domain/IP ports\n')

	print('	-he, --header		[Domain/IP]	Website/IP Header\n')

	print('	-r, --robots		[Domain]	robots.txt Checker\n')

	print('	--reverse		[IP]		IP to Hostname\n')

	print('	-h , --help				Show documentation \n')





def whois(q):

	loading()

	r = requests.get('http://api.hackertarget.com/whois/?q=' + q)

	print('\n')

	print(r.text)





def dns(q):

	loading()

	r = requests.get('http://api.hackertarget.com/dnslookup/?q=' + q)

	print('\n')

	print(r.text + '\n')

	if 'cloudflare' in r.text:

		print(G + '[+] Cloudflare detected ! ')

	else:

		print(R + '[+] This site is not protected by cloudflare ! ')





def transfer(q):

	loading()

	r = requests.get('http://api.hackertarget.com/zonetransfer/?q=' + q)

	print('\n')

	print(r.text)





def scan(q):

	loading()

	r = requests.get('http://api.hackertarget.com/nmap/?q=' + q)

	print('\n')

	print(r.text)





def header(q):

	loading()

	r = requests.get('http://api.hackertarget.com/httpheaders/?q=' + q)

	print('\n')

	print(r.text)





def robots(domain):

	loading()

	url1 = requests.get('http://' + domain + '/robots.txt')

	url2 = requests.get(url1.url)

	if url2.status_code == 200:

		print('\n')

		print(url2.text)

	else:

		print('\n')

		print(G + "[+] robots.txt does not exist !")





def reverse(q):

	loading()

	r = requests.get('http://api.hackertarget.com/reversedns/?q=' + q)

	print('\n')

	print(r.text)





if __name__ == '__main__':



	banner()

	menu()



	parsing = argparse.ArgumentParser(description="This tool is a python script used to get information gathering .")



	parsing.add_argument('-w', '--whois', dest='whois', help='Domain/IP whois')

	parsing.add_argument('-d', '--dns', dest='dns', help="DNS lookup and cloudflare detector")

	parsing.add_argument('-t', '--transfer', dest='transfer', help="Scan zone Transfer")

	parsing.add_argument('-s', '--scan', dest='scan', help="Scan Domain/IP ports")

	parsing.add_argument('-he', '--header', dest='header', help="Website/IP Header")

	parsing.add_argument('-r', '--robots', dest='robots', help="robots.txt Checker")

	parsing.add_argument('--reverse', dest='reverse', help="IP to Hostname")

	args = parsing.parse_args()



	whois2 = args.whois

	dns2 = args.dns

	transfer2 = args.transfer

	scan2 = args.scan

	header2 = args.header

	robots2 = args.robots

	reverse2 = args.reverse



	if whois2 is not None:

		whois(whois2)

	elif dns2 is not None:

		dns(dns2)

	elif transfer2 is not None:

		transfer(transfer2)

	elif scan2 is not None:

		scan(scan2)

	elif header2 is not None:

		header(header2)

	elif robots2 is not None:

		robots(robots2)

	elif reverse2 is not None:

		reverse(reverse2)

	else:

		pass
