
import dns.resolver
import dns.query
import dns.zone
from openSourceRepo import OpenSourceRepo





if __name__ == '__main__':
#    orgName = input('Please enter the org name:')
    ipAddress = input('Please Enter the Ip Address:')
#    OpenSourceRepo.openSourceDNDdata(orgName)
    OpenSourceRepo.findIPDetails(ipAddress)
