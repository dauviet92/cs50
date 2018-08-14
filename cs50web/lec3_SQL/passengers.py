def main():
    #List all flights
    flights = db.execute("SELECT id, origin, destination, duration FROM flight").fetchall()
    for flight in flights:
        print(f"Flight {flight.id} : {flight.origin} to {flight.destination} , {flight.duration})
    #Prompt user to choose a flight:
    flight_id = int(input("\nFlight ID: "))
    flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id = :id", {"id" : flight_id}).fetchone()

    if flight is None:
        print("Erro : No such flight.")
        return
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                        {"flight_id": flight_id}).fetchall()
    print("\nPassengers:")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == 0:
        print("No passegners.")
