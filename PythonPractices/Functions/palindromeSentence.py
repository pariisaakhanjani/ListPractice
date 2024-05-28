def palindromeSentence(Sentence):
    String = ""
    for char in Sentence:
        if char.isalnum():
            String += char
    return String[: : -1].casefold() == String.casefold()

user_input = input(str("please write a sentence and I will tell you if it is palindrome or not:"))

if palindromeSentence(user_input):
    print("your sentence is Palindrome")
else:
    print("your sentence is not palindrome")