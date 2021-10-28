import csv


vdoms = ['FW-CSF', 'FW-INTGRITY', 'FW-AUTOIT', 'FW-GIN', 'FW-GRX', 'FW-IPX', 'FW-LIE', 'FW-SHAREVDF', 'FW-VOIPX', 'FW-WIFI', 'FW-EFA', 'FW-GCN',
         'FW-OMoney', 'FW-ONLINE', 'FW-SERVICES', 'FW-VAS']
with open('policy_mod.csv', 'r') as csvfile, open('policies_mod.txt', 'w') as policies:
    addrlist = csv.reader(csvfile, delimiter=',')

    for addr in addrlist:
        if addr[0] in vdoms:
            policies.write("end\n")
            policies.write("end\n")
            policies.write("\n")
            policies.write("config vdom\n")
            policies.write('edit "' + addr[0] + '"\n')
            policies.write("config firewall policy\n")
        else:
            policies.write('edit "' + addr[0] + '"\n')
            if addr[1] == 'add':
                if addr[2]:
                    source = addr[2].split()
                    policies.write('append srcaddr')
                    for i in source:
                        policies.write(' "' + i + '"')
                    policies.write('\n')
                if addr[3]:
                    dest = addr[3].split()
                    policies.write('append dstaddr')
                    for j in dest:
                        policies.write(' "' + j + '"')
                    policies.write('\n')
                if addr[4]:
                    group = addr[3].split()
                    policies.write('append group')
                    for k in group:
                        policies.write(' "' + k + '"')
                    policies.write('\n')
                if addr[5]:
                    serv = addr[5].split()
                    policies.write('append service')
                    for t in serv:
                        policies.write(' "' + t + '"')
                    policies.write('\n')
                if addr[6]:
                    policies.write('set nat ' + addr[6] + '\n')
                    policies.write('set ippool enable \n')
                    policies.write('set poolname "' + addr[7] + '"\n')

            if addr[1] == 'remove':
                if addr[2]:
                    source = addr[2].split()
                    policies.write('unselect srcaddr')
                    for i in source:
                        policies.write(' "' + i + '"')
                    policies.write('\n')
                if addr[3]:
                    dest = addr[3].split()
                    policies.write('unselect dstaddr')
                    for j in dest:
                        policies.write(' "' + j + '"')
                    policies.write('\n')
                if addr[4]:
                    group = addr[3].split()
                    policies.write('unselect group')
                    for k in group:
                        policies.write(' "' + k + '"')
                    policies.write('\n')
                if addr[5]:
                    serv = addr[5].split()
                    policies.write('unselect service')
                    for t in serv:
                        policies.write(' "' + t + '"')
                    policies.write('\n')
                if addr[6]:
                    policies.write('set nat ' + addr[6] + '\n')
                    policies.write('set ippool disable \n')
            policies.write('next\n')
            policies.write("\n")
    policies.write("end\n")
