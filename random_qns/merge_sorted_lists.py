# given 2 sorted list, merge them into another sorted list

la = [1, 3 ,7,8,9, 11, 13]
lb = [1, 2 ,3,10, 11 ,12]

"""
ans = []
pop the first elements of both lists
if head of la <= head of lb:
    ans.append(la)
    for a in la:
        if a <= head of lb:
            ans.append(a)
        else:
            return merge

base case:
1. la and lb empty: return []
2. la empty: return lb
3. lb empty: return la

recursive case:
1. if hla <= hlb: 
    ans.append(hla)
    return merge(la.pop(), lb, ans)
2. else:
    ans.append(hlb)
    return merge(la, lb.pop(), ans)
"""


def merge(la, lb, ans = []):
    print(la, lb, ans)
    if not la and not lb:
        return ans
    elif not la and lb:
        return merge(la, [], ans + lb)
    elif la and not lb:
        return merge([], lb, ans + la)
    else:
        heada = la[0]
        headb = lb[0]
        if heada <= headb:
            la.pop()
            return merge(la, lb, ans.append(heada))
        else:
            lb.pop()
            return merge(la, lb, ans.append(headb))

merge(la, lb)

def mergev2(la, lb):
    ans = []
    lena = len(la)
    lenb = len(lb)
    longest = lena if lena >= lenb else lenb
    print(lena, lenb, longest)


mergev2(la, lb)

#print(la + lb)
#emp = []
#print(emp)