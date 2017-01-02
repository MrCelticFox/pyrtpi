# Python CLI for Dublin Bus' RTPI

A command line interface for Dublin Bus' Real Time Passenger Information, written in Python.

## Usage
The script is run like so: `python rtpi.py <stop_number> [OPTIONS]`
where `<stop_number>` is the number of the bus stop that you want to get the times for.  
Currently supported options are as follows:
- `-n <num>` : allows the user to limit the number of results displayed
- `-b <bnum>` : allows the user to only display results for a certain bus route
- `-h` : prints help information and exits

Note that options can be combined, so running `python rtpi.py 192 -b 46a -n 3`
will display the first 3 times for the 46a bus at stop 192.

## Compatibility
This project is designed to be run with Python 3 or above. Versions below that are not supported and are not guaranteed to work.
