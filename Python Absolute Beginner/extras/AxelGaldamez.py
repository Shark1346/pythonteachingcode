# [ ] create, call and test fishstore() function 
# This is the defining the fishstore function()
def fishstore(fish, price): 
    report= "Report for Axel Galdamez. Fish Type: "+ fish+ "costs $"+ price
    return report
fish_entry = input("Please enter a fish type: ").capitalize()
price_entry= input ("How much does the fish cost?: ")
print(fishstore(fish_entry, price_entry))
