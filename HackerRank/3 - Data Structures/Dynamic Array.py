def dynamicArray(n, queries):
        seq = [[] for _ in range(n)]
        res = []
        lastAnswer = 0
        
        for t, x, y in queries:
                idx = (x ^ lastAnswer) % n
                if t == 1:
                        seq[idx].append(y)
                else:
                        s = seq[idx]
                        lastAnswer = s[y % len(s)]
                        res.append(lastAnswer)
        return res