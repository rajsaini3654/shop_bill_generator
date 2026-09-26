# This class represnts a row in invoice
class ItemInfo:
    def __init__(self, name, quantity, unitPrice):
        self.name = name
        self.quantity = int(quantity)
        self.unitPrice = float(unitPrice)
        self.lineTotal = self.quantity * self.unitPrice

        # Validation that quantity and unitPrice are non-negative values
        if self.quantity < 0:
            raise ValueError("Quantity can not be negative")
        if self.unitPrice < 0:
            raise ValueError("Unit Price can not be negative")