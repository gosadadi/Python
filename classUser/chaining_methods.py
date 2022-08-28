class User:
    def __init__(self,first_name, last_name, email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member =False
        self.gold_cards_points =0
    def display_info(self):
        print(self.first_name + self.last_name + self.email + str(self.age))
        return self
    def enroll(self):
        if (self.is_rewards_member== True):
            print("user are already a member.")
            return False
        else:
            print("enroll the member.")
            return True
    def spend_points(self,amount):
        self.amount=200-amount
        if(self.amount>0):
            print(f"you still have {self.amount} points")
        else:
            print("you have used all your points")
p1=User("Gosa","Dadi","gos.d.dadi@gmail.com",32)
# print(p1.first_name+" "+p1.last_name +" "+p1.email+ " "+ str(p1.age))
p1.display_info().spend_points(50)
p1.enroll()
p2=User("John"," Doe"," doe@gmail.com ",40)
p2.display_info().spend_points(100)
p2.enroll()
