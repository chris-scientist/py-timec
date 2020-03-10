from datetime import datetime, timedelta
import argparse

# =====================================================================
# Constants

NB_DAYS_KEY     = "NB_DAYS"
NB_WEEKEND_KEY  = "NB_WEEKEND"

# =====================================================================
# Functions

def is_weekend(a_date):
	index_of_day = a_date.weekday()
	return True if (index_of_day == 5 or index_of_day == 6) else False

def compute_global(a_start_date, a_end_date):
	cur_date = a_start_date
	nb_days = 0
	add_day_flag = True if a_start_date < a_end_date else False
	nb_weekend = 0
	while cur_date.date() != a_end_date.date() :
		# Nb weekend compute
		if is_weekend(cur_date) :
			nb_weekend = nb_weekend + 0.5
		# Nb day compute
		if add_day_flag :
			cur_date = cur_date + timedelta(days = 1)
			nb_days = nb_days + 1
		else:
			cur_date = cur_date - timedelta(days = 1)
			nb_days = nb_days - 1
	# Add nb days for last day
	if nb_days > 0 :
		if add_day_flag :
			nb_days = nb_days + 1
		else:
			nb_days = nb_days - 1
	# Add nb weekend if is last day in weekend
	if is_weekend(cur_date) :
		nb_weekend = nb_weekend + 0.5
	# Result
	out_map = {
		NB_DAYS_KEY: nb_days,
		NB_WEEKEND_KEY: nb_weekend
	}
	return out_map

def compute_basic_nb_days(a_start_date, a_end_date):
	diff_days = (a_end_date - a_start_date)
	return diff_days.days

def string2date(string_date):
	array_date = string_date.split("/")
	return datetime(int(array_date[2]), int(array_date[1]), int(array_date[0]))

def display_days_in_year(nb_days):
	if nb_days > 365 :
		print("Nb of year: " + str(nb_days / 365.25))

def display_nb_weekend(a_nb_of_weekend):
	print("Nb of weekend: " + str(a_nb_of_weekend) + " (" + str(int(a_nb_of_weekend * 2)) + " in days)")

def display(a_start_date, a_end_date, a_mode, a_display_nb_weekend):
	# Compute on dates
	nb_of_day = compute_basic_nb_days(a_start_date, a_end_date)
	complex_output = compute_global(a_start_date, a_end_date)
	if a_mode == "dpd":
		nb_of_day = complex_output[NB_DAYS_KEY]
	# Display
	print("Start date: " + str(a_start_date))
	print("End date: " + str(a_end_date))
	print("Nb of days: " + str(nb_of_day))
	display_days_in_year(nb_of_day)
	if a_display_nb_weekend :
		display_nb_weekend(complex_output[NB_WEEKEND_KEY])

# =====================================================================
# Script

# Manage arguments of script

argparser = argparse.ArgumentParser()
argparser.add_argument("-v", "--verbose", action="store_true", help="show debug message if true")
argparser.add_argument("-s", "--start", help="beginning date")
argparser.add_argument("-e", "--end", help="end date")
argparser.add_argument("-m", "--mode", help="compute nb days mode (basic|dpd), by default is basic")
argparser.add_argument("-dw", "--displaynbweekend", action="store_true", help="display nb weekend")

args = argparser.parse_args()

# Settings

isShowError = args.verbose
start_date = datetime.now()
end_date = datetime.now()
mode = "basic"
display_nb_weekend_flag = False

if args.start != None:
	start_date = string2date(args.start)

if args.end != None:
	end_date = string2date(args.end)

if args.mode != None:
	if args.mode.lower() == 'dpd':
		mode = "dpd"

if args.displaynbweekend != None and args.displaynbweekend == True:
	display_nb_weekend_flag = True

# Main program

display(start_date, end_date, mode, display_nb_weekend_flag)
