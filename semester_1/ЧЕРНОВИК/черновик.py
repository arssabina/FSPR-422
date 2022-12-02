class Store:
    new_user_info={}
    passwords=[]
 
    def __init__(self, name, email, password, code_of_card): 
        self.name=name
        self.email=email
        self.password=password
        self.code_of_card=code_of_card

    def __repr__(self):
        if self.name.isalpha() == True and "@" in self.email and len(self.password) == 6 and len(self.code_of_card) ==1:
            self.new_user_info={'name': self.name, 'e-mail' : self.email, 'password' : self.password,
            'code_of_card': self.code_of_card}
            print(self.new_user_info)
            return f"Registration is successful"
        else: 
            return f"Incorrect information"
   
       
user=Store(input("Enter your name:"), input ("e-mail:"), input("password:"), input("code_of_card:"))
print(user)
