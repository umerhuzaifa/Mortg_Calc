import matplotlib.pyplot as plt
import numpy as np

monthly30 = []

class Mortg:
    
    def __init__(self, i_rate, t_rate, s_price, down, PMI):
        self.int_rate = i_rate
        self.tax_rate = t_rate
        self.sale_price = s_price
        self.down_payment = down
        self.borrowed = s_price - down
        self.lst_principal = []
        self.total_interest = 0
        self.total_payable = 0
        self.monthly_price = 0
        self.PMI_rate = PMI
        self.ratio30mort = 0
        self.ratio15mort = 0
    def mort_30f(self):
        '''Function to give the bigger picture values: total payment, monthly payment '''
        ## the term (1+r)^n 
        self.ratio30mort = (1+self.int_rate)**360        
        
        self.monthly_price = self.borrowed * self.int_rate * self.ratio30mort/(self.ratio30mort - 1) \
            + self.tax_rate * self.sale_price + self.borrowed * self.PMI_rate
        
        ## (S - D) * (r) * (1+r)^n/((1+r)^n - 1) + S * tax/12
        self.total_payable = 360 * self.monthly_price
        self.total_tax     = 360 * self.tax_rate * self.sale_price
        self.total_interest = self.total_payable - self.borrowed - self.total_tax - self.borrowed * self.PMI_rate
        for i in range(360):
            self.lst_principal.append(self.monthly_price)
        self.display_results(30)
        
    def mort_15f(self):
        '''Function to give the bigger picture values: total payment, monthly payment '''

        self.ratio15mort = (1+self.int_rate)**180        
        self.monthly_price = self.borrowed * self.int_rate * self.ratio15mort/(self.ratio15mort - 1) \
            + self.tax_rate * self.sale_price + self.borrowed * self.PMI_rate
        ## (S - D) * (r) * (1+r)^n/((1+r)^n - 1) + S * tax/12
        self.total_payable = 180 * self.monthly_price
        self.total_tax     = 180 * self.tax_rate * self.sale_price
        self.total_interest = self.total_payable - self.borrowed - self.total_tax - self.borrowed * self.PMI_rate
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
##        fig = plt.figure()
##        ax = fig.add_axes([0,0,1,1])
##        ax.bar(months,self.lst_principal)
##        plt.show()
    def month_break(self):
        '''Calculation of breakdown of interest and instalments '''
##        plt.figure()
            

if __name__=='__main__':
    mortg_rate = 5.11/12 * 0.01  
    UIF_rate   = 5.5 /12 * 0.01
    tax_rate   = 1.9 * 0.01/12
    PMI        = 1 * 0.01/12
    
    sale_price = 3.5e5
    down_price = 30e3
    print('Traditional Mortgage Rate')
    
    home1 = Mortg(mortg_rate, tax_rate, sale_price, down_price, PMI)
    home1.mort_30f()
##    home1.mort_15f()
    
    print('UIF Provided Rate')
    home2 = Mortg(UIF_rate, tax_rate, sale_price, down_price, PMI)
    home2.mort_30f()
