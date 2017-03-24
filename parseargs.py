# Module to use argparse to parse for arguments, or override
import argparse

parser = argparse.ArgumentParser(description="Prefer taking arguments for configuration, but will override to querying for arguments.")

parser.add_argument("-o", "--override", action="count", help="Overrides defauflt config search behavior. Normal behavior: Look for parseargs.conf in execution directory. Load. If failure, prompt. If failure, use defaults.", default=0)
parser.add_argument("rngmax", type=int, help="Maximum range on random observations. Lower bound is 1 (int). Default: 120.", default=120)
parser.add_argument("observations", type=int, help="Number of observations in a trial. Default: 1,000.", default=1000)
parser.add_argument("trials", type=int, help="Number of trials (sets of observations). Default: 500.", default=500)

args = parser.parse_args()
