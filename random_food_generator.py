adjective_list = ["spicy ","creamy ","sweet ","yummy ","juicy ","bitter ","cheesy ","cold "]
cooking_style_list = ["steamed ","barbecue ","fried ","roasted ","microwaved ","smoked ","pickled ","juiced "]
food_item_list = ["onions","rice","chicken","broccoli","human toes","salad","nachos","lemonade"]
import random
random_index = random.randint(0,7)
print("\n")
print("If you are hungry try...")
print(adjective_list[random_index] + cooking_style_list[random_index] + food_item_list[random_index])

input()