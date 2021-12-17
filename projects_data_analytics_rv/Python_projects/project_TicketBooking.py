class train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def getstatus(self):
        print(f"train: {self.name}\navilable seats: {self.seats}\nticket fare: Rs {self.fare}")

    def bookTicket(self,n):
        if n == 0:
            print("pls enter a valid passanger count")
        
        elif self.seats>0:
            print("your birth is confirmed!")
            for i in range(-self.seats,0):
                print("seat no:", -i)
                if i == n-self.seats-1:
                    break
            self.seats = self.seats - n
        else:
            print("sorry! ticket is not avilable for this train")

    def cancelTicket(self, noftc):
        self.noftc = noftc
        if noftc > 0:
            self.seats = self.seats + noftc

rajdhani = train("rajdhani_exp", 240, 640)
satabdi = train("satabdi_exp", 78, 650)

while(True):
    print("for cheack avilablity press [1]\nfor PNR status press [2]\nfor exit press [3]")
    ui = int(input("your option: "))
    if ui == 1:
        st = input("enter train name: ")
        if st == "cancel":
            exit()

        elif st == "rajdhani":
            rajdhani.getstatus()
            print("1. For Book Ticket\n2. For Cancel Ticket\n3. For Exit")
            opt = int(input("Your Option: "))
            if opt == 1:
                rajdhani.bookTicket(n = int(input("Total Passanger: ")))
            elif opt == 2:
                rajdhani.cancelTicket(noftc = int(input("NoOfTicketCancel: ")))
            elif opt == 3:
                exit()

        elif st == "satabdi":
            satabdi.getstatus()
            print("1. For Book Ticket\n2. For Cancel Ticket\n3. For Exit")
            opt = int(input("Your Option: "))
            if opt == 1:
                satabdi.bookTicket(n = int(input("Total Passanger: ")))
            elif opt == 2:
                satabdi.cancelTicket(noftc = int(input("NoOfTicketCancel: ")))
            elif opt == 3:
                exit()
    elif ui == 2:
        print("for more option press 1")
        r = True
        while r:
            pnr = int(input("PNR: "))
            if pnr == 1:
                r = False
            else:
                print("please wait... your pnr is processing")
    else:
        exit()