phrase = list(input())
hello = 'hello'
for char in 'hello':
    if char in phrase:
        while hello.index(char) != hello.index(char):
            del phrase[hello.index(char)]
        if phrase == hello:
            print("YES")
else:
    print("NO")