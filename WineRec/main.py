
## set of questions 
global region_q
region_q = "are you looking for a wine from a specific region, or are you open to exploring different options? "


## Chardonnay

def Chardonnay():
    print(region_q)
    region = input("answer: ")
    print(region)


Chardonnay()