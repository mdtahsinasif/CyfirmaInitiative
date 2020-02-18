

import dns.resolver
import dns.query
import dns.zone
from ipwhois import IPWhois

class OpenSourceRepo:

    def __init__(self):
         self.openSourceDNSdata(self)
         self.findIPDetails(self)


    def openSourceDNDdata(self):
        name = self
        for qtype in 'A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA':
            answer = dns.resolver.query(name,qtype, raise_on_no_answer=False)
            if answer.rrset is not None:
                print(answer.rrset)

        z = dns.zone.from_xfr(dns.query.xfr('nsztm1.digi.ninja', 'zonetransfer.me'))
        names = z.nodes.keys()
        sorted(names)
        #names.sort
        for n in names:
            print (z[n].to_text(n))



    def findIPDetails(self):
        obj = IPWhois(self)
        res=obj.lookup_whois()
        print (res)
