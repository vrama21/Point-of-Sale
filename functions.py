class ButtonInput():
    def menu_item(self, qty, item, price):
        self.qty = qty
        self.item = item
        self.price = price
        print(qty, item, price)

    def test(self):


print(ButtonInput.menu_item("1", "Large Pizza", "12.00", "12.00"))

