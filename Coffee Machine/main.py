# Stage 1/6: Making coffee

# print('Starting to make a coffee')
# print('Grinding coffee beans')
# print('Boiling water')
# print('Mixing boiled water with crushed coffee beans')
# print('Pouring coffee into the cup')
# print('Pouring some milk into the cup')
# print('Coffee is ready!')

# Stage 2/6: Ingredient calculator

# print('Write how many cups of coffee you will need:')
# val = int(input())
# print(f'For {val} cups of coffee you will need:')
# print(f'{val * 200} ml of water')
# print(f'{val * 50} ml of milk')
# print(f'{val * 15} g of coffee beans')

# Stage 3/6: Estimate the number of servings
import math
print('Write how many ml of water the coffee machine has:')
val_water = int(input()) / 200
print('Write how many ml of milk the coffee machine has:')
val_milk = int(input()) / 50
print('Write how many grams of coffee beans the coffee machine has:')
val_coffee = int(input()) / 15
print('Write how many cups of coffee you will need:')
count_cup = int(input())

result_cup = math.floor(min([val_water, val_milk, val_coffee]))
# print(result_cup)
if result_cup == count_cup:
    print('Yes, I can make that amount of coffee')
elif result_cup < count_cup:
    print(f'No, I can make only {round(result_cup)} cups of coffee')
elif result_cup > count_cup:
    dif = math.floor(result_cup) - count_cup
    print(f'Yes, I can make that amount of coffee (and even {dif} more than that)')
