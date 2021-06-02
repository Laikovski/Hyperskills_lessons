# Bill Splitter
## Stage 1/4: Invite your friends 

    
    - Take user input — how many people want to join, including the user;
    - In case of an invalid number of people (zero or negative), "No one is joining for the party" is expected as an output;
    - Otherwise, take the friends' names as input, iteratively;
    - Store them in a dictionary initialized with zeros;
    - Print out the dictionary.

## Stage 2/4: The bill has arrived

    
    - If there are no people to split the bill (the number of friends is 0 or an invalid input), output "No one is joining for the party";
    - Else, take user input: the final bill;
    - Split the total bill equally among everyone;
    - Round up the split value to two decimal places;
    - Update the dictionary with the split values;
    - Print the updated dictionary.

## Stage 3/4: The Lucky One 
    
    - In case of an invalid number of people, "No one is joining for the party" is expected as an output;
    - Otherwise, ask the user whether they want to use the "Who is lucky?" feature;
    - Take input from the user;
    - If a user wants to use the feature (Yes), choose a name from the dictionary keys at random and print the following: {Name} is the lucky one!;
    - If the user enters anything else, print No one is going to be lucky.

## Stage 4/4: Party is over

    - In case of an invalid number of people, "No one is joining for the party" is expected as an output;
    - Otherwise, if the user choice is Yes, re-split the bill according to the feature;
    - Round up the split value to two decimal places;
    - Update the dictionary with new split values and 0 for the lucky person;
    - Print the updated dictionary;
    - If the user entered anything else instead of Yes, print the original dictionary.
