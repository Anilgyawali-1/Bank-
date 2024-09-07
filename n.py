# import json
import hashlib


inp = input('Enter your password : ')
hash = hashlib.new("SHA256")
hash.update(inp.encode())
inp = hash.hexdigest()
print(inp)
