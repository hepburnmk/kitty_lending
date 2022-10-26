"""
Store the available cash in a variable called kitty
Create an empty list called requests
Read the data from the text file line-by-line, storing each line as a different element in the requests list
Loop through all of the requests in the list. For each request, check the following:
If the payment can be made in full
Print to the console stating that the request was paid
Write an additional line to the end of the loan_requests.txt file
If the payment can be partially paid
Print to the console stating that a partial payment was made
Write an additional line to the end of the loan_requests.txt file
If the payment cannot be paid (kitty is empty)
Print to the console stating that the request went unpaid
Write an additional line to the end of the loan_requests.txt file
"""

kitty = 500
requests = []


with open('loan_requests.txt', 'r') as requests:
    content = requests.readlines()
    # Read the list from a text file, using context manager to automatically close after block runs.

    requests = [r.strip() for r in content]
    print(requests)
    # Put into list removing whitespace on the right. Test this worked.

    requests = [eval(i) for i in requests]
    # Iterate through the list of strings and eval to a list of integers

    print(type(requests[0]))
    # Test this worked

    print(requests)
    # Imported list

print("\nMegan Kelly's Interim Assessment 2 for IT Specialist in Python\n")

with open('loan_requests.txt', 'a') as write_file:
    for amount in requests:
        if amount <= kitty:
            print("€" + str(amount), "- Paid!")
            write_file.write("\nRequest of €" + str(amount) + " paid in full.")
            kitty = kitty - amount
            # Deduct the amount from the kitty to reduce the value.

        elif kitty > 0:

            print("€" + str(amount), "request cannot be processed in full"
                                     " (Insufficient funds available). Amount paid: €" + str(kitty))
            write_file.write(
                "\nRequest of €" + str(amount) + " could not be paid in full. "
                                                 "Partial payment of €" + str(kitty) + " made.")
            kitty = kitty - kitty
            # Deduct the remaining amount from the kitty, resulting in 0

        else:
            print("Request of €" + str(amount), "is UNPAID!")
            write_file.write("\nOutstanding request: €" + str(amount) + ".")

print("Amount left in kitty is:", kitty)
