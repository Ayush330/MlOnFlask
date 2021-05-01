# importing the requests library
import requests
import json

# api-endpoint
URL = "https://prowizardsinc.com/ajax.php?h=CusRegistration"

Signup_Data = {
    'mobile':'1234567898',
    'name':'Ayush Kumar ',
    'email':'kumarayushanand199814@gmail.com',
    'address':'Patna1,Bihar1',
    'state':'Bihar1',
    'city':'Patna1',
    'pincode':'841105'
}

Login_Data = {
    'cus_id':'4215010402216412',
    'password':'7378510868'
}

Normal_Data = {
    'cus_id':'4215010402216412'
}

# sending post request and saving the response as response object
r = requests.post(url = URL, data = Signup_Data)

print("Status Code: ",r.status_code)
# extracting data in json format
data = r.json()

#data to be posted
print(Login_Data)

print(data)

print(data.keys())

print(data['data'][0].keys())
