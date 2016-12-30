# Python CLI for Dublin Bus' RTPI

A command line interface for Dublin Bus' Real Time Passenger Information, written in Python.

## Usage
The script is run like so:  
`python rtpi.py <stop_number> [<bus_number>]`  
where `<stop_number>` is the number of the bus stop that you want to get the times for.
An optional parameter `<bus_number>` may also be specified which will limit the results
to only display times for that route.

## Compatibility
This project is designed to be run with Python 3 or above. Versions below that are not supported and are not guaranteed to work.
