class CinemaTicketSystem:
    def __init__(self):
        self.movies = {}
        self.users = {}
        self.tickets = {}
        self.movie_id_counter = 1
        self.user_id_counter = 1
        self.ticket_id_counter = 1

    def addMovie(self, movieName):
        movie_id = self.movie_id_counter
        self.movies[movie_id] = movieName
        self.movie_id_counter += 1
        return movie_id

    def showAllMovies(self):
        for movie_id, movie_name in self.movies.items():
            print(f"{movie_id}. {movie_name}")

    def addUser(self, userName):
        user_id = self.user_id_counter
        self.users[user_id] = userName
        self.user_id_counter += 1
        return user_id

    def buyTicket(self, userId, movieId):
        if userId in self.users and movieId in self.movies:
            ticket_id = self.ticket_id_counter
            self.tickets[ticket_id] = (userId, movieId)
            self.ticket_id_counter += 1
            return ticket_id
        else:
            print("Invalid userId or movieId")
            return None

    def cancelTicket(self, ticketId):
        if ticketId in self.tickets:
            del self.tickets[ticketId]
            return True
        else:
            return False
     
    def getName(self, user_ID):
        return self.movies.get(user_ID)

