import matplotlib.pyplot as plt
import numpy as np

monthly30 = []

class Mortg:
    
    def __init__(self, i_rate, t_rate, s_price, down):
        self.int_rate = i_rate
        self.tax_rate = t_rate
        self.sale_price = s_price
        self.down_payment = down
        self.borrowed = s_price - down
        self.lst_principal = []
        self.total_interest = 0
        self.total_payable = 0
        self.monthly_price = 0
    def mort_30f(self):
        '''Function to give the bigger picture values: total payment, monthly payment '''

        ratio = (1+self.int_rate)**360        
        self.monthly_price = (self.sale_price - self.down_payment) \
            * self.int_rate * (ratio) /(ratio - 1)
        self.total_payable = 360 * self.monthly_price
        self.total_interest = self.total_payable - self.borrowed
        for i in range(360):
            self.lst_principal.append(self.monthly_price)
        self.display_results(30)
        
    def mort_15f(self):
        '''Function to give the bigger picture values: total payment, monthly payment '''

        ratio = (1+self.int_rate)**180        
        self.monthly_price = (self.sale_price - self.down_payment) \
            * self.int_rate * (ratio) /(ratio - 1)
        self.total_payable = 180 * self.monthly_price
        self.total_interest = self.total_payable - self.borrowed
        for i in range(180):
            self.lst_principal.append(self.monthly_price)
        self.display_results(15)
        
    def display_results(self, tenor):
        print('\n \n \n')
        print(f"{'|'+15*'-'+'|'+21*'-'+'|'+17*'-'+'|'}")
        print(f"| {tenor} yr. Fixed Payments for Mortgage {19*' '}|")
        print(f"{'|'+15*'-'+'|'+21*'-'+'|'+17*'-'+'|'}")
        print('| Total Payable | Total Interest Paid | Monthly Payment |')
        print('| {:,.9}{}| {:,.9}{}| {:,.6}{}|'.format(self.total_payable, 3*' ',self.total_interest,9*' ',self.monthly_price, 8 * ' '))
        print(f"{'|'+15*'-'+'|'+21*'-'+'|'+17*'-'+'|'}")
        months = np.linspace(1, tenor * 12, tenor * 12)
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.bar(months,self.lst_principal)
        plt.show()
    def month_break(self):
        '''Calculation of breakdown of interest and instalments '''
        plt.figure()
            

if __name__=='__main__':
    int_rate = 5.11/12 * 0.01  #%
    tax_rate = 2.14 * 0.01 #%
    sale_price = 4e5
    down_price = 30e3
    home1 = Mortg(int_rate, tax_rate, sale_price, down_price)
    home1.mort_30f()
    home1.mort_15f()
