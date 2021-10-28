import csv


vdoms = ['FW-CSF', 'FW-INTGRITY', 'FW-AUTOIT', 'FW-GIN', 'FW-GRX', 'FW-IPX', 'FW-LIE', 'FW-SHAREVDF', 'FW-VOIPX', 'FW-WIFI', 'FW-EFA', 'FW-GCN',
         'FW-OMoney', 'FW-ONLINE', 'FW-SERVICES', 'FW-VAS']
with open('obj_grp.csv', 'r') as csvfile, open('addr_grp.txt', 'w') as addrobjects:
    addrlist = csv.reader(csvfile, delimiter=',')
    for addr in addrlist:
        if addr[0] in vdoms:
            addrobjects.write("end\n")
            addrobjects.write("end\n")
            addrobjects.write("\n")
            addrobjects.write("config vdom\n")
            addrobjects.write('edit "' + addr[0] + '"\n')
            addrobjects.write("config firewall addrgrp\n")
        else:
            addrobjects.write('edit "' + addr[0] + '"\n')
            if addr[1] == 'new':
                membrii=addr[2].split()
                addrobjects.write('set member')
                for i in membrii:
                    addrobjects.write(' "' + i + '"')
                addrobjects.write('\n')
                addrobjects.write('set comment "' + addr[3] + '"\n')
            else:
                membrii = addr[2].split()
                addrobjects.write('append member')
                for j in membrii:
                    addrobjects.write(' "' + j + '"')
                addrobjects.write('\n')
            addrobjects.write('next\n')
            addrobjects.write("\n")
    addrobjects.write("end\n")




