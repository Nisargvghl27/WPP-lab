# Pangrams
# Roy wanted to increase his typing speed for programming contests so, his friend advised him to
# type the sentence “The quick brown for jumps over the lazy dog” repeatedly because it is a
# pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)
# After typing the sentence several times, Roy became bored with is. So he started to look for other
# pangrams.
# Given a sentence s, tell Roy if it is a pangram or not.


def check(str):
    str = str.lower()
    a = "abcdefghijklmnopqrstuvwxyz"
    for i in a:
        if i not in str:
            return False
    return True


str = input("Enter string : ")
if check(str):
    print("pangram")
else:
    print("not pangram")
