vec = [-4, -2, 0, 2, 4]
#vecs = [x*2 for x in vec]
#print (vecs)

#vec1 = [x for x in vec if x <= -0]
vec1 =[abs(x) for x in vec]
print (vec1)
