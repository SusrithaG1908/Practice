def removeStars(s: str) -> str:
        stack=[]
        for char in s:
            if char=="*" and stack:
                stack.pop()
            else:
                stack.append(char)
        string=''
        while stack:
            string+=stack.pop()

        return string[::-1]

print(removeStars("leet**cod*e"))