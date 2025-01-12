my_shopping_list = ["bread", "milk", "butter"]
## To remove the duplicates we use SETS
print(len(my_shopping_list))
print(my_shopping_list[1])


def bring_food(my_shopping_list):
    pass


l = bring_food(my_shopping_list)


def bring_more_food(my_shopping_list):
#    my_shopping_list.append("cheese")
    more_item = input("Enter Item: ")
    my_shopping_list.append(more_item)
#    my_shopping_list.remove(more_item)
#    my_shopping_list.insert(0,more_item)
    return my_shopping_list


l = bring_more_food(my_shopping_list)
print(l)
