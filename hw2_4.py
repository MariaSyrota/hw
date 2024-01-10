# Write an algorithm that takes an list and moves all of the zeros to the end, preserving the order of the other elements.
# move_zeros([False,1,0,1,2,0,1,3,"a"]) # returns[False,1,1,2,1,3,"a",0,0]
#
# For test exemples:
# [1,2,0,1,0,1,0,3,0,1]
# [9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]
# ["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]
# ["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]
# [0,1,None,2,False,1,0]
# ["a","b"]
# ["a"]
# [0,0]
# [0]
# [False]
# []





def move_zeros(lst: list) -> list:
    """
    Переміщує всі нулі в кінець списку, залишаючи порядок інших елементів незмінним.

    Параметри:
    lst (list): Список, який містить числа та булеві значення.

    Повертає:
    list: Список, в якому всі нулі розташовані в кінці списку.
    """
    non_zeros = [x for x in lst if x != 0 or isinstance(x, bool)]
    zeros = [x for x in lst if x == 0 and not isinstance(x, bool)]
    return non_zeros + zeros

lst = [False, 1, 0, 1, 2, 0, 1, 3, "a"]
result = move_zeros(lst)
print(result)