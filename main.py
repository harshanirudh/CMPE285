
class StocksCalc:
    def __init__(self, symbol, allotment_size, final_price, sell_commission, init_price, buy_commission, tax ):
        self.symbol = symbol
        self.allotment_size = allotment_size
        self.final_price = final_price
        self.sell_commission = sell_commission
        self.init_price = init_price
        self.buy_commission = buy_commission
        self.tax = tax
        
    def getReport(self):
        self.proceeds = self.allotment_size * self.final_price
        print("Proceeds: $",self.proceeds)
        
        a = self.allotment_size * self.init_price + self.buy_commission + self.sell_commission
        b = (self.proceeds - a)* (0.15)
        self.cost = a + b
        print("Cost: $", self.cost)
        
        self.net_profit = self.proceeds - self.cost
        print("Net Profit: $", self.net_profit)
        
        self.ROI = float(self.net_profit / self.cost) *100
        print("Return on Investment is:", self.ROI)
        
        self.break_even = float((self.allotment_size*self.init_price + self.buy_commission + self.sell_commission) / self.allotment_size)
        print("Break Even Price: $" ,self.break_even)

calc = StocksCalc("ADBE", 100, 110, 15, 25, 10, 15)
print("PROFIT REPORT:")
calc.getReport()


