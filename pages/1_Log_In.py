from lib import *
from user_handling import *

st.header('Login Menu')

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
