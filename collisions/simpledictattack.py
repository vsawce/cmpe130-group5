import hashlib

# GET "password" MD5 ENCODING FOR TESTING PURPOSES
str_arr = ["password"]

hex_arr = []

for i in range(len(str_arr)):
    print("Message " + str((i+1)) + " = " + str_arr[i])
    hex_arr.append(hashlib.md5(str_arr[i].encode()))
    print("Encoding " + str((i+1)) + " = " + hex_arr[i].hexdigest())

# 5f4dcc3b5aa765d61d8327deb882cf99 is the "password" hash

# Represents a known dictionary of likely/common passwords
word_dictionary = "professortarng", "bruh", "abc123", "password", "yomama"

for word in word_dictionary:
    if hashlib.md5(word.encode()).hexdigest() == '5f4dcc3b5aa765d61d8327deb882cf99':
        print("Attack successful, detected: " + word)
        break
    else:
        print("Miss")

