from lib import *
from user_handling import *

st.header('Login Menu')

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
