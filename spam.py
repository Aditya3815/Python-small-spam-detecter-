text = input("Enter the text")

if("make a lot of money" in text):
    spam = True 
elif("click this" in text):
    spam =True 
elif("subscribe this" in text):
    spam = True 
else:
    spam = False          