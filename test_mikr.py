from netmiko import ConnectHandler

mikrotik_router_1 = {
'device_type': 'mikrotik_routeros',
'host': '10.10.21.116',
'port': '22',
'username': 'user1',
'password': '1'
}

sshCli = ConnectHandler(**mikrotik_router_1)
print(sshCli.find_prompt())

output = sshCli.send_command("/interface ethernet print")
print(output)

command = "/export"
output = sshCli.send_command(command)
print(output)

file = open("BackUp-Config-Mikrotik-Netmiko.txt", "w")
file.write(output)
file.close()

sshCli.disconnect()