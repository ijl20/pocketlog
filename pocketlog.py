
import sys

# Reads lines from gunicorn log such as:
# [2019-01-22 13:18:48,946] [smartcambridge.views] [INFO] - : |logger|pocket|VVKA-4702|stop_timetable|component_ref=0500CCITY527|

def log_date(line):
    return line[1:11]

def log_client(line):
    log_parts = line.split("|")
    return log_parts[3]

def main():
    print("Hello World?")

    line_count = 0

    current_clients = []

    current_date = "foo" # will be updated to include 'current' date from line in log file

    with open('pocket.log', 'rU') as f:
        for line in f:
            line_count += 1
            line_date = log_date(line)
            line_client = log_client(line)

            if line_count == 1:
                current_date = line_date
                current_clients = [ line_client ]

            else:
                if not line_date == current_date:
                    print("{0} {1} {2}".format(current_date, len(current_clients), ' '.join(current_clients)))
                    current_clients = [ line_client ]
                    current_date = line_date
                else:
                    if not line_client in current_clients:
                        current_clients.append(line_client)

            #sys.stdout.write("{0} {1}".format(line_count,line))

    print("{0} {1} {2}".format(current_date, len(current_clients), ' '.join(current_clients)))
# Main
main()

