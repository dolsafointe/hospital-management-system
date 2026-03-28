class Invoice:
    def __init__(self, invoice_id, amount, date):
        self.invoice_id = invoice_id
        self.amount = amount
        self.date = date
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_amount(self):
        return sum(item.amount for item in self.items)

class InvoiceItem:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

class Payment:
    def __init__(self, payment_id, invoice, amount, payment_date):
        self.payment_id = payment_id
        self.invoice = invoice
        self.amount = amount
        self.payment_date = payment_date
        self.status = 'Pending'

    def process_payment(self):
        # Here we would add logic to process the payment
        self.status = 'Completed'

    def refund(self):
        # Here we would add logic to refund the payment
        self.status = 'Refunded'
