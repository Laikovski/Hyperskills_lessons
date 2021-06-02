# Coffee Machine 

## Stage 1/6: Making coffee

    The first version of the program just makes you a coffee. It should print to the standard output what it is doing as it makes the drink.

## Stage 2/6: Ingredient calculator

    - First, read the numbers of coffee drinks from the input.
    - Figure out how much of each ingredient the machine will need. Note that one cup of coffee made on this coffee machine contains 200 ml of water, 50 ml of milk, and 15 g of coffee beans.
    - Output the required ingredient amounts back to the user.

## Stage 3/6: Estimate the number of servings 
    
    - It requests the amounts of water, milk, and coffee beans available at the moment, and then asks for the number of cups a user needs.
    - If the coffee machine has enough supplies to make the specified amount of coffee, the program should print "Yes, I can make that amount of coffee".
    - If the coffee machine can make more than that, the program should output "Yes, I can make that amount of coffee (and even N more than that)", where N is the number of additional cups of coffee that the coffee machine can make.
    - If the amount of given resources is not enough to make the specified amount of coffee, the program should output "No, I can make only N cups of coffee".
