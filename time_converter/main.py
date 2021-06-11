from datetime import datetime
from data import hours, hours_equal, minutes

current_time = datetime.now()

def convert_time(value):
    '''Convert time from digit to string'''

# if time has '00' minutes
    if value[1] == 0:
        if value[0] == 0:
            print(f'{hours_equal[value[0]]} часов (полночь)')
        elif value[0] == 1 or value[0] == 13:
            print(f'{hours_equal[value[0]]} час ровно')
        elif 1 < value[0] <= 4 or 13 < value[0] <= 16:
            print(f'{hours_equal[value[0]]} часа ровно')
        elif 4 < value[0] <= 12 or 16 < value[0] <= 24:
            print(f'{hours_equal[value[0]]} часов ровно')

# if time has '01-29' and '31-44' minutes
    if 1 <= value[1] < 30 or 31 <= value[1] < 45:
        if value[1] == 1 or value[1] == 21 or value[1] == 31 or value[1] == 41:
            print(f'{minutes[value[1]]} минута {hours[value[0] + 1]}')
        elif 2 <= value[1] < 5 or 22 <= value[1] < 25 or 32 <= value[1] < 35 or 42 <= value[1] < 45:
            print(f'{minutes[value[1]]} минуты {hours[value[0] + 1]}')
        elif 5 <= value[1] < 21 or 25 <= value[1] < 30 or 36 <= value[1] < 41:
            print(f'{minutes[value[1]]} минут {hours[value[0] + 1]}')

# if time has '45-59' minutes
    if 45 <= value[1] < 60:
        if value[1] < 51:
            print(f'без {minutes[value[1]]} минут {hours[value[0] + 1]}')
        elif value[1] == 59:
            print(f'без {minutes[value[1]]} минуты {hours_equal[value[0] + 1]}')
# if time equal half
    if value[1] == 30:
        print(f'половина {hours[value[0] + 1]}')

def start_program():
    """Choose insert user"""
    your_choose = int(input('Hello, please choose your action. 1 - Print system time. 2 - Insert your time\n'))
    if your_choose == 1:
        time_value_sys = [current_time.hour, current_time.minute]
        convert_time(time_value_sys)
    elif your_choose == 2:
        time_value_user = input('Insert your time please. Format should be 24H (00:00)').split(':')
        time_value_user = [int(x) for x in time_value_user]
        convert_time(time_value_user)

    else:
        print('You can insert only "1" or "2". Try again.')
        start_program()

start_program()