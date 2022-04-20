import random as np


lst = [13, 4, 20, 15, 6, 20, 20]

lst = np.array(lst)

result = np.where(lst == 20)

print(result)
