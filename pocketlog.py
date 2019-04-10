#!/usr/bin/env python3

import sys

# Reads lines from gunicorn log such as:
# [2019-01-22 13:18:48,946] [smartcambridge.views] [INFO] - : |logger|pocket|VVKA-4702|stop_timetable|component_ref=0500CCITY527|

def log_date(line):
    return line[1:11]

def log_client(line):
    log_parts = line.split("|")
    return log_parts[3]

def print_day(date, total_clients, clients, repeat_clients):
    new_clients_str = ''
    repeat_clients_str = ''
    new_clients = []
    today_repeat_clients = []

    for client in clients:
        if client in repeat_clients:
            repeat_clients_str += '#'
            today_repeat_clients.append(client)
        else:
            new_clients_str += '='
            new_clients.append(client)

    print(f'{date},{len(clients):0>3},{len(today_repeat_clients)},{len(new_clients)},{total_clients:0>3},{repeat_clients_str + new_clients_str},{"+".join(sorted(today_repeat_clients))},{"+".join(sorted(new_clients))}')

if __name__=="__main__":

    if len(sys.argv) != 2:
        print("Usage: ")
        print("  pockelog.py [input_file_name] >output_file_name")
        sys.exit(0)

    print("Date,Day Users,Day Repeat Users,Day New Users,Total Users,Bar chart,Repeat User Ids")

    current_clients = [] # unique clients for DATE

    prior_clients = [] # unique clients before current date

    repeat_clients = []

    current_date = None # will be updated to include 'current' date from line in log file

    ####################################################################
    # Build 'repeat_clients' list
    ####################################################################
    with open(sys.argv[1], 'rU') as f:
        for line in f:

    #for line in sys.stdin:
            line_date = log_date(line)
            line_client = log_client(line)

            if current_date is None:
                current_clients.append(line_client)
                current_date = line_date

            elif current_date == line_date:
                if not line_client in current_clients:
                    current_clients.append(line_client)
            else:
                # current_date is not None and current_date != line_date

                # add current_clients to prior_clients
                for client in current_clients:
                    if not client in prior_clients:
                        prior_clients.append(client)

                current_clients = [ line_client ]
                current_date = line_date

            # Add current client to repeat_clients list
            if line_client in prior_clients:
                if not line_client in repeat_clients:
                    repeat_clients.append(line_client)

    current_clients = []

    current_date = None # will be updated to include 'current' date from line in log file

    prior_clients = []

    with open(sys.argv[1], 'rU') as f:
        for line in f:

    #for line in sys.stdin:
            line_date = log_date(line)
            line_client = log_client(line)

            if current_date is None:
                current_clients.append(line_client)
                current_date = line_date

            elif current_date == line_date:
                if not line_client in current_clients:
                    current_clients.append(line_client)
            else:
                # current_date is not None and current_date != line_date
                #print(f'changing day from {current_date} to {line_date}')
                #print(f'prior_clients [{len(prior_clients)}] is {"+".join(prior_clients)}')
                print_day(current_date, len(prior_clients), current_clients, repeat_clients)

                current_clients = [ line_client ]
                current_date = line_date

            if not line_client in prior_clients:
                #print(f'adding {line_client} to prior_clients')
                prior_clients.append(line_client)

    print_day(current_date, len(prior_clients), current_clients, repeat_clients)

    print(f'Repeat clients,{len(repeat_clients):0>3},{"+".join(repeat_clients)}')

    print(f'Prior clients,{len(prior_clients):0>3},{"+".join(prior_clients)}')


