"""Functions to automate Conda airlines ticketing system."""
SEAT_LETTERS = "ABCD"

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    for count in range(number):
        yield SEAT_LETTERS[count%4]

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    current_row = 0
    seat_letters = generate_seat_letters(number)
    for seat in seat_letters:
        if seat == "A":
            current_row += 1
            if current_row == 13:
                current_row += 1
        yield str(current_row)+seat

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat_codes = generate_seats(len(passengers))
    current_seat_index = 0
    passenger_information = {}
    for passenger in passengers:
        passenger_information[passenger] = seat_codes.__next__()
        current_seat_index += 1
    return passenger_information

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        return_code = seat+flight_id
        yield return_code + "0"*(12-len(return_code))
