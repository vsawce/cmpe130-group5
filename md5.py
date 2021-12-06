import math

s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
  5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
  4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
  6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

k = [int(abs(math.sin(i+1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

init_values = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

def md5(input):

    #TAKE INPUT AS BYTE_ARRAY
    input_as_byte_array = bytearray(input, 'utf-8')
    length_of_input = (len(input_as_byte_array) * 8) & 0xffffffffffffffff; #lenth in # of bits

    #FIND THE NUMBER OF REQUIRED PADDED BITS
    length_of_padded_bits = 0
    c = 0
    if(length_of_input <= 448):
        length_of_padded_bits = 448 - length_of_input
    else:
        while(((length_of_input)+c) % 512 != 448):
            c += 1
        length_of_padded_bits = c

    #ADD PADDING (1 and additional zeros)
    input_as_byte_array.append(0x80)
    while ((len(input_as_byte_array)%64) != 56):
        input_as_byte_array.append(0x0)

    #APPEND LENGTH OF ORIGINAL MESSAGE IN 64 BITS
    input_as_byte_array += (length_of_input.to_bytes(8, byteorder='little'))

    #MD5 MIXING ALGO
    a0 = init_values[0]
    b0 = init_values[1]
    c0 = init_values[2]
    d0 = init_values[3]
    for chunk_index in range(0, len(input_as_byte_array), 64):
        chunk = input_as_byte_array[chunk_index:(chunk_index + 64)]
        a = a0
        b = b0
        c = c0
        d = d0
        for i in range(64):
            if 0 <= i <= 15:
                f = (b & c) | ((~b) & d)
                g = i
            elif 16 <= i <= 31:
                f = (d & b) | ((~d) & c)
                g = ((5 * i) +1) % 16
            elif 32 <= i <= 47:
                f = (b ^ c ^ d)
                g = ((3 * i) + 5) % 16
            elif 48 <= i <= 63:
                f = (c ^ (b | (~d)))
                g = (7 * i) % 16

            f = (f + a + k[i] + int.from_bytes(chunk[4*g:4*g+4], byteorder='little'))
            a = d
            d = c
            c = b
            b = (b + left_rotate(f, s[i])) & 0xFFFFFFFF

        a0 = (a0 + a) & (0xFFFFFFFF)
        b0 = (b0 + b) & (0xFFFFFFFF)
        c0 = (c0 + c) & (0xFFFFFFFF)
        d0 = (d0 + d) & (0xFFFFFFFF)

    #produce digest(IN LITTLE ENDIAN)
    digest = (a0 << 0) | (b0 <<32) | (c0 <<64) | (d0 <<96)
    return digest

def left_rotate(x, y):
    return ((x << (y & 31)) | ((x & 0xffffffff) >> (32 - (y & 31)))) & 0xffffffff

def md5_to_hex(digest):
    raw = digest.to_bytes(16, byteorder='little')
    return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))

# def main():
#     str = "Lrem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
#     print(md5_to_hex(md5(str)))

# main()
