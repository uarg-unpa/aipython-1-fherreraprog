#lista con range
lrange=list(range(7))
print(lrange)
#remove
lrange.remove(3)
print(lrange)
#reverse
lrange.reverse()
print(lrange)
#count
lrange.append(2)
print(lrange.count(2))
#sum, min, max
print(sum(lrange))
#del
del(lrange[2])
print(lrange)
del(lrange)
print(lrange)