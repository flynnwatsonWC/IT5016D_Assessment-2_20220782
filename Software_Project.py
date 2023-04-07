
#Defaults
used_ids = []

ticket_list = []

tickets_solved = 0

tickets_resolved = 0

tickets_reopened = 0

tickets_created = 0


class Ticket():
    
    
    def __init__(self, Num, Creator, ID, Email, Description, Response, Status):
        global tickets_solved
        global tickets_resolved
        global tickets_reopened
        global tickets_created
        
        
        self.Num = Num
        self.Creator = Creator
        self.ID = ID
        self.Email = Email
        self.Description = Description
        self.Response = Response
        self.Status = Status
        
        
        if self.Status == "Open":
            tickets_solved += 1
            
        
        elif self.Status == "Closed":
            tickets_resolved += 1
            
        
        tickets_created += 1
        
        
        used_ids.append(self.Num)
        
    #Ticket Printing
    def ticketprint(self):
        print("--PRINT A TICKET--")
        print("Ticket Number:", self.Num)
        print("Ticket Creator:", self.Creator)
        print("Staff ID:", self.ID)
        print("Staff Email:", self.Email)
        print("Description:", self.Description)
        print("Response:", self.Response)
        print("Status:", self.Status)
        
    #Password Changing
    def change_password(self):
        global tickets_solved
        global tickets_resolved
        changedpwp1 = self.Response[0:3]
        changedpwp2 = self.ID[0:3]
        changedpw = changedpwp2.join(changedpwp1)
        self.Response = "Password Updated to ", changedpw
        self.Status = "Closed"
        tickets_resolved += 1
        tickets_solved -= 1
        
        
#Ticket Stats
def ticketstats():
    global tickets_solved
    global tickets_resolved
    print("--TICKET STATS--")
    print("Tickets Created:", tickets_created)
    print("Tickets Resolved:", tickets_resolved)
    print("Tickets to Solve:", tickets_solved)
        
        
#Example Tickets

#Example 1
ticket1 = Ticket(2001, "Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working", "Not Yet Provided", "Open")
ticket_list.append(ticket1)

#Example 2
ticket2 = Ticket(2002, "Maria", "MARIAH", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars", "Not Yet Provided", "Open")
ticket_list.append(ticket2)

#Example 3
ticket3 = Ticket(2003, "John", "JOHNS", "john@whitecliffe.co.nz", "Password Change", "New password generated: JOJoh", "Closed")
ticket_list.append(ticket3)


#Ticket Creating
def create_ticket():
    global used_ids
    global ticket_list
    userNum = used_ids[-1] + 1
    tid = userNum - 2001
    print("--CREATE A TICKET--")
    userCreator = input("Please input your name: ")
    userID = input("Please input your Staff ID: ")
    userEmail = input("Please input your Email: ")
    userDescription = input("Please add a Description: ")
    ticket4 = Ticket(userNum, userCreator, userID, userEmail, userDescription, "Not Yet Provided", "Open")
    ticket_list.append(ticket4)
    Ticket.ticketprint(ticket_list[tid])
    if "Password Change" in userDescription:
        Ticket.change_password(ticket_list[tid])
        print("Password Changed New Password in Response")
    main()

    
#Ticket Viewing 
def view_tickets():
    global used_ids
    global ticket_list
    print("--VIEW A TICKET--")
    sel_ticket = int(input("Which Ticket would you like to view: "))
    tid = sel_ticket - 2001
    if sel_ticket in used_ids:
        Ticket.ticketprint(ticket_list[tid])
    main()

    
#Ticket Editing
def edit_ticket():
    global used_ids
    global ticket_list
    global tickets_solved
    global tickets_resolved
    global tickets_created
    print("--EDIT A TICKET--")
    sel_ticket = int(input("Which Ticket would you like to edit: "))
    if sel_ticket in used_ids:
        tid = sel_ticket - 2001
        Ticket.ticketprint(ticket_list[tid])
        edit_choice = input("Would you like to \nRe(O)pen, \n(C)lose, \n(R)espond \nor (D)elete a ticket: ")
        if edit_choice == "O":
            ticket_list[tid].Status = "Open"
            tickets_solved += 1
            tickets_resolved -= 1
        elif edit_choice == "C":
            ticket_list[tid].Status = "Closed"
            tickets_resolved += 1
            tickets_solved -= 1
        elif edit_choice == "R":
            userResponse = input("Please Enter a Response: ")
            ticket_list[tid].Response = userResponse
        elif edit_choice == "D":
            confirmation = input("Are you Sure (Y/N): ")
            if confirmation == "Y":
                if ticket_list[tid].Status == "Closed":
                    tickets_resolved -= 1
                elif ticket_list[tid].Status == "Open":
                    tickets_solved -= 1
                ticket_list.pop(tid)
                used_ids.pop(tid)
                print("Ticket Deleted")
                tickets_created -= 1
                main()
            elif confirmation == "N":
                print("No Changes have been made")
        Ticket.ticketprint(ticket_list[tid])
        main()
    else:
        print("No Ticket of that ID Exists")
        edit_ticket()
       
    
#Main
def main():
	ticketstats()
	print("--MAIN MENU--")
	usertask = input("Would you like to \n(C)reate new ticket \n(V)iew a Ticket \nor (E)dit a Ticket: ")
	if usertask == "V":
		view_tickets()
	elif usertask == "C":
		create_ticket()
	elif usertask == "E":
		edit_ticket()
	else:
		main()
            
            
#Initalise
main()