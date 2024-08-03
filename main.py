from cts import CinemaTicketSystem

def main():
    cinemaSystem = CinemaTicketSystem()
    
    while True:
        
        print("\n_______________________________________________________")
        print("\nЗдравствуйте, у вас есть следующие доступные функции:")
        print("1. Добавить новый фильм")
        print("2. Показать все доступные фильмы")
        print("3. Добавить нового пользователя")
        print("4. Купить билет")
        print("5. Отменить покупку билета")
        print("6. Выйти")
        print("_______________________________________________________")
        choice = input("Введите номер выбранной функции: ")

        if choice == '1':
            movieName = input("Введите название фильма: ")
            movie_id = cinemaSystem.addMovie(movieName)
            print(f"Фильм {movieName} с номером {movie_id}  успешно добавлен")

        elif choice == '2':
            cinemaSystem.showAllMovies()

        elif choice == '3':
            userName = input("Введите имя пользователя: ")
            user_id = cinemaSystem.addUser(userName)
            print(f"Пользователь {userName} с номером {user_id} добавлен")

        elif choice == '4':
            userId = int(input("Введите номер пользователя: "))
            movieId = int(input("Введите номер фильма: "))
            ticket_id = cinemaSystem.buyTicket(userId, movieId)
            if ticket_id:
                print(f"Привет, {cinemaSystem.users[userId]}! Билет на фильм <<{cinemaSystem.movies[movie_id]}>> c номером: {ticket_id} успешно куплен")

        elif choice == '5':
            ticketId = int(input("Введите номер билета: "))
            success = cinemaSystem.cancelTicket(ticketId)
            if success:
                print("Билет успешно отменен")
            else:
                print("Билет с таким номером не найден")

        elif choice == '6':
            break

        else:
            print("Неверный ввод, попробуйте снова")

if __name__ == "__main__":
    main()
