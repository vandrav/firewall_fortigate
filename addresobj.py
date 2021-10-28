import csv


vdoms = ['FW-CSF', 'FW-INTGRITY', 'FW-AUTOIT', 'FW-GIN', 'FW-GRX', 'FW-IPX', 'FW-LIE', 'FW-SHAREVDF', 'FW-VOIPX', 'FW-WIFI', 'FW-EFA', 'FW-GCN',
         'FW-OMoney', 'FW-ONLINE', 'FW-SERVICES', 'FW-VAS', 'FW-CLOUD']
with open('obj.csv', 'r') as csvfile, open('addrobjects.txt', 'w') as addrobjects:
    addrlist = csv.reader(csvfile, delimiter=',')
    for addr in addrlist:
        if addr[0] in vdoms:
            addrobjects.write("end\n")
            addrobjects.write("end\n")
            addrobjects.write("\n")
            addrobjects.write("config vdom\n")
            addrobjects.write('edit "' + addr[0] + '"\n')
            addrobjects.write("config firewall address\n")
        else:
            if addr[2] == 'ipmask':
                addrobjects.write('edit "' + addr[0] + '"\n')
                addrobjects.write('set associated-interface "' + addr[1] + '"\n')
                addrobjects.write('set subnet ' + addr[3] + '\n')
                addrobjects.write('set comment "' + addr[5] + '"\n')
                addrobjects.write('next\n')
                addrobjects.write("\n")
            elif addr[2] == 'iprange':
                addrobjects.write('edit "' + addr[0] + '"\n')
                addrobjects.write('set associated-interface "' + addr[1] + '"\n')
                addrobjects.write('set type "' + addr[2] + '"\n')
                addrobjects.write('set start-ip "' + addr[3] + '"\n')
                addrobjects.write('set end-ip "' + addr[4] + '"\n')
                addrobjects.write('set comment "' + addr[5] + '"\n')
                addrobjects.write('next\n')
                addrobjects.write("\n")
            elif addr[2] == 'fqdn':
                addrobjects.write('edit "' + addr[0] + '"\n')
                addrobjects.write('set associated-interface "' + addr[1] + '"\n')
                addrobjects.write('set type "' + addr[2] + '"\n')
                addrobjects.write('set fqdn "' + addr[3] + '"\n')
                addrobjects.write('set comment "' + addr[5] + '"\n')
                addrobjects.write('next\n')
                addrobjects.write("\n")
    addrobjects.write("end\n")




