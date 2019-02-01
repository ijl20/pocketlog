
import sys

# Reads lines from gunicorn log such as:
# [2019-01-22 13:18:48,946] [smartcambridge.views] [INFO] - : |logger|pocket|VVKA-4702|stop_timetable|component_ref=0500CCITY527|

def log_date(line):
    return line[1:11]

def log_client(line):
    log_parts = line.split("|")
    return log_parts[3]

def print_day(date, clients, prior_clients):
    new_clients = ''
    repeat_clients = ''

    for client in clients:
        if client in prior_clients:
            repeat_clients += '#'
        else:
            new_clients += '='

    #print(f'{date} {len(clients):0>3}/{len(prior_clients):0>3} {" ".join(sorted(clients))}')
    print(f'{date} {len(clients):0>3}/{len(prior_clients):0>3} {repeat_clients + new_clients}')

def main():
    print("Hello World?")

    current_clients = [] # unique clients for DATE

    prior_clients = [] # unique clients EVER

    repeat_clients = []

    current_date = None # will be updated to include 'current' date from line in log file

    #with open('pocket.log-records', 'rU') as f:
    #    for line in f:

    for line in sys.stdin:
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
            print_day(current_date, current_clients, prior_clients)

            # add current_clients to prior_clients
            for client in current_clients:
                if not client in prior_clients:
                    prior_clients.append(client)

            current_clients = [ line_client ]
            current_date = line_date

        # Add current client to all_clients list
        if line_client in prior_clients:
            if not line_client in repeat_clients:
                repeat_clients.append(line_client)

    print_day(current_date, current_clients, prior_clients)

    print(f'Repeat clients: {len(repeat_clients):0>3} {",".join(repeat_clients)}')

    print(f'Prior clients: {len(prior_clients):0>3} {",".join(prior_clients)}')
# Main
main()

