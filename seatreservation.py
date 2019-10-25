# seat reservation code

chairs = ['-','-','-','-','-','-','-','-','-']

print ("SEAT RESERVATION. '-' means available, 'x' means taken.")

def printchairs():

    counter = 0
    for x in chairs:

        print (chairs[counter], end='')
        
        if x[0] == chairs[counter]:
            counter += 1
        
        if (counter == 3 or counter == 6):
            print()

        if (counter == 9):
            print()


def occupiedchairs():
    seats = 0;

    for y in chairs:
        if (y == "X"):
            seats += 1
        else:
            continue

    if (seats == 9):
        return True
            


reserveChair = ""
chairsoccupied = False

while (True):
    print("CHAIRS: [0 1 2 = top row] [3 4 5 = middle row] [6 7 8 = bottom row]")
    chair = int(input("From 0 to 8, enter chair number: "))
    chairs[chair] = 'X'

    printchairs()

    chairsoccupied = occupiedchairs()    

    if (chairsoccupied == True):
        print ("All chairs occupied!")
        break

    reserveChair = input("Do you want to reserve more? Y or N: ")

    # if input is any character, then it means n or no
    if (reserveChair == "yes" or reserveChair == "y"):
        continue
    else:
        break
    
 



 
