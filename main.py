import funkcjesql as fsql
import sys

# ----------------------------------------------------------------
fsql.create_table()
fsql.admin_panel()

try:
    while True:
        while True:
            
            print()
            print("1. Zaloguj się")
            print("2. Zarejestruj się")
            print("5. Wyjdź")

            try:
                user_choice = int(input("Wybierz liczbę: "))
            except:
                user_choice = 0
                print("Nieprawidłowy format!")
            print()
            if user_choice == 1:
                username=input("Podaj nazwę użytkownika:")
                password=input("Podaj hasło:")
                if fsql.login(username,password)==1:
                    break
                
            if user_choice == 2:
                username=input("Podaj nazwę użytkownika:")
                password=input("Podaj hasło(min. 8 znaków):")
                if fsql.register(username,password)==1:
                    continue
                

            if user_choice == 3:
                print("3")
            if user_choice == 5:
                fsql.connection.close()
                sys.exit()

        while True:
            print()
            print("1. Pokaż zadania")
            print("2. Dodaj zadanie")
            print("3. Usuń zadanie")
            print("4. Zmień status")
            print("5. Wyjdź/Wyloguj")


            try:
                user_choice = int(input("Wybierz liczbę: "))
            except:
                user_choice = 0
                print("Nieprawidłowy format!")
            print()
            if user_choice == 1:
                fsql.show_tasks()
                
            if user_choice == 2:
                task = input("Wpisz treść zadania: ")
                category= input("Wpisz kategorie zadania(dom, ogród, praca, inny): ")
                fsql.add_task(task,category)

            if user_choice == 3:
                task_index=input("Podaj indeks zadania do usunięcia: ")
                fsql.delete_task(task_index)
            if user_choice == 4:
                task_index=input("Wpisz indeks zadania: ")
                modify_task=input("1.Jeśli zrobiłeś zrobiłeś \n2.Jeśli jesteś w trakcie robienia\n3.Jeśli do zrobienia\nNumer: ")
                fsql.f_modify_task(task_index,modify_task)
            if user_choice == 5:
                break
finally:
    print("Wyjście z aplikacji")
    fsql.connection.close()