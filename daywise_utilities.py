from lib import *
from analysis_utilities import *

# returns a dictionary with an initial day-hours mapping
def get_init_dict():
    return {
        'Mon': 0,
        'Tue': 0,
        'Wed': 0,
        'Thu': 0,
        'Fri': 0, 
        'Sat': 0,
        'Sun': 0
    }

# takes one or more CSV files and returns a dictionary mapping each day to number of hours of sleep
def find_day_distribution(files):
    #  initializing dictionary
    # 'db' stands for 'distribution'
    db = get_init_dict()
    # reading each file
    for file in files:
        if file is not None:
            # creating DataFrame from CSV file
            df = pd.read_csv(file)
            # storing the date
            ts = pd.Timestamp(df.iat[0, 0])
            # adding sleep hours to the day
            db[ts.day_name()[0:3]] = db[ts.day_name()[0:3]] + find_sleep_duration(df)
    return db        	
