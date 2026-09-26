from ItemInfo import ItemInfo

class Invoice:
    __items: list[ItemInfo] = []
    __totalAmount = 0

    # This method adds an item to invoice
    def addItem(self, name, quantity, unitPrice):
        item = ItemInfo(name, quantity, unitPrice)
        self.__items.append(item)
        self.__totalAmount += item.lineTotal

    # This method gives grand total
    def getTotalAmount(self):
        return self.__totalAmount

    # This method returns invoice in table format as string
    def __str__(self):
        lines = []
        lines.append('|-------------------------------------------|')
        lines.append('|            Raj Clothing Store             |')
        lines.append('|-------------------------------------------|')
        lines.append("| Name           | Quantity | Price | Total |")
        lines.append('|-------------------------------------------|')
        for item in self.__items:
            lines.append(f'| {item.name.ljust(14)} | {str(item.quantity).ljust(8)} | {str(item.unitPrice).ljust(5)} | {item.lineTotal}   |')
        lines.append('|-------------------------------------------|')
        lines.append(f'| Grand Total                       | {self.getTotalAmount()}   |')
        lines.append('|-------------------------------------------|')
        return "\n".join(lines)

    # This method prints invoice
    def display(self):
        print(self)