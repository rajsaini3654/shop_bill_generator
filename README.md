# Invoice Billing System

A simple command-line billing application for **Raj Clothing Store**. It collects product details from the user, calculates line totals and a grand total, prints a formatted invoice to the terminal, and saves each invoice as a timestamped text file.

## Features

- Interactive CLI prompts for the number of distinct products and their details (name, quantity, unit price)
- Input validation for the number of items (must be a positive integer)
- Automatic calculation of line totals and grand total
- Formatted, table-style invoice printed to the console
- Invoices auto-saved to an `invoices/` folder with a unique timestamped filename
- Validation to reject negative quantities or unit prices

## Project Structure

```
.
├── AmountCalculator.py   # Entry point — handles user input and orchestrates billing
├── Invoice.py            # Invoice class — stores items, computes totals, formats output
├── ItemInfo.py           # ItemInfo class — represents a single line item
└── invoices/             # Auto-created folder where saved invoices are stored
```

## Class Overview

### `ItemInfo` (`ItemInfo.py`)
Represents one row/item on the invoice.

| Attribute | Description |
|---|---|
| `name` | Item name |
| `quantity` | Quantity purchased (`int`) |
| `unitPrice` | Price per unit (`float`) |
| `lineTotal` | `quantity * unitPrice` |

Raises `ValueError` if `quantity` or `unitPrice` is negative.

### `Invoice` (`Invoice.py`)
Represents the full invoice — a collection of `ItemInfo` objects.

| Method | Description |
|---|---|
| `addItem(name, quantity, unitPrice)` | Creates an `ItemInfo` and adds it to the invoice |
| `getTotalAmount()` | Returns the running grand total |
| `__str__()` | Returns the invoice formatted as a text table |
| `display()` | Prints the invoice to the console |

### `AmountCalculator.py`
The script you run. It:
1. Asks how many distinct products to enter
2. Collects `name quantity unitPrice` for each product (space-separated, one line per item)
3. Builds an `Invoice`, displays it, and saves it to `invoices/invoice_<timestamp>.txt`

## Requirements

- Python 3.9+ (uses the `list[ItemInfo]` type-hint syntax)
- No external dependencies — standard library only (`os`, `datetime`)

## How to Run

```bash
python AmountCalculator.py
```

Example session:

```
Enter number of distinct products: 2

Enter item details in below format
Name     Quantity    Unit Price
Shirt 2 499.99
Jeans 1 1299.50

|-------------------------------------------|
|            Raj Clothing Store             |
|-------------------------------------------|
| Name           | Quantity | Price | Total |
|-------------------------------------------|
| Shirt          | 2        | 499.99| 999.98   |
| Jeans          | 1        | 1299.5| 1299.5   |
|-------------------------------------------|
| Grand Total                       | 2299.48   |
|-------------------------------------------|

Invoice has been saved in invoices/invoice_20260926_143012.txt
```

> Each item line must be entered as three space-separated values: `Name Quantity UnitPrice` (e.g. `Shirt 2 499.99`). Item names cannot contain spaces in the current input format.

## Known Limitations

- **Shared state across instances:** `Invoice.__items` and `Invoice.__totalAmount` are declared as *class* attributes rather than being initialized in `__init__`. In Python, mutable class attributes are shared by all instances, so creating more than one `Invoice` in the same run (or the same process) can cause item lists and totals to leak between invoices. This isn't triggered by the current single-invoice CLI flow, but it's a latent bug worth fixing (initialize `self.__items = []` and `self.__totalAmount = 0` inside `__init__`).
- **No input validation on raw input:** `AmountCalculator.py` assumes each line splits into exactly three tokens and that quantity/price are numeric; malformed input will raise an unhandled exception.
- **No product-name spaces:** because splitting is done on whitespace, item names with spaces aren't supported.
- **File handling:** the output file is opened/closed manually rather than via a `with` block, so a failure between `open()` and `close()` could leave the file handle open.

## Possible Improvements

- Fix the class-level mutable attribute bug in `Invoice`
- Use `with open(...)` for safer file handling
- Add try/except around user input parsing with helpful error messages
- Support item names with spaces (e.g. via comma-separated input)
- Add unit tests for `ItemInfo` and `Invoice`
