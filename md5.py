
def string_process(input):
        input_bytes  = bytes(input, 'utf-8')
        length_of_input = len(input_bytes) #LENGTH in BYTES NOT BITS
        #print (length_of_input)

        length_of_padded_bits = 0
        c = 0

        #56 bytes is 448 bits
        if(length_of_input <= 56):
            length_of_padded_bits = 56 - length_of_input
        else:
            while(((length_of_input * 8)+c) % 512 != 448):
                c += 1
            length_of_padded_bits = c/8
        #print(length_of_padded_bits)

        output_bytes = input_bytes + bytes.fromhex('80') #ADD 1 and 7 zeros
        for i in range(length_of_padded_bits - 1):
            output_bytes += bytes.fromhex('00')

        for i in range(7):
            output_bytes += bytes.fromhex('00')
        output_bytes += bytes.fromhex('{:x}'.format((length_of_input*8)))
        print("Input Bytes = ")
        print(input_bytes.hex())
        print("Output Bytes = ")
        print (output_bytes.hex())

input_string = "hello"
print("Input_String = " + input_string + "\n")
string_process("hello")
