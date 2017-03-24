# Look at arguments.
# If file location overridden, look for the specified file.
# If not, look for default file (./parseargs.json).
# Read out specific values from file.
# If missing, provide the default.
import argparse
import os.path

parser = argparse.ArgumentParser(description="Load configuration parameters from JSON-based configuration file.")

parser.add_argument("-f", "--file", type=str, default="./parseargs.json", help="Overrides defauflt config file location with specified location/filename. Default: ./parseargs.json")
parser.add_argument("-p", "--prompt", default=0, action="count", help="Prompt user for value instead of using command line.")

args = parser.parse_args()

if args.prompt > 0:
	tfile = input("What file would you like? ")
else:
	tfile = args.file

print(tfile)
