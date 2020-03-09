from datetime import datetime, timedelta
import argparse

# =====================================================================
# Functions

def compute_day_per_day_nb_days(a_start_date, a_end_date):
	cur_date = a_start_date
	nb_days = 0
	add_day_flag = True if a_start_date < a_end_date else False
	while cur_date.date() != a_end_date.date() :
		if add_day_flag :
			cur_date = cur_date + timedelta(days = 1)
			nb_days = nb_days + 1
		else:
			cur_date = cur_date - timedelta(days = 1)
			nb_days = nb_days - 1
	if nb_days > 0 :
		nb_days = nb_days + 1
	return nb_days

def compute_basic_nb_days(a_start_date, a_end_date):
	diff_days = (a_end_date - a_start_date)
	return diff_days.days

def string2date(string_date):
	array_date = string_date.split("/")
	return datetime(int(array_date[2]), int(array_date[1]), int(array_date[0]))

def display_days_in_year(nb_days):
	if nb_days > 365 :
		print("Nb of year: " + str(nb_days / 365.25))

def display(a_start_date, a_end_date, a_mode):
	# Compute on dates
	nb_of_day = compute_basic_nb_days(a_start_date, a_end_date)
	if a_mode == "dpd":
		nb_of_day = compute_day_per_day_nb_days(a_start_date, a_end_date)
	# Display
	print("Start date: " + str(a_start_date))
	print("End date: " + str(a_end_date))
	print("Nb of days: " + str(nb_of_day))
	display_days_in_year(nb_of_day)

# =====================================================================
# Script

# Manage arguments of script

argparser = argparse.ArgumentParser()
argparser.add_argument("-v", "--verbose", action="store_true", help="show debug message if true")
argparser.add_argument("-s", "--start", help="beginning date")
argparser.add_argument("-e", "--end", help="end date")
argparser.add_argument("-m", "--mode", help="compute nb days mode (basic|dpd), by default is basic")

args = argparser.parse_args()

# Settings

isShowError = args.verbose
start_date = datetime.now()
end_date = datetime.now()
mode = "basic"

if args.start != None:
	start_date = string2date(args.start)

if args.end != None:
	end_date = string2date(args.end)

if args.mode != None:
	if args.mode.lower() == 'dpd':
		mode = "dpd"

# Main program

display(start_date, end_date, mode)
