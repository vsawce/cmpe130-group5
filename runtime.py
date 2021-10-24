from ctypes import string_at
from datetime import datetime
import hashlib
import string
import random
import matplotlib.pyplot as plt

def md5_time(input):
    start_time = datetime.now()
    output = hashlib.md5(input.encode('utf-8'))
    end_time = datetime.now()
    print('MD5: ' + output.hexdigest())
    return round((end_time - start_time).total_seconds() * 1000000)

def sha3_256_time(input):
    start_time = datetime.now()
    output = hashlib.sha3_256(input.encode('utf-8'))
    end_time = datetime.now()
    print('SHA256: ' + output.hexdigest())
    return round((end_time - start_time).total_seconds() * 1000000)

def rand_string(n):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for char in range(n))

#################################################################################

string_sizes = [10, 50, 100, 300, 500, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 50000000]
strings = []

md5_times = []
sha3_256_times = []

for size in string_sizes:
    str = rand_string(size)
    strings.append(str)
    
for i in range(len(string_sizes)):
    print(f'Generating hashes for string of length: {string_sizes[i]}')
    str = strings[i]
    md5_times.append(md5_time(str))
    sha3_256_times.append(sha3_256_time(str))
    print(f'Length {string_sizes[i]} finished')

print("MD5 times: ", end = '')
print(md5_times)
print("SHA256 times: ", end = '')
print(sha3_256_times)

plt.plot(string_sizes, md5_times, label = "MD5")
plt.plot(string_sizes, sha3_256_times, label = "SHA256")

plt.xlabel("String size (characters * 10^7)")
plt.ylabel("Time to run (microseconds)")
plt.title("Run time analysis: MD5 vs SHA256")

plt.legend()

plt.show()