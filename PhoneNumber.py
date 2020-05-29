import random
def create_phone_numbers(alist):

    mask = '(xxx) xxx-xxxx'
    
    for x in alist:
        x = random.choice(alist)
        mask = mask.replace('x', str(x))

    return mask
    

print(create_phone_numbers([1,2,3,4,5,6,7,8,9,0]))