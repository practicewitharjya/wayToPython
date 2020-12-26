import requests
# url = 'https://www.w3schools.com/python/demopage.php'
# myobj = {
#     "email": "eve.holt@reqres.in",
#     "password": "pistol"
# }
#
# x = requests.post("https://reqres.in/api/register", data=myobj)
# print(x.status_code, x.reason)
# print(x.text)
#
# print("test")
# r = requests.get("https://reqres.in/api/users/2")
# print(r.text)
#
# data={
#     "name": "morpheus",
#     "job": "zion resident"
# }
# r = requests.put("https://reqres.in/api/users/2",data=data)
# print(r.text)


r = requests.delete("https://reqres.in/api/users/2")
print(r.status_code)

#print(r.text)