# storing all library imports in one place
# this file is imported into each file

import streamlit as st
import time
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import csv
import os 
import plotly.graph_objects as go
import re
import glob
import string
import random


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

# takes a DataFrame and returns the date
def find_date(df):
	return df.at[0, 'timestamp']

# takes a DataFrame and returns the bed time
def find_bed_time(df):
	# the initial state is not asleep
	asleep = False 
	# reading each row
	for i in range(len(df.index)):
		# asleep state is represented by 1
		if not asleep and df.at[i, 'prediction'] == 1:
			# time at which the subject went to sleep
			return df.at[i, 'timestamp']

# takes a DataFrame and returns the wake time
def find_wake_time(df):
	# the initial state is not asleep
	asleep = False 
	# reading each row
	for i in range(len(df.index)):
		# asleep state is represented by 1
		if not asleep and df.at[i, 'prediction'] == 1:
			asleep = True
		if asleep and df.at[i, 'prediction'] == 0:
			# time at which the subject woke up
			return df.at[i, 'timestamp']

def find_day(df):
	ts = pd.Timestamp(df.iat[0, 0])
	return ts.day_name()[0:3]


def write_sql_csv(username, input_files, output_file_name):
    if os.path.exists(output_file_name):
        os.remove(output_file_name) 
    with open(output_file_name, 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(['daily_id', 'user_id', 'date', 'day', 'sleep_duration', 'bed_time_gt', 'wake_time_gt', 'uncertain_rate'])

        for file in input_files:
            if file is not None:
                df = pd.read_csv(file)
                writer.writerow([''.join(random.choices(string.ascii_letters+string.digits,k=10)), 
				 username, 
				 find_date(df),
				 find_day(df),
				 find_sleep_duration(df), 
				 find_bed_time(df), 
				 find_wake_time(df), 
				 find_uncertain_rate(df)
				 ]) 


def add_data(username):
	files = []
	for i in range(1, 91):
		f = open('F' + str(i) +'.csv', 'r')
		files.append(f)
	write_sql_csv(username, files, 'daily_sleep.csv')






