# python基础知识学习， 实践

import random

randnum = random.randint(1, 10)
i = 0
while i < 5:
    temp = input("pls input num:")
    num = int(temp)
    if num == randnum:
        print("yes")
        break
    else:
        print("no")
        if num > randnum:
            print("it's little than", num)
        else:
            print("it's bigger than", num)
    i = i + 1
else:
    print("sorry no times !")

print("End")
