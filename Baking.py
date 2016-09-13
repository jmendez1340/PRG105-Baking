# 240  ml = 1 cup

# Put the function at the top
# ml acts as the local variable

def convert(ml):
    cup = round((float(ml)/240 ),5)
    return cup

print "ml will be converted into cups"
ml = raw_input("How many ml? ")
cup = convert(ml)
print (ml + "ml is equal to " + str(cup) + " cup(s)")