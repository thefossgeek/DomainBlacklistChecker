#!/usr/bin/python3
import sys
import dns.resolver
import argparse
#from netaddr import CIDR, IP
from netaddr import IPNetwork, IPAddress

google_public_dns_ip = ['8.8.8.8', '8.8.4.4'] 

# Update the CIDR in which you would like to check
check_cidr = 'xx.xx.xx.xx/24'

def get_args():
    """
    This method defines what arguments it requires, and it will figure out how to parse those out of `sys.argv`.
    The method also automatically generates help and usage messages and issues errors when users give the program invalid arguments.
    """
    parser = argparse.ArgumentParser(description='Python script to get Azure Key Vault Secret using REST API',
                formatter_class = argparse.RawTextHelpFormatter)
	
    parser.add_argument('-f', '--filename',
                        help='The full path of file which contain list of domain names.',
                        metavar='<filename>',
                        action='store',
                        required=True,
                       	default=None)

    args = parser.parse_args()

    return args

def main():
    
    args = get_args()

    infilename = args.filename


    dns_resolver = dns.resolver.Resolver(configure=False)

    dns_resolver.nameservers = google_public_dns_ip

    f = open(infilename, "r")
    for line in f:
        domain = line.rstrip()
        try:
            query_gdns = dns_resolver.query(domain, 'A')
            try:
                query_local = dns.resolver.query(domain, 'A')
                for ipval in query_local:
                    ipv4_address = ipval.to_text()
                    #print (domain, ipval.to_text())
                    if IPAddress(ipv4_address) in IPNetwork(check_cidr):
                        # Continue if the IP address is internal IP.
                        continue 
                    else:
                        # Print only domain needs to be block listed
                        print (domain, ipval.to_text())
            except:
                continue
        except:
            # Continue if the domain entry not in Google DNS.
            continue 

    f.close()

if __name__ == "__main__":
    main()
