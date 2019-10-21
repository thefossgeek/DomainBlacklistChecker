# DomainBlacklistChecker
A DNS lookup tool to quickly review the standard DNS records for a domain and show the list of domain needs to be configured in blocklist

# User Guide

Follow the below instruction to run the script:

1). Clone the repo to your local machine

```
$ git clone https://github.com/thefossgeek/DomainBlacklistChecker.git
```

2). Switch to the repo directory

```
$ cd DomainBlacklistChecker
```

3). Run the below command to install dependency python module. Please note this required internet to download packages

```
$ sudo pip3 install -r requirements.txt
```

4). See the script document help for supported command line arguments.

```
$ ./blacklist_checker.py --help
usage: blacklist_checker.py [-h] -c <cidr> -f <filename>

Python script to get Azure Key Vault Secret using REST API

optional arguments:
  -h, --help            show this help message and exit
  -c <cidr>, --cidr <cidr>
                        The CIDR in which you want to lookup if the domain already blocklisted or not.
  -f <filename>, --filename <filename>
```

4). Run the script with arguments

```
$ ./blacklist_checker.py -f ./domain_lists.txt -c 'xx.xx.xx.xx/24'

or

$ ./blacklist_checker.py --filename ./domain_lists.txt -cidr 'xx.xx.xx.xx/24'

NOTE: Update your list of domain name in domain_lists.txt or create your own file and pass the full fule path as command line arguments.
 
```

5). Example:

```
$ ./blacklist_checker.py -f domain_lists.txt -c '192.168.56.0/24'
tutorialspoint.com 94.130.81.180
gopi.com 50.62.124.1
```
