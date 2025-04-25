# Decode the message:
# A message containing the letters from A-Z can be encoded into the numbers using the mapping
# A-> 1, B-> 2, C-> 3, ..., Z-> 26. To decode an encoded message, you need to group the digits
# and do the reverse mapping. You are required to display all the possible decoded messages.
# For example: "11106" can be decoded into:
# a. "AAJF" with the grouping (1 1 10 6)
# b. "KJF" with the grouping (11 10 6)


def decode_message(s, current="", index=0):
    if index == len(s):
        print(current)
        return

    num1 = int(s[index])
    if 1 <= num1 <= 9:
        decode_message(s, current + chr(64 + num1), index + 1)

    if index + 1 < len(s):
        num2 = int(s[index : index + 2])
        if 10 <= num2 <= 26:
            decode_message(s, current + chr(64 + num2), index + 2)


def get_encoded_message():
    while True:
        message = input("Enter the encoded message (digits only): ")
        if message.isdigit():
            return message
        else:
            print("Invalid input. Please enter digits only.")


while True:
    print("\nMessage Decoder:")
    print("1. Decode a message")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        encoded_message = get_encoded_message()
        print("Possible decoded messages:")
        decode_message(encoded_message)
    elif choice == "2":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
