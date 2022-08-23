import requests

r =  requests.get('http://yandex.ru')

print(r)
print(dir(r))
# print(help(r))
print(r.status_code)

print("content:")
print("-----")
print(r.content)
print("-----")
print("text:")
print("-----")
print(r.text)