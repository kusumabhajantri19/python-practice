special_food = {"bengaluru":"bisi bath",
           "mysore":"Mysore pak",
           "mangalore":"neer dosa",
           "belagavi":"kara",
           "gok":"karan",
           }
print(special_food["mysore"])
print(special_food.get("dharawad"))
special_food["udupi"] = "shira"
print(special_food)
del special_food["mangalore"]
print(special_food)
# special_food.pop("belagavi")
# print(special_food)
# special_food.clear()
# print(special_food)


print(special_food.keys())
print(special_food.values())
print(special_food.items())
new_dishes = {"hubbli":"peda",
              }
special_food.update(new_dishes)
print(special_food)
