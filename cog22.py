def permutations(s):
    result=[]
    used =[False]*len(s)

    def backtrack(current):
        if len(current)==len(s):
            result.append("".join(current))
            return

        for i in range(len(s)):
            if used[i]:
                continue

            used[i]=True
            current.append(s[i])
            backtrack(current)

            current.pop()
            used[i]=False

    backtrack([])
    return result

print(permutations("abc"))
            