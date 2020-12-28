import requests

# r = requests.get('https://reqres.in/api/users/2')
# print("Status code:",r.status_code)
# print(r.text)

# myObj = {
#     "name": "morpheus",
#     "job": "leader"
# }
# r = requests.post('https://reqres.in/api/users',data=myObj)
# print("Status code:",r.status_code)
# print(r.text)



# putObj = {
#     "name": "morpheus",
#     "job": "zion resident"
# }
# r = requests.put('https://reqres.in/api/users',data=putObj)
# print("Status code:",r.status_code)
# print(r.text)

r = requests.delete('https://reqres.in/api/users/2')
print("Status code:",r.status_code)
print(r.text)