# Reserving Tickets
# Cancelling Tickets
# database=railways

print("RAILWAY RESERVATION SITE")
print("PRESS '1' FOR RESERVATION AND '2' FOR CANCELLATION")
choice = input("what do you want to use the website for:")


def reservation():
    print("Trains Available")
    print("1.A")
    print("2.B")
    print("3.C")
    train = input("you want a reservation in which train:")
    if train == "1":
        seats = 20
        members = int(input("enter the no. of people travelling:"))
        seats = seats - members
        adults = int(input("No. of adults:"))
        children = int(input("no. of children:"))
        for i in range(0, members):
            name = input("NAME:")
            age = input("AGE:")
        print("YOUR TICKET HAS BEEN BOOKED")
    elif train == "2":
        seats = 20
        members = int(input("enter the no. of people travelling:"))
        seats = seats - members
        adults = int(input("No. of adults:"))
        children = int(input("no. of children:"))
        for i in range(0, members + 1):
            name = input("NAME:")
            age = input("AGE:")
        print("YOUR TICKET HAS BEEN BOOKED")
    elif train == "3":
        seats = 20
        members = int(input("enter the no. of people travelling:"))
        seats = seats - members
        adults = int(input("No. of adults:"))
        children = int(input("no. of children:"))
        for i in range(0, members + 1):
            name = input("NAME:")
            age = input("AGE:")
        print("YOUR TICKET HAS BEEN BOOKED")
    else:
        None


def cancellation():
    members = int(input("enter the no. of members on the ticket:"))
    seats = 20
    seats = seats - members
    PNR = int(input("Enter the PNR no.:"))
    train = int(input("Enter the the train no.:"))
    seats = seats + members
    print("YOUR TICKET HAS BEEN CANCELLED")


if choice == "1":
    reservation()
elif choice == "2":
    cancellation()
else:
    None
