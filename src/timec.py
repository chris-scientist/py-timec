from datetime import datetime
import argparse

# =====================================================================
# Functions

def string2date(string_date):
	array_date = string_date.split("/")
	return datetime(int(array_date[2]), int(array_date[1]), int(array_date[0]))

def display_days_in_year(nb_days):
	if nb_days > 365 :
		print("Nb of year: " + str(nb_days / 365.25))

def display(a_start_date, a_end_date, a_diff_day):
	print("Start date: " + str(a_start_date))
	print("End date: " + str(a_end_date))
	print("Nb of days: " + str(a_diff_day.days))
	display_days_in_year(a_diff_day.days)

# =====================================================================
# Script

# Manage arguments of script

argparser = argparse.ArgumentParser()
argparser.add_argument("-v", "--verbose", action="store_true", help="show debug message if true")
argparser.add_argument("-s", "--start", help="beginning date")
argparser.add_argument("-e", "--end", help="end date")

args = argparser.parse_args()

# Settings

isShowError = args.verbose
start_date = datetime.now()
end_date = datetime.now()

if args.start != None:
	start_date = string2date(args.start)

if args.end != None:
	end_date = string2date(args.end)

# Main program

diff_days = (end_date - start_date)

display(start_date, end_date, diff_days)
