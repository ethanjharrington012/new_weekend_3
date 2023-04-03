class Parking_Garage():
    
    def __init__(self,parkingSpaces, name):
        self.tickets_available = parkingSpaces
        self.parkingSpaces = parkingSpaces
        self.name = name
        self.id_name = {}


    def takeTicket(self):
        
        licence_id = input("\nWhats your licence plate number?: ")
        self.id_name[licence_id] = 1           
        self.tickets_available -= 1
        for key, value in self.id_name.items():
            print(f"\nYou Licence plate number is {key.upper()} and you perchased {value} tickets")
        
    def returnTicket(self):
        tickets_returning = input("\nWhats your license plate number: ")
        for key in self.id_name.keys():
            if key != tickets_returning:
                print(f"Try again there is no plate by the title of {tickets_returning.upper()}")
            else:
                self.tickets_available += 1
                del [tickets_returning]
                self.checkoutTicket()


    def showTicketavailable(self): 
            print(f'\n{self.tickets_available} tickets available.') 
      
    def checkoutTicket(self):
        while True:
            payment = input("Please pay your fee of $15.00 (Type: 15.00): ")
            if payment != "15.00":
                print("Incorrect amount.")
                self.checkoutTicket()
            else:
                print(f" \nThanks for parking at {self.name}.\nHave a great day!")
            break
                
    def run(self):
           
    
        while True:
            quest_name = input("Whats your name: ")
            
            response = input(f"\nWelcome to the garage! it is $15.00 a day to park! \nWhat are you doing {quest_name.title()}? Entering/Exiting/Show (tickets)/quit: ").lower()

            if response == 'entering':
                self.takeTicket()

            elif response == 'exiting':
                self.returnTicket()
                
                
            elif response == 'show':
                self.showTicketavailable()
            elif response == 'quit':
                print("\nHave a great day! ")
                break
            else:
                print("Invalid entry. Please try again, doofus.")



ethans_Garage = Parking_Garage(100, "Ethans ass garage")
            
ethans_Garage.run()