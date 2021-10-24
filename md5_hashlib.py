import hashlib

def main():
    #input_string = "hello world long string testing. hello world long string testing. hello world long string testing. hello world long string testing."
    #print("input_string = " + input_string + "\n")

    # Not in string, needs conversion
    #encoded_hex = hashlib.md5(input_string.encode())
    #print("encoded_hex = " + encoded_hex.hexdigest() + "\n")

    str_arr = ["hello world long string testing. hello world long string testing. hello world long string testing. hello world long string testing."
                ]
    hex_arr = []

    for i in range(len(str_arr)):
        print("Message " + str((i+1)) + " = " + str_arr[i])
        hex_arr.append(hashlib.md5(str_arr[i].encode()))
        print("Encoding " + str((i+1)) + " = " + hex_arr[i].hexdigest())

    #Implement rainbow tables or chosen-prefix-collision
    #Can use salts to easily find collisions

main()
