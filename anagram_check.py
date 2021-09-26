# anagrams checking
def anagram(str1,str2):
    s1=str1.lower()
    s2=str2.lower()
    print(sorted(s1))
    print(sorted(s2))
    if sorted(s1)==sorted(s2):
        print("anagrams")
    else:
        print("not a anagrams")


x=input("Enter the first string ")
y=input("Enter the second string ")
anagram(x,y)






































