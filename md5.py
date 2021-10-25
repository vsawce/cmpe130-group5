
class md5:
    s = [
    7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
    5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
    4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
    6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
    k = [
    0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
    0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
    0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
    0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
    0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
    0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
    0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
    0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
    0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
    0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
    0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
    0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
    0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
    0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
    0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
    0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391]
    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476
    length_processed_bytes = 0
    digest = b''

    def __init__(self):
        self.processed_byte = b''

    def string_process(self, input):
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
                length_of_padded_bits = c/8 #LENGTH IN BYTES
            #print(length_of_padded_bits)

            output_bytes = input_bytes + bytes.fromhex('80') #ADD 1 and 7 zeros
            for i in range(int(length_of_padded_bits) - 1):
                output_bytes += bytes.fromhex('00')

            bits_length = len(((length_of_input*8).to_bytes(2, byteorder='big')))
            #print(bits_length)
            for i in range((8-bits_length)):
                output_bytes += bytes.fromhex('00')
            output_bytes += ((length_of_input*8).to_bytes(2, byteorder='big'))

            self.processed_byte = output_bytes
            self.length_processed_bytes = len(output_bytes)
            #print(self.length_processed_bytes)
            print("Input Bytes = ")
            print(input_bytes.hex())
            print("Output Bytes = ")
            print (output_bytes.hex())

    def md5_process(self):
        chunks = list(chunked(128, self.processed_byte.hex())) #break processed bytes into chunks

        for chunk in chunks:
            m = list(chunked(8, chunk))
            a = self.a0
            b = self.b0
            c = self.c0
            d = self.d0
            #print(m)
            for i in range(64):
                f = 0
                g =0
                if(i >= 0 and i <= 15):
                    f = f_op(b, c, d)
                    g = i
                elif(i >= 16 and i <= 31):
                    f = g_op(b, c, d)
                    g = (((5*i) + 1) % 16)
                elif(i >= 32 and i <= 47):
                    f = h_op(b, c, d)
                    g = (((3*i) + 5) % 16)
                elif(i >= 48 and i <= 63):
                    f = i_op(b, c, d)
                    g = ((7*i) % 16)
                #print(m[g].hex())
                #print(int.from_bytes(m[g], byteorder='big'))
                f = (f + a + (self.k[i]) + (int((m[g]),16))) % (2**32)
                #f = f + a + (self.k[i]) + (int.from_bytes(m[g], byteorder='big'))
                a = d
                d = c
                c = b
                b = (b + left_rotate(f, self.s[i])) % (2**32)
            self.a0 = (self.a0 + a) % (2**32)
            self.b0 = (self.b0 + b) % (2**32)
            self.c0 = (self.c0 + c) % (2**32)
            self.d0 = (self.d0 + d) % (2**32)
        print((self.a0).bit_length())
        print(hex(self.b0))
        print(hex(self.c0))
        self.digest = self.a0
        self.digest = (self.digest << 32) | self.b0
        self.digest = (self.digest << 32) | self.c0
        self.digest = (self.digest << 32) | self.d0

        #self.digest += (self.a0).to_bytes(2, byteorder='little')
        #self.digest += (self.b0).to_bytes(2, byteorder='little')
        #self.digest += (self.c0).to_bytes(2, byteorder='little')
        #self.digest += (self.d0).to_bytes(2, byteorder='little')
        print(hex(self.digest))





def chunked(size, source):
    for i in range(0, len(source), size):
        yield source[i:i+size]

def f_op(b, c, d):
    return ((b & c) | (~b & d))
def g_op(b, c, d):
    return ((b & d) | (c & ~d))
def h_op(b, c, d):
    return (b ^ c ^ d)
def i_op(b, c, d):
    return (c ^ (b | ~d))

def left_rotate(x, y):
    #return (x<<y) | (x>>(32-y))
    return ((x << (y & 31)) | ((x & 0xffffffff) >> (32 - (y & 31)))) & 0xffffffff

def main():
    input_string = "hello"
    print("Input_String = " + input_string + "\n")
    gg = md5()
    gg.string_process(input_string)
    gg.md5_process()
    #string_process(input_string)
    #bits = 1024
    #p = bits.to_bytes(2, byteorder='big')
    #print(p.hex())


main()
