import array
import hashlib

def main():
    #input_string = "hello world long string testing. hello world long string testing. hello world long string testing. hello world long string testing."
    #print("input_string = " + input_string + "\n")

    # Not in string, needs conversion
    #encoded_hex = hashlib.md5(input_string.encode())
    #print("encoded_hex = " + encoded_hex.hexdigest() + "\n")

    str_arr = ["hello world long string testing. hello world long string testing. hello world long string testing. hello world long string testing."]

    hex_arr = []

    for i in range(len(str_arr)):
        print("Message " + str((i+1)) + " = " + str_arr[i])
        hex_arr.append(hashlib.md5(str_arr[i].encode()))
        print("Encoding " + str((i+1)) + " = " + hex_arr[i].hexdigest())

    #Implement rainbow tables or chosen-prefix-collision
    #Can use salts to easily find collisions


    #####################################
    #       KNOWN COLLIDING VALUES      #
    #####################################
    input1 = array.array('I',  [0x6165300e,0x87a79a55,0xf7c60bd0,0x34febd0b,0x6503cf04,
    0x854f709e,0xfb0fc034,0x874c9c65,0x2f94cc40,0x15a12deb,0x5c15f4a3,0x490786bb,
    0x6d658673,0xa4341f7d,0x8fd75920,0xefd18d5a])

    # Change two bits
    input2 = array.array('I', [x^y for x,y in zip(input1,
    [0, 0, 0, 0, 0, 1<<10, 0, 0, 0, 0, 1<<31, 0, 0, 0, 0, 0])])

    # Is input1 equal to input2?
    print(input1 == input2)

    print(hashlib.md5(input1).hexdigest())
    print(hashlib.md5(input2).hexdigest())

main()
