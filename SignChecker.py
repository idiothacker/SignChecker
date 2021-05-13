import nmap, argparse, csv, concurrent.futures

parser = argparse.ArgumentParser(description="Example: \n\npython3 ScanChecker.py -i ip_addresses.txt -o results.csv")
parser.add_argument("-i", metavar="--infile", help="The location of your input file, 1 IP per line. (-i ips.txt)", required=True)
parser.add_argument("-o", metavar="--outfile", help="The name of the output csv file (-o results.csv)", required=True)

args = parser.parse_args()
in_file = args.i
out_file = args.o
host_list = []

scanner = nmap.PortScanner()

def scan(ip,host_list):
    res = {
        "IP Address": ip,
        "SMB Signing": "True"
    }

    current = host_list.index(ip) + 1
    total = len(host_list)

    try:
        print(f"Checking {ip} for SMB Signing. [{current}/{total}]")
        check = scanner.scan(hosts=str(ip),arguments="-Pn -p 445 --script smb-security-mode.nse")
        if ("hostscript" in str(check)) and ("disabled" in str(check)):
            res["SMB Signing"] = "False"
            return res
        else:
            return None
    except:
        print(f"Error checking {ip}. [{current}/{total}]")
        return None

with open(in_file, "r") as hosts:
    for h in hosts:
        h = h.strip()
        if h != "":
            host_list.append(h)

with open(out_file, "w", newline="") as csvfile:
    fieldnames = ["IP Address","SMB Signing"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(scan, h,host_list) for h in host_list]
        for f in concurrent.futures.as_completed(results):
            if f.result() != None:
                writer.writerow(f.result())
