import socket

Domain_Name = input("Enter Your Target Doman Name Here :\t")

Ip_of_Domain = socket.gethostbyname(Domain_Name)

print("Your Target Domain IP Address is :\n" , Ip_of_Domain)
