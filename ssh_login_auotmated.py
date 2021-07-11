#!/usr/bin/python3

import pexpect 

PROMPT = ['#', '>>', '>', '\$',]

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
		return
	child.sendline(password)
	child.expect(PROMPT)
	return child


def main():
	host = input("Enter the host taget/iP:")
	user = input("Enter the ssh Username:")
	password = input("Enter the ssh Password:")
	child = connect(user,host,password)
	send_command(child, 'etc /cat/shadow | grep root;ps')
main()
