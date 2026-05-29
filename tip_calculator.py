def calculate_tip(bill, tip_percentage):
    tip = (bill * tip_percentage) / 100
    total = bill + tip
    return{
        "tip":tip,
        "total":total
    }


result1 = calculate_tip(200,100)
print(result1)
result2 = calculate_tip(400,200)
print(result2)
result3 = calculate_tip(600,400)
print(result3)

#print only display the value in screen
#return gives back the value from a function
