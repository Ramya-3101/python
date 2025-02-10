word=input("enter a word: ")
#revwords=word[1::-1]
if word==word[::-1]:
    print("palindrome")
else:
    print("not palindrome")