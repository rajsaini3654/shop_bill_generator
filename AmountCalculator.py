from os import makedirs, path
from datetime import datetime
from Invoice import Invoice

def billing():
    # Number of distinct itmes (i.e. number of rows in invoice)
    distinctProductCount = int(input("Enter number of distinct products: "))

    while distinctProductCount <= 0:
        distinctProductCount = int(input("Please enter valid number of items: "))

    invoice = Invoice()
    print("\nEnter item details in below format")

    # Format for input
    print("Name     Quantity    Unit Price")

    for i in range(distinctProductCount):
        # Taking input from user
        itemDetails = input() 
        itemName, itemQuantity, itemUnitPrice = itemDetails.split()
        invoice.addItem(itemName, itemQuantity, itemUnitPrice)

    # Displaying it on the terminal
    invoice.display()

    # Saving invoice for future reference
    directory = "invoices"
    makedirs(directory, exist_ok=True)
    timeStamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file = path.join(directory, 'invoice_' + timeStamp + '.txt')
    f = open(file, "w", encoding="utf-8")
    f.write(invoice.__str__())
    f.close()
    print(f'Invoice has been saved in {file}')

if __name__ == "__main__":
    billing()