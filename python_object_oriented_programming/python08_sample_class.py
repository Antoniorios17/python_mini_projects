class staff:
    def __init__(self, p_position, p_name, p_pay):
        self._position = p_position
        self.name = p_name
        self.pay = p_pay
        print("Creating Staff object")

    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d" %(self._position, self.name, self.pay)
    
    def calculate_pay(self):
        prompt = '\nEnter number of hours worked for %s: ' %(self.name)
        hours = input(prompt)
        prompt = 'Enter hourly rate for %s: ' %(self.name)
        hourly_rate = input(prompt)
        self.pay = int(hours)*int(hourly_rate)
        return self.pay
    
    @property
    def position(self):
        print('Getter Method')
        return self._position
    
    @position.setter
    def position(self, value):
        if value == 'Manager' or value == 'Basic':
            self._position = value
        else:
            print('Position is invalid. No changes made.')

class management_staff(staff):
    def __init__(self, p_name, p_pay, p_allowance, p_bonus):
        super().__init__('Manager', p_name, p_pay)
        self.allowance = p_allowance
        self.bonus = p_bonus
    
    def calculate_pay(self):
        basic_pay = super().calculate_pay()
        self.pay = basic_pay + self.allowance
        return self.pay
    
    def calculate_perf_bonus(self):
        prompt = 'Enter performance grade for %s: ' %(self.name)
        grade = input(prompt)
        if (grade == 'A'):
            self.bonus = 1000
        else:
            self.bonus = 0
        return self.bonus
class basic_staff(staff):
    def __init__(self, p_name, p_pay):
        super().__init__('Basic', p_name, p_pay)
        

    
