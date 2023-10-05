f = open("Alice.txt","r",encoding = "UTF8")

book = f.read()
words = []

print("검색하려고 하는 단어를 5객 입력하세요:")
for _ in range(5):
    words.append(input())
for word in words:
    n = book.count(word)
    print("%s : %d번" %(word,n))
f.close()
