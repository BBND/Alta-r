# Altaïr
💻 Altaïr is a concentrate of scanning tools offering to its users complete services.

⛔If the tool is used for malicious purposes, we will not be liable.⛔

## About the tool

- **Reversing: Access the hostname of an IP address**
- **Whois: Get informations about a domain name**
- **DNS Lookup: View the standard DNS records for a domain**
- **robots.txt checker: Check the robots.txt file of a website**
- **Website header: View the header content of a website or IP address**
- **Scan ports: Scan open ports on a network server**
- **Tansfer zone: Get all DNS records for a target domain**
- **Cloudflare detector: Check if a site is secured by Cloudflare (security service in case of denial of service attack, data breach or malicious bot)**

## How it works ?

| Argument | Description |
| ------ | ------ |
| -h, --help | Display help message and exit |
| -w [Domain/IP], --whois [Domain/IP] | Domain/IP whois |
| -d [Domain], --dns	[Domain]  | DNS lookup and cloudflare detector |
| -t [Domain], --transfer [Domain]  | Scan zone Transfer |
| -s [Domain/IP], --scan [Domain/IP]  | Scan Domain/IP ports |
| -he [Domain/IP], --header	[Domain/IP]  | Website/IP Header |
| -r [Domain], --robots	[Domain]  | robots.txt Checker |
| --reverse		[IP]  | IP to Hostname |

## Usage Examples

```sh
$ python altaïr.py --scan www.example.com
```

```sh
$ python altaïr.py -r www.example.com
```

## Author
[BBND](https://www.bbnd.eu)

