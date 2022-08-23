import http.client
conn = http.client.HTTPConnection("localhost", 5000)
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()  # This will return entire content.
# The following example demonstrates reading data in chunks.
conn.request("GET", "/")
r1 = conn.getresponse()
while chunk1 := r1.read(200):
    print(repr(chunk1))


# Example of an invalid request
conn = http.client.HTTPConnection("localhost", 5000)
conn.request("GET", "/test")
r2 = conn.getresponse()
print(r2.status, r2.reason)
data2 = r2.read()
conn.request("GET", "/test")
r2 = conn.getresponse()
while chunk2 := r2.read(200):
    print(repr(chunk2))

conn = http.client.HTTPConnection("localhost", 5000)
conn.request("GET", "/about")
r3 = conn.getresponse()
print(r3.status, r3.reason)
data3 = r3.read()
conn.request("GET", "/about")
r3 = conn.getresponse()
while chunk3 := r3.read(404):
    print(repr(chunk3))

conn.close()