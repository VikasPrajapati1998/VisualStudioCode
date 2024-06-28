# Tuple Varieties
lst_x = [1, 2, 3, 4]
lst_y = [2, 4, 6, 8, 10]
lst_c = [lst_x, lst_y]
print(lst_c)
lst_c = [*lst_x, *lst_y]
print(lst_c)

tpl_x = (1, 2, 3, 4)
tpl_y = (2, 4, 6, 8, 10)
tpl_z = (tpl_x, tpl_y)
print(tpl_z)
tpl_z = (*tpl_x, *tpl_y)
print(tpl_z)
