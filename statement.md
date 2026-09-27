# Problem Statement

## Background

Small retail stores — such as clothing shops — often handle billing manually, using handwritten receipts or basic calculators. This approach is slow, error-prone, and leaves no organized digital record of past transactions. As a store's customer base grows, manually tallying item totals and grand totals becomes increasingly unreliable and hard to audit.

## Problem

Raj Clothing Store needs a simple, reliable way to:

- Record the items a customer is purchasing (name, quantity, unit price)
- Automatically and accurately calculate line totals and a grand total, removing manual arithmetic errors
- Present the customer with a clear, readable invoice
- Keep a permanent, timestamped digital record of every transaction for future reference, audits, or dispute resolution

There is currently no lightweight tool that fits this need without the overhead of a full point-of-sale system, database setup, or paid software.

## Objective

Build a simple command-line billing application in Python that:

1. Takes item details as console input for a given sale
2. Validates the input (e.g. rejecting negative quantities or prices)
3. Computes per-item and grand totals automatically
4. Displays the invoice in a clean, tabular format
5. Saves each invoice to a uniquely named text file on disk

## Scope

**In scope:**
- Single-session, single-invoice command-line billing
- Basic input validation
- Local file-based invoice storage (plain text)

**Out of scope (for this version):**
- Multi-user or networked access
- A graphical user interface
- Persistent database storage
- Tax, discount, or multi-currency calculations
- Editing or voiding a previously saved invoice

## Expected Outcome

A working Python CLI tool (`AmountCalculator.py`, `Invoice.py`, `ItemInfo.py`) that a store employee can run to generate and save an invoice in under a minute, with no external dependencies beyond the Python standard library.
