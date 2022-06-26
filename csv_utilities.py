from lib import *
from analysis_utilities import *

# takes a dictionary and a file name (string)
# stores dictionary's data in the file with given name
def write_csv(db, file_name):
    # deleting file if it already exists
    if os.path.exists(file_name):
        os.remove(file_name)
    # writing each key-value pair to file
    with open(file_name, 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(['Day', 'Hours'])
        for key in db.keys():
            writer.writerow([key, db[key]]) 


# Takes CSV files and the name of the output file (string)
# Calculates the amount of sleep on each day and writes a row to the output file 
# format [Day, Hours, Category], where the category depends on the hours of sleep. 
def write_raw_csv(input_files, output_file_name):
    if os.path.exists(output_file_name):
        os.remove(output_file_name) 
    with open(output_file_name, 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(['Day', 'Hours', 'Category'])
        for file in input_files:
            if file is not None:
                df = pd.read_csv(file)
                ts = pd.Timestamp(df.iat[0, 0])
                duration = find_sleep_duration(df)
                category = ''
                if duration < 7:
                    category = 'Too less'
                elif duration < 9:
                    category = 'Just right'
                else:
                    category = 'Too much'
                
                writer.writerow([ts.day_name()[0:3], duration, category])

# Behaves similar to write_raw_csv, but the output file has the format [Day, Hours, Uncertainty Rate]
def write_pred_csv(input_files, output_file_name):
    if os.path.exists(output_file_name):
        os.remove(output_file_name) 
    with open(output_file_name, 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(['Day', 'Hours', 'uncertain_rate'])
        for file in input_files:
            if file is not None:
                df = pd.read_csv(file, usecols = ['timestamp', 'prediction', 'uncertain_rate'])
                duration = find_sleep_duration(df)
                category = find_uncertain_rate(df)
                ts = pd.Timestamp(df.iat[0, 0])
                writer.writerow([ts.day_name()[0:3], duration, category])               
                

 