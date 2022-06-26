from lib import *

# takes a DataFrame and returns the total number of hours slept
# assumes that all sleep is contiguous
# DataFrame stores 24-hour activity starting at 6pm
def find_sleep_duration(df):
	# the initial state is not asleep
	asleep = False 
	# reading each row
	for i in range(len(df.index)):
		# asleep state is represented by 1
		if not asleep and df.at[i, 'prediction'] == 1:
			# time at which the subject went to sleep
			t1 = pd.Timestamp(df.at[i, 'timestamp'])
			asleep = True
		if asleep and df.at[i, 'prediction'] == 0:
			# time at which the subject woke up
			t2 = pd.Timestamp(df.at[i, 'timestamp'])
			break
	# returning duration in hours		
	return (t2 - t1).total_seconds() / 3600

# takes a DataFrame and returns the uncertainty rate
def find_uncertain_rate(df):
	for i in range (len(df.index)):
		if df.at[i, 'prediction'] == 1:
			return df.at[i, 'uncertain_rate']	