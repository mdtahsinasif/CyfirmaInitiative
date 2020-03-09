

from openSourceRepo import OpenSourceRepo

def week(choice):
    switcher = {
        1: one,
        2: two
    }
    fun  = switcher.get(choice, "Invalid Choice")
    print (fun())



def one():
    getOrgDetail()

def two():
    getIPDetails()





def getOrgDetail():
    orgName = input('Please enter the org name:')
    OpenSourceRepo.openSourceDNDdata(orgName)


def getIPDetails():
    ipAddress = input('Please Enter the Ip Address:')

    #     # 66.171.248.170
    OpenSourceRepo.findIPDetails(ipAddress)






if __name__ == '__main__':
    try:
        choice = input("Enter Choice 1: for Organisation Details  Choice 2: for IP Address Details  ")
        week(int(choice))
    except:
        print('Please enter the correct choice---------')







