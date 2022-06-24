from lib import *
from chart_utilities import *
from analysis_utilities import *
from csv_utilities import *
from daywise_utilities import *
import sqlite3 
import hashlib
import string
import random
import sqlite3 
     
"""
# SleepMore
"""


# hashes the password string using SHA-256
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

#takes the entered password and the hashed version of the actual password. 
#Returns true if the hashed version of the entered password matches the actual hashed password
def check_hashes(password, hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

# connecting to SQL database
conn = sqlite3.connect('data.db')
c = conn.cursor()

# creates an empty users table with the required columns
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, fullname TEXT, age INTEGER, gender TEXT, country TEXT, role TEXT, networkinfo TEXT, password TEXT)')

# writes one row of data to the users table
def add_userdata(username, fullname, age , gender, country, role, networkinfo, password):
	c.execute('INSERT INTO userstable(username, fullname, age , gender, country, role, networkinfo, password) VALUES (?,?,?,?,?,?,?,?)',
		(username, fullname, age , gender, country, role, networkinfo, password))
	conn.commit()

# Takes username and password. Logs the user in if they are correct.
def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

# Displays the entire users table
def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def main():

	menu = ["Home","Login","SignUp"]
	choice = st.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader('Welcome to SleepMore. Please log in or create an account to continue.')

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.text_input("User Name")
		password = st.text_input("Password",type='password')
		if st.button("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))
				c.execute('SELECT role FROM userstable WHERE username =?', (username,))
				data = c.fetchone()
				role = data[0]
				if role == 'individual':
					c.execute('SELECT * FROM userstable WHERE username =?', (username,))
					st.write('User Data')
					st.write(c.fetchall())
					file = open('daily_sleep_copy.csv')
					c.execute('CREATE TABLE IF NOT EXISTS daily(daily_id TEXT, date TEXT, sleep_duration INTEGER, bed_time_gt TEXT, wake_time_gt TEXT, uncertain_rate INTEGER)')
					rows = csv.reader(file)
					c.executemany("INSERT INTO daily VALUES (?, ?, ?, ?, ?, ?)", rows)
					c.execute('SELECT * FROM daily')
					data = c.fetchall()
					st.write('Sleep Data')
					st.write(data)

				elif role == 'agency':
					st.write(view_all_users())
			else:
				st.warning("Incorrect Username/Password")

	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		full_name = st.text_input('Full Name')
		age = st.text_input('Age')
		gender = st.text_input('Gender')
		country = st.text_input('Country')
		network_info = ''.join(random.choices(string.ascii_letters+string.digits,k=16))
		new_password = st.text_input("Password",type='password')
		role = st.text_input('Role')

		if st.button("Signup"):
			create_usertable()
			#new_user, full_name, age , gender, country, role, network_info, password
			add_userdata(new_user, full_name, age, gender, country, role, network_info,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()


#uploaded_files = st.file_uploader("Choose one or more CSV files", accept_multiple_files=True)
#write_raw_csv(uploaded_files, 'raw.csv')
#files = glob.glob('/Users/vibhhusharma/Downloads/dataWiFiTapPrediction/batch1/Week 1/*')
files = []
for i in range(1, 8):
	f = open(str(i) +'.csv', 'r')
	files.append(f)

write_pred_csv(files, 'pred.csv')
make_freq_chart('raw.csv')

files = []
for i in range(1, 8):
	f = open(str(i) +'.csv', 'r')
	files.append(f)


uploaded_files4 = st.file_uploader("Choose one or more CS", accept_multiple_files=True)
db = find_day_distribution(files)
write_csv(db, 'hours.csv')
make_pie_chart('hours.csv')

files = []
for i in range(1, 8):
	f = open(str(i) +'.csv', 'r')
	files.append(f)
uploaded_files2 = st.file_uploader("Choose one or more CSV file", accept_multiple_files=True)
write_pred_csv(files, 'pred.csv')
make_pred_chart('pred.csv')
files = []
for i in range(1, 8):
	f = open(str(i) +'.csv', 'r')
	files.append(f)

uploaded_files3 = st.file_uploader("Choose one or more CSV ", accept_multiple_files=True)
db = find_day_distribution(files)
write_csv(db, 'hours.csv')
make_pie_chart('hours.csv')
make_polar_bar_chart('pred.csv')



