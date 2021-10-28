import csv


vdoms = ['FW-CSF', 'FW-INTGRITY', 'FW-AUTOIT', 'FW-GIN', 'FW-GRX', 'FW-IPX', 'FW-LIE', 'FW-SHAREVDF', 'FW-VOIPX', 'FW-WIFI', 'FW-EFA', 'FW-GCN',
         'FW-OMoney', 'FW-ONLINE', 'FW-SERVICES', 'FW-VAS']
with open('services.csv', 'r') as csvfile, open('services add.txt', 'w') as services:
    addrlist = csv.reader(csvfile, delimiter=',')

    for addr in addrlist:
        if addr[0] in vdoms:
            services.write("end\n")
            services.write("end\n")
            services.write("\n")
            services.write("config vdom\n")
            services.write('edit "' + addr[0] + '"\n')
            services.write("config firewall service custom\n")
        else:
            services.write('edit "' + addr[0] + '"\n')
            services.write('set protocol TCP/UDP/SCTP\n')
            services.write('set '+addr[1]+'-portrange ' + addr[2] +'\n')
            services.write('next\n')
            services.write("\n")
    services.write("end\n")
