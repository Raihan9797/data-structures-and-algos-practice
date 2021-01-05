# Problem: Default List - https://www.codewars.com/kata/5e882048999e6c0023412908
# collections module has a defaultdict, which gives you a defaultvalue when you try to get the value for a key that doesn't exist. Do it for lists now!


# Examples
# lst = DefaultList(['hello', 'abcd', '123', 123, True, False], 'default_value')
# lst[4] = True
# lst[80] = 'default_value'
# lst.extend([104, 1044, 4066, -2])
# lst[9] = -2



''' What i learned
## Technical ##
1. Learnt about inheritance! 
- Didn't know how to inherit the other methods and so i had to implement each method on my own

2. Making use of try and except to make the feature easier to implement!


3. Reminder that python lists can access in reverse!
- the maximum negative number is the same as the length of the list!!
my_list = [1, 2, 3, 4, 5, 6]
len(my_list) # 6
my_list[-7] # error!

## Non-technical ##

'''

## My Solution ##
class DefaultList():

    def __init__(self, lst, default_val):
        self.lst = lst
        self.default_val = default_val
    
    def __getitem__(self, index):
        print('GETTING')
        if not self.lst: return self.default_val
        negative_length = -1 * len(self.lst)
        if (index < negative_length or index >= len(self.lst)): return self.default_val
        return self.lst[index]

    def extend(self, another_list):
        print('GETTING')
        # if not self.lst: return self.default_val
        print(self.lst)
        self.lst.extend(another_list)
        return self.lst
    
    def append(self, new_ele):
        print(self.lst)
        if not self.lst: return self.default_val
        self.lst.append(new_ele)
        return self.lst
    
    def insert(self, index, new_ele):
        if not self.lst: return self.default_val
        self.lst.insert(index, new_ele)
        return self.lst
    
    def pop(self, index=-1):
        if not self.lst: return self.default_val
        self.lst.pop(index)
        return self.lst
    
    def remove(self, ele):
        if not self.lst: return self.default_val
        self.lst.remove(ele)
        print(self.lst)
        return self.lst




## Better Solution ##
class DefaultList(list):
    def __init__(self,it, default):
        super().__init__(it)
        self.default=default
    
    def __getitem__(self,i):
        try: return super().__getitem__(i)
        except IndexError: return self.default


## Testing ##
lst = DefaultList([1, 3, 4, 7, 2, 34], 'def')

lst.extend([3, 23, 'hello', 'lists', 'word', 344])

lst.append(233344455)
lst[12] # 233344455)
lst[100] # 'def')

lst.remove(2)
lst.remove(1)
lst.remove(3)
lst.insert(-3, 34.34)

lst[8]  # 'word')
lst[10]  # 233344455