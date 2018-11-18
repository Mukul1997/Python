scores = {'John':86.5,'Jack':91.2,'Jill':84.5,'Harry':72.1,'Joe':80.5}
print(scores)

s = { k:scores[k] for k in sorted(scores, key=scores.get, reverse=True) }
print(s)

avg = sum(scores.values())/len(scores.values())
print("Average : ",avg)
