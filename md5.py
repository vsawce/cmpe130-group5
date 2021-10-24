
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
        for i in range(int(length_of_padded_bits) - 1):
            output_bytes += bytes.fromhex('00')

        bits_length = len(((length_of_input*8).to_bytes(2, byteorder='big')))
        #print(bits_length)
        for i in range((8-bits_length)):
            output_bytes += bytes.fromhex('00')
        output_bytes += ((length_of_input*8).to_bytes(2, byteorder='big'))

        print("Input Bytes = ")
        print(input_bytes.hex())
        print("Output Bytes = ")
        print (output_bytes.hex())

def md5_process():
    print(" \n")

def main():
    input_string = "hello world long string testing. hello world long string testing. hello world long string testing. hello world long string testing."
    print("Input_String = " + input_string + "\n")
    string_process(input_string)
    #bits = 1024
    #p = bits.to_bytes(2, byteorder='big')
    #print(p.hex())

main()
