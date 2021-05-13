# SignChecker
SignChecker is a simple python script that uses NMAP NSE SMB scripts to check for SMB signing an outputs the results to a CSV file.

## Installation
Clone the repository, navigate into the `SignChecker` folder and then run the following command.

``` python
pip3 install -r requirements.txt
```

## How to Use
```
  -h, --help    show this help message and exit
  -i --infile   The location of your input file, 1 IP per line. (-i ips.txt)
  -o --outfile  The name of the output csv file (-o results.csv)
```

### Run Example:
``` bash
python3 SignChecker.py -i ip_addresses.txt -o results.csv
```
