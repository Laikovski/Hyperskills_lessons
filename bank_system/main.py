import random
import sqlite3
import sys
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
login_card = ''
# cur.execute("DROP TABLE card")
main_menu = True
class Account:
    IIN = "400000"
    # check_digit = "4"

    def __init__(self):
        self.card_number = self.new_card_number()
        self.card_pin = str(random.randint(1111, 9999))

    def new_card_number(self):
        customer_account_number = random.randint(111111111, 999999999)
        account = Account.IIN + str(customer_account_number)
        check_sum = 0
        for i in range(15):
            if i % 2 == 0:
                n = int(account[i]) * 2
                check_sum += n if n < 10 else (n - 9)
            else:
                check_sum += int(account[i])
        check_digit = (10 - (check_sum % 10))  if (check_sum % 10) != 0 else 0
        return account + str(check_digit)


def choose_action():
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    action = input()
    return action


def create_account():
    new_card = Account()
    add_card_to_db(new_card.card_number, new_card.card_pin)
    print("Your card number:\n" + new_card.card_number)
    print("Your card PIN:\n" + new_card.card_pin)

def check_balance_db(card):
    cur.execute("SELECT number, balance FROM card WHERE number = :card", {'card': card[0]})
    card_balance = cur.fetchone()
    print(f'Balance {card_balance[1]}')
    return card_balance

def account_page(card):

    def account_menu():
        print('1. Balance')
        print('2. Add income')
        print('3. Do transfer')
        print('4. Close account')
        print('5. Log out')
        print('0. Exit')
        action_acc = input()
        return action_acc

    def add_money():
        current_balance = check_balance_db(card)
        print('Enter income:')
        insert_balance = int(input())
        result_sum = current_balance[1] + insert_balance
        cur.execute("UPDATE card SET balance = :sum WHERE number = :card",
                    {'card': current_balance[0], 'sum': result_sum})
        conn.commit()
        print('Income was added!')
        account_page(card)

    def transfer_money(card):
        print('Enter card number:')
        insert_card = input()
        global temp
        temp = True
        while temp == True:
            i = 0
            odd_number = 0
            while i < len(insert_card):
                temp = int(insert_card[i]) * 2
                if temp >= 10:
                    temp = temp - 9
                    odd_number += temp
                else:
                    odd_number += temp
                i += 2
            k = 1
            even_number = 0
            while k < len(insert_card):
                even_number += int(insert_card[k])
                k += 2
            if (odd_number + even_number) % 10 == 0:
                cur.execute("SELECT number, pin FROM card WHERE number = :card_user", {'card_user': insert_card})
                card_user = cur.fetchone()
                if not card_user:
                    print('Such a card does not exist.')
                    account_page(card)
                print('Enter how much money you want to transfer:')
                insert_sum = int(input())
                cur.execute("SELECT number, balance FROM card WHERE number = :card", {'card': card[0]})
                card_balance = cur.fetchone()

                if card_balance[1] < insert_sum:
                    print('Not enough money!')
                    account_page(card)
                else:
                    res = card_balance[1] - insert_sum
                    cur.execute("UPDATE card SET balance = :sum WHERE number = :card",
                                {'card': card[0], 'sum': res})

                    cur.execute("SELECT number, balance FROM card WHERE number = :insert_card", {'insert_card': insert_card})
                    insert_card = cur.fetchone()
                    add_balance = insert_card[1] + insert_sum
                    print(add_balance)
                    cur.execute("UPDATE card SET balance = :sum WHERE number = :card",
                                {'card': insert_card[0], 'sum': add_balance})
                    conn.commit()

                    temp = False
                    print('Success!')
                    account_page(card)
                    break
            elif (odd_number + even_number) % 10 != 0:
                print('Probably you made a mistake in the card number. Please try again!')
                account_page(card)
                break
    def close_account(card):
        cur.execute("DELETE FROM card WHERE number = :card", {'card': card[0]})
        cur.fetchone()
        conn.commit()
        print('The account has been closed!')

    def log_out():
        pass

    while True:
        action_acc = account_menu()
        if action_acc == '0':
            login_card = ''
            global main_menu
            main_menu = False
            temp = False
            print('Bye!')
            sys.exit()

        if action_acc == '1':
            res = check_balance_db(card)
            print(res[1])
        elif action_acc == '2':
            add_money()
        elif action_acc == '3':
            transfer_money(card)
        elif action_acc == '4':
            close_account(card)
        elif action_acc == '5':
            log_out(card)

        break
        # account_menu()

def log_into_account():
    card = input("Enter your card number:")
    pin = input("Enter your PIN:")
    cur.execute("SELECT number, pin FROM card WHERE number = :card", {'card': card})
    card = cur.fetchone()
    global login_card
    login_card = card
    if not card:
        print("Wrong card number or PIN!")
    elif card[1] == pin:
        print("You have successfully logged in!")
        account_page(card)
    else:
        print("Wrong card number or PIN!")


def add_card_to_db(card_number, card_pin):
    cur.execute("INSERT INTO card (number, pin) VALUES (:number, :pin)",
                {'number': card_number, 'pin': card_pin})
    conn.commit()


def create_db():
    # cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS card (
                id INTEGER,
                number TEXT,
                pin TEXT,
                balance INTEGER DEFAULT 0
                )""")
    conn.commit()

# cur.execute("DROP TABLE card")
# conn.commit()
create_db()
while main_menu == True:
    action = choose_action()
    if action == "1":
        create_account()
    elif action == "2":
        log_into_account()
    elif action == "0":
        print('Bye!')
        break


conn.close()