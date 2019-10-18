#!/usr/bin/python3
import sys
import dns.resolver
import argparse


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

    google_public_dns_ip = ['8.8.8.8', '8.8.4.4'] 

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
                    print (domain, ipval.to_text())
            except:
                print (domain, 'notinlocal')
        except:
            print (domain, 'notingoogle') 

    f.close()

if __name__ == "__main__":
    main()
