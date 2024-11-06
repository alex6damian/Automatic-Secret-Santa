from random import randint
def make_pairs(names):
    pairs=[]
    names1 = names.copy()
    i=0
    
    while i<len(names)-1:
        index=randint(0,len(names1)-1)
        
        if names[i]["Nume"] != names1[index]["Nume"]:
            pairs.append((names[i],names1[index]))
            names1.pop(index)
            i+=1
    
    return pairs
