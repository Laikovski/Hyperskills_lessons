# Stage 1/6: Making coffee

print('Starting to make a coffee')
print('Grinding coffee beans')
print('Boiling water')
print('Mixing boiled water with crushed coffee beans')
print('Pouring coffee into the cup')
print('Pouring some milk into the cup')
print('Coffee is ready!')

# Stage 2/6: Ingredient calculator

print('Write how many cups of coffee you will need:')
val = int(input())
print(f'For {val} cups of coffee you will need:')
print(f'{val * 200} ml of water')
print(f'{val * 50} ml of milk')
print(f'{val * 15} g of coffee beans')

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

# Stage 4/6: Buy, fill, take!

class CoffeeMachine():
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def print_info(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')

    def buy_coffee(self, choose):
        if choose == '1':
            self.water = self.water - 250
            self.coffee = self.coffee - 16
            self.money = self.money + 4
        elif choose == '2':
            self.water = self.water - 350
            self.milk = self.milk -75
            self.coffee = self.coffee - 20
            self.money = self.money + 7
        elif choose == '3':
            self.water = self.water - 200
            self.milk = self.milk - 100
            self.coffee = self.coffee - 12
            self.money = self.money + 6
        self.cups = self.cups - 1
    def fill_machine(self, water, milk, coffee, cups):
        self.water = self.water + water
        self.milk = self.milk + milk
        self.coffee = self.coffee + coffee
        self.cups = self.cups + cups
    def give_money(self):
        self.money = self.money - self.money
first_machine = CoffeeMachine(400, 540, 120, 9, 550)
first_machine.print_info()

user_input = input('\nWrite action (buy, fill, take): ')

if user_input == 'buy':
    select = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')
    first_machine.buy_coffee(select)
if user_input == 'fill':
    water = int(input('Write how many ml of water you want to add: '))
    milk = int(input('Write how many ml of milk you want to add: '))
    coffee = int(input('Write how many grams of coffee beans you want to add:'))
    cups = int(input('Write how many disposable coffee cups you want to add:'))
    first_machine.fill_machine(water, milk, coffee, cups)
if user_input == 'take':
    out = first_machine.money
    print(f'I gave you ${out}')
    first_machine.give_money()
print('')
first_machine.print_info()

# Stage 5/6: Keep track of the supplies

class CoffeeMachine():
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def print_info(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')

    def buy_coffee(self, choose):
        print('I have enough resources, making you a coffee!')
        if choose == '1':
            self.water = self.water - 250
            self.coffee = self.coffee - 16
            self.money = self.money + 4
        elif choose == '2':
            self.water = self.water - 350
            self.milk = self.milk -75
            self.coffee = self.coffee - 20
            self.money = self.money + 7
        elif choose == '3':
            self.water = self.water - 200
            self.milk = self.milk - 100
            self.coffee = self.coffee - 12
            self.money = self.money + 6
        self.cups = self.cups - 1

    def fill_machine(self, water, milk, coffee, cups):
        self.water = self.water + water
        self.milk = self.milk + milk
        self.coffee = self.coffee + coffee
        self.cups = self.cups + cups
    def give_money(self):
        self.money = self.money - self.money
first_machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    user_input = input('\nWrite action (buy, fill, take, remaining, exit): ')

    if user_input == 'remaining':
        print('')
        first_machine.print_info()
    if user_input == 'buy':
        select = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')

        if select == '1' and first_machine.water >= 250 and first_machine.coffee >= 16:
            first_machine.buy_coffee(select)
        elif select == '2' and first_machine.water >= 350:
            first_machine.buy_coffee(select)
        elif select == '3' and first_machine.water >= 200:
            first_machine.buy_coffee(select)
        else:
            print('Sorry, not enough water!')
    if user_input == 'fill':
        water = int(input('Write how many ml of water you want to add: '))
        milk = int(input('Write how many ml of milk you want to add: '))
        coffee = int(input('Write how many grams of coffee beans you want to add:'))
        cups = int(input('Write how many disposable coffee cups you want to add:'))
        first_machine.fill_machine(water, milk, coffee, cups)
    if user_input == 'take':
        out = first_machine.money
        print(f'I gave you ${out}')
        first_machine.give_money()
    if user_input == 'exit':
        break

# Stage 6/6: Brush up your code
class CoffeeMachine():
    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def print_info(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')

    def buy_coffee(self, choose):
        print('I have enough resources, making you a coffee!')
        if choose == '1':
            self.water = self.water - 250
            self.coffee = self.coffee - 16
            self.money = self.money + 4
        elif choose == '2':
            self.water = self.water - 350
            self.milk = self.milk -75
            self.coffee = self.coffee - 20
            self.money = self.money + 7
        elif choose == '3':
            self.water = self.water - 200
            self.milk = self.milk - 100
            self.coffee = self.coffee - 12
            self.money = self.money + 6
        self.cups = self.cups - 1

    def fill_machine(self, water, milk, coffee, cups):
        self.water = self.water + water
        self.milk = self.milk + milk
        self.coffee = self.coffee + coffee
        self.cups = self.cups + cups
    def give_money(self):
        self.money = self.money - self.money
first_machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    user_input = input('\nWrite action (buy, fill, take, remaining, exit): ')

    if user_input == 'remaining':
        print('')
        first_machine.print_info()
    if user_input == 'buy':
        select = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ')

        if select == '1' and first_machine.water >= 250 and first_machine.coffee >= 16:
            first_machine.buy_coffee(select)
        elif select == '2' and first_machine.water >= 350:
            first_machine.buy_coffee(select)
        elif select == '3' and first_machine.water >= 200:
            first_machine.buy_coffee(select)
        else:
            print('Sorry, not enough water!')
    if user_input == 'fill':
        water = int(input('Write how many ml of water you want to add: '))
        milk = int(input('Write how many ml of milk you want to add: '))
        coffee = int(input('Write how many grams of coffee beans you want to add:'))
        cups = int(input('Write how many disposable coffee cups you want to add:'))
        first_machine.fill_machine(water, milk, coffee, cups)
    if user_input == 'take':
        out = first_machine.money
        print(f'I gave you ${out}')
        first_machine.give_money()
    if user_input == 'exit':
        break
