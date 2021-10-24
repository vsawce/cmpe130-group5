import hashlib

def main():
    input_string = "hello world long string testing. hello world long string testing. hello world long string testing. hello world long string testing."
    print("input_string = " + input_string + "\n")

    # Not in string, needs conversion
    encoded_hex = hashlib.md5(input_string.encode())
    print("encoded_hex = " + encoded_hex.hexdigest() + "\n")

main()
