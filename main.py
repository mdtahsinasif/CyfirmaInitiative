
import dns.resolver
import dns.query
import dns.zone
from openSourceRepo import OpenSourceRepo



#
# name = 'iana.org'
# for qtype in 'A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA':
#     answer = dns.resolver.query(name,qtype, raise_on_no_answer=False)
#     if answer.rrset is not None:
#         print(answer.rrset)
#
#
#
# z = dns.zone.from_xfr(dns.query.xfr('nsztm1.digi.ninja', 'zonetransfer.me'))
# names = z.nodes.keys()
# sorted(names)
# #names.sort
# for n in names:
#     print (z[n].to_text(n))



#
# from ipwhois import IPWhois
#
# ipInput = input('Enter Ip Adress: ')
# obj = IPWhois(ipInput)
# res=obj.lookup_whois()
# print (res)


if __name__ == '__main__':
#    orgName = input('Please enter the org name:')
    ipAddress = input('Please Enter the Ip Address:')
#    OpenSourceRepo.openSourceDNDdata(orgName)
    OpenSourceRepo.findIPDetails(ipAddress)