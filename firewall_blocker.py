'''
Firewall configurations


set zone-policy zone OUTSIDE interface eth2
set zone-policy zone INSIDE interface eth1

set firewall group network-group DENIED_IPS network 10.0.2.2/32
set firewall group network-group SERVERS network 10.0.1.2/32

set firewall name OUTSIDE-TO-INSIDE rule 100 description "Deny attackers ips"
set firewall name OUTSIDE-TO-INSIDE rule 100 source group network-group DENIED_IPS
set firewall name OUTSIDE-TO-INSIDE rule 100 destination group network-group SERVERS
set firewall name OUTSIDE-TO-INSIDE rule 100 action drop

set zone-policy zone INSIDE from OUTSIDE firewall name OUTSIDE-TO-INSIDE

commit
save

'''

FIREWALL_IP = "10.0.1.1"

def executeCommand(sshConnection, command):
	ssh_stdin, ssh_stdout, ssh_stderr = sshConnection.exec_command(command)
	return ssh_stdin, ssh_stdout, ssh_stderr

def blockIP(sshConnection, ip):
	ssh_stdin, ssh_stdout, ssh_stdere = executeCommand(pcClient, "set firewall group network-group DENIED_IPS network "+ip+"/32")
	ssh_stdin, ssh_stdout, ssh_stdere = executeCommand(pcClient, "commit")
	ssh_stdin, ssh_stdout, ssh_stdere = executeCommand(pcClient, "save")
	print("IP "+ip+" blocked successfully!")

def main():

	pcClient = client.SSHClient()
	pcClient.set_missing_host_key_policy(client.AutoAddPolicy())
	pcClient.connect(FIREWALL_IP, username="vyos", password="vyis")
	print("Connected to firewall "+FIREWALL_IP)
	blockIP(pClient, "10.0.2.2")

main()