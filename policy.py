import csv


vdoms = ['FW-CSF', 'FW-INTGRITY', 'FW-AUTOIT', 'FW-GIN', 'FW-GRX', 'FW-IPX', 'FW-LIE', 'FW-SHAREVDF', 'FW-VOIPX', 'FW-WIFI', 'FW-EFA', 'FW-GCN',
         'FW-OMoney', 'FW-ONLINE', 'FW-SERVICES', 'FW-VAS', 'FW-CLOUD']
with open('policy.csv', 'r') as csvfile, open('policies.txt', 'w') as policies:
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
            policies.write('edit 0 \n')
            policies.write('set srcintf "' + addr[0] + '"\n')
            policies.write('set dstintf "' + addr[1] + '"\n')
            policies.write('set srcaddr')
            source = addr[2].split()
            for i in source:
                policies.write(' "' + i + '"')
            policies.write('\n')
            if addr[3]:
                group = addr[3].split()
                policies.write('set group')
                for j in group:
                    policies.write(' "' + j + '"')
                policies.write('\n')
            dest = addr[4].split()
            policies.write('set dstaddr')
            for k in dest:
                policies.write(' "' + k + '"')
            policies.write('\n')
            if addr[5] == {}:
                policies.write('set action "' + addr[5] + '"\n')
            else:
                policies.write('set action accept \n')
            if addr[6]:
                policies.write('set schedule "' + addr[6] + '"\n')
            else:
                policies.write('set schedule "always"\n')
            serv = addr[7].split()
            policies.write('set service')
            for t in serv:
                policies.write(' "' + t + '"')
            policies.write('\n')
            if addr[8]:
                policies.write('set logtraffic "' + addr[8] + '"\n')
            else:
                policies.write('set logtraffic all \n')
            if addr[9]:
                policies.write('set nat ' + addr[9] + '\n')
                policies.write('set ippool enable \n')
                policies.write('set poolname "' + addr[10] + '"\n')
            else:
                policies.write('set nat disable \n')
            policies.write('set comments "' + addr[11] + '"\n')
            policies.write('next\n')
            policies.write("\n")
    policies.write("end\n")
