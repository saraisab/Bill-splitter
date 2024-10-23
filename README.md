# Bill-splitter
### Hyperskill project


It's the right time to update your dictionary with new split values to make our "Who is lucky?" feature better. First, we need to recalculate the split value for everyone. Make sure that our lucky one pays 0.

Recalculate the split value for n-1 people where n is the total length of the dictionary and update the values in the dictionary with the new split value for everyone.

If a user decides not to use the "Who is lucky" feature, print the original dictionary.
Objectives

In this stage your program should perform the following steps together with the steps from the previous stages:

    In case of an invalid number of people, "No one is joining for the party" is expected as an output;
    Otherwise, if the user choice is Yes, re-split the bill according to the feature;
    Round the split value to two decimal places;
    Update the dictionary with new split values and 0 for the lucky person;
    Print the updated dictionary;
    If the user entered anything else instead of Yes, print the original dictionary.

Examples

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1: The feature is used

Enter the number of friends joining (including you):
> 5

Enter the name of every friend (including you), each on a new line:
> Marc
> Jem
> Monica
> Anna
> Jason

Enter the total bill value:
> 100

Do you want to use the "Who is lucky?" feature? Write Yes/No:
> Yes

Jem is the lucky one!

{'Marc': 25, 'Jem': 0, 'Monica': 25, 'Anna': 25, 'Jason': 25}
