import requests
print("                FREE SMS SENDER API")
resp = requests.post("http://textbelt.com/text",{
'phone': '+79295029190', # Your telephone number here.
'message': 'Salom nima gap',# Your text message here
'key': 'textbelt', 
})
print(resp.json())
