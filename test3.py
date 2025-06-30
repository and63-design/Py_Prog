import hashlib
password = 'asdfasdfasdf'
sha1password = 'asdfkja;slkfjpoqwierupoqiurpoiqu'
sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
first5Char = sha1password
print(first5Char)
