my_dict = {'Niko' : 1986, 'Jon' : 1993}
print(my_dict)
print(my_dict['Niko'])
my_dict['Kendric'] = 1979
print(my_dict['Kendric'])
my_dict.update({'Max' : 1997,
                'Helga' : 1999})
my_dict.pop('Max')
print(my_dict.get('Max'))
print(my_dict)


my_set = {1, 2, 3, 4, 5, 6, 'apple', True,
          1, 2, 3, 4, 5, 6, 'apple', True,
          1, 2, 3, 4, 5, 6, 'peach', False}
print(set(my_set))
my_set.add(8)
my_set.add(13)
my_set.remove(1)
print(my_set)