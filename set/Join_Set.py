set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set3 = setl.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
setl.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set1 = {"google", "microsorft", "apple"}
set1.intersection_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set1 = {"google", "microsorft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)