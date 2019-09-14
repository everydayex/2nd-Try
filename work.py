work = {'Week1': '40hrs', 'Week2': '35hrs', 'Week3': '48hrs'}


while True:

    print('Enter work week')
    week_number = input()
    if not week_number:
        print("Week not found")


    week_hours = int(input("Enter how many hours you worked this week"))
    if week_hours == '':
        break


    if week_hours >= 40:
        print("Eligible for overtime pay")
    elif week_hours <= 40:
        print("Not eligible for overtime pay")


