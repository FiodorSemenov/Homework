'''

All of the animals are having a feast! Each animal is bringing one dish.
There is just one rule: the dish must start and end with the same 
letters as the animal's name. For example, the great blue heron is 
bringing garlic naan and the chickadee is bringing chocolate cake.
Write a function feast that takes the animal's name and dish as arguments
and returns true or false to indicate whether the beast is allowed to 
bring the dish to the feast. Assume that beast and dish are always 
lowercase strings, and that each has at least two letters. 
beast and dish may contain hyphens and spaces, but these will not appear
at the beginning or end of the string. They will not contain numerals.

'''

import string

animal = str(input("введите название животного \t"))
dish = str(input("введите название блюда \t"))

if (animal[0] == dish[0]) and (animal[-1] == dish[-1]):
    if (animal[0] in string.ascii_lowercase) and (
            animal[-1] in string.ascii_lowercase):
        if len(animal) >= 2 and len(dish) >= 2:
            if str.isalpha(animal) and str.isalpha(dish):
                print("this animal can bring this dish to the feast")
            else:
                if animal.find(" ") or animal.find(
                        "-") or dish.find("-") or dish.find(" "):
                    animal = animal.replace("-", "")
                    animal = animal.replace(" ", "")
                    dish = dish.replace(" ", "")
                    dish = dish.replace("-", "")
                    if str.isalpha(animal) and str.isalpha(dish):
                        print("this animal can bring this dish to the feast")
                    else:
                        print("this animal cannot bring this dish to the feast")
                else:
                    print("this animal cannot bring this dish to the feast")
        else:
            print("this animal cannot bring this dish to the feast")
    else:
        print("this animal cannot bring this dish to the feast")
else:
    print("this animal cannot bring this dish to the feast")
