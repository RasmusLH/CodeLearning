# Script that takes a user input string and encodes it using a simple algorithm

def encode(string):
    encoded = ""
    for char in string:
        encoded += chr(ord(char) + 1)
    return encoded


def decode(string):
    decoded = ""
    for char in string:
        decoded += chr(ord(char) - 1)
    return decoded

print(encode(input("Enter a string to encode: ")))

print(decode(input("Enter your encoded string to decode it: ")))