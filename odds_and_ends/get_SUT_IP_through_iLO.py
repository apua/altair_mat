import hpilo

ilo_ip = vSphere_iLO = '16.153.114.143'
ilo = hpilo.Ilo(ilo_ip)
sut_ip = ilo.get_embedded_health()['nic_information']['NIC Port 1']['ip_address']
print(sut_ip)
