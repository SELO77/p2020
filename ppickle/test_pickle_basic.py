import pickle
from pprint import pprint

my_list = ['a', 'b', 'c']
my_dict = {'a':1 , 'b': 2}

## Save pickle
with open("data.pickle", "wb") as fw:
    pickle.dump(my_dict, fw)

## Load pickle
with open("data.pickle", "rb") as fr:
    data = pickle.load(fr)

pprint(data)
