start = ''' After gaining all of the infinity stones and destroying half of the universe, Thanos is looking for his next meal.'''

keepplaying = "yes"
print(start)

while keepplaying == "Yes" or keepplaying == "yes":
    userchoice = input(" Should he go to eat at Subway or McDonald's? Type 1 for Subway and Type 2 for McDonald's.")
    if userchoice == "1":
        print("You have made the wrong choice and have caused Thanos to destroy the other half of the universe.")
        print("Reality is often disappointing")
        print("")
        keepplaying = input("Would you like to try again? Type yes or no.")
        if keepplaying == "no":
            quit()
    elif userchoice == "2":
        print("Congratulations! You have made the correct choice. All Thanos had been looking for was a happy meal.")
        print("The joy of his happy meal has changed Thanos's mind and he reversed the destruction he has caused.")
        keepplaying = "no"
    else:
        print("Please select one of the valid options: 1 or 2.")
        keepplaying = input("Would you like to try again? Type yes or no.")
        if keepplaying == "no":
            quit()

keepplaying = "yes"
while keepplaying == "yes" or keepplaying == "Yes":
    userchoice = input("A couple hours after eating lunch and the happiness gained from the happy meal wares off, Thanos begins to return to thoughts of destroying the Universe. Should he start by destroying the Avengers or destroying the Infinity Gauntlet. Type 1 for Avengers and Type 2 for Infinity Gauntlet.")
    if userchoice == "1":
        print("You made the wrong choice and Thanos ends up completing his ultimate goal of destroying the whole Universe.")
        print("This is the end of Avengers and there is no longer any heros to protect and save the Universe.")
        keepplaying = input("Would you like to try again? Type yes or no.")
    elif userchoice == "2":
        print("Congratulations! You made the right choice.")
        print("Thanos ends up destroying the Infinity Gauntlet and hides in a Garden. The Avengers locate Thanos and realize that the Ifinity Gauntlet is gone. This sets a challenge for the remaining Avengers and results in the reversal of all the destruction that Thanos had created. ")
        print("")
        keepplaying = "no"
    else:
        print("Please select one of the vaild options: 1 or 2.")
        keepplaying = input("Would you like to try again? Type yes or no.")
    if keepplaying == "no":
        quit()
