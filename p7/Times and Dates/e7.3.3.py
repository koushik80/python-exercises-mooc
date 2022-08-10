# E-7.3.3: Screen Time

# Problem: https://programming-22.mooc.fi/part-7/3-times-and-dates#programming-exercise-how-old


# Sample output:


# Solution:
from datetime import datetime, timedelta


def screen_time():

    file = input("Filename: ")

    with open(file, 'w') as new_file:
        total_minutes = []
        print("Filename: ", file)
        start_date = input("Starting date: ")
        start_date = start_date.split('.')
        start_date = datetime(int(start_date[2]), int(
            start_date[1]), int(start_date[0]))
        s_date = start_date.strftime('%d.%m.%y')
        num_days = int(input("How many days: "))
        end_date = start_date + timedelta(days=num_days-1)
        end_date = end_date.strftime('%d.%m.%y')

        print(start_date)
        new_file.write(f'Time period: {s_date} - {end_date}\n')
        print("Please type in screen time in minutes on each day (TV computer mobile): ")
        daily_note = {}
        i = 0

        while i < num_days:
            e_date = start_date + timedelta(days=i)
            time = e_date.strftime('%d.%m.%y')
            user_input = input(f'Screen time {time}: ')
            daily_note[time] = user_input.replace(' ', '/')
            total_minutes.append(user_input)
            i += 1

        p = 0
        for m in total_minutes:
            s = m.split(' ')
            a = [int(i) for i in s]
            for y in a:
                p += y
        mm = p / num_days
        new_file.write(f'Total minutes: {p}\n')
        new_file.write(f'Average minutes: {mm}\n')
        for day_am, time in daily_note.items():
            new_file.write(f'{day_am}: {time}\n')
        print(f'Data stored in file {file}')


screen_time()
