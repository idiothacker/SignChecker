# SignChecker
SignChecker is a simple python script that uses NMAP NSE SMB scripts to check for SMB signing an outputs the results to a CSV file.

## How to Use
```
  -h, --help    show this help message and exit
  -i --infile   The location of your input file, 1 IP per line. (-i ips.txt)
  -o --outfile  The name of the output csv file (-o results.csv)
```

### Run Example:
``` bash
python3 ScanChecker.py -i ip_addresses.txt -o results.csv
```
