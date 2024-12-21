import pandas as pd
#
# # Load the CSV file
# df = pd.read_csv('weight-height.csv')
#
# # Display the first few rows of the DataFrame
# # print(df)
# print(df.head(3))
# print(df.Gender)
users_list = []
user_tmp = []

while True:
    first_name = input('Podaj imię:  ')
    last_name = input('Podaj nazwisko:  ')
    age = int(input('Podaj wiek:  '))
    user_tmp.append(first_name)
    user_tmp.append(last_name)
    user_tmp.append(age)
    if age >= 18:
        user_tmp.append(1234)
    else:
        user_tmp(None)

    print(f'użytkownik {user_tmp} zapisany')
    users_list.append(user_tmp)
    user_tmp = []
    decission = input('Czy chcesz dodać kolejnego użytkownika? t/n')
    if decission[0].lower() == 't':
        print('Ok, dodaj kolejneą osobę')
    elif decission[0].lower() == 'n':
        print('Ok, koniec dodawania osób')
        break
    else:
        print('Nierozpoznany wybór, jeszcze raz')
        decission = input('Czy chcesz dodać kolejną osobę')
        if decission[0].lower() == 't':
            print('Ok, dodaj kolejną osobę')
        else:
            print('koniec dodawania osób')
            break
print(f'Użytkownicy: {users_list}')

