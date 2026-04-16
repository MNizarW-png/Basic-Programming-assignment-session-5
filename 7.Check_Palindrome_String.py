x = input("Input words: ")
y = ""
for abjad in x:
    y = abjad + y
if (x == y):
    print(f"{x} Is Palindrome")
else:
    print(f"{x} Is Not Palindrome")