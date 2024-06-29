# HOMEWORK
# # Todo => id , title , description , priority, created_at => class
# 2) Todo =>  named_tuple


# NAMED TUPLE
# id=uuid4()
# time_of_creation=datetime.now()


# tasks=namedtuple("Todo", ["id","title", "priority_level","description","created_at"])

# homework=tasks(id, 'Programming homework', 'First', 'Urgent', time_of_creation)
# print(homework.priority_level)

# CLASS
# class Todo:
#     def __init__(self, id, title,priority_level, description, created_at):
#         self.id=id
#         self.title=title
#         self.priority_level=priority_level
#         self.description=description
#         self.created_at=created_at

# homework2=Todo(uuid4(),'math_homework','Second', 'urgent',datetime.now())  
# print(homework2.created_at)
# print(homework2.priority_level)

# # 2nd HOMEWORK
# def transaction(balance):
#     initial_balance=balance
    
#     def send_money(amount):
#         nonlocal balance
#         if amount>0:
#             commission=amount*0.01
#             sent_money=amount+commission
#             if sent_money<balance:
#                 balance=initial_balance-sent_money
#                 return f"Commission is {commission} so'm and Minus {sent_money} from your purse"
#             else:
#                 return f'Insufficient Funds. Operation not carried'
    
#     def receive_money(amount):
#         nonlocal balance
#         balance=balance+amount
#         return f"There was {amount} so'm plus to your balance"
    
#     def get_balance():
#         nonlocal balance
#         return f"Your current balance is {balance} so'm "
    
#     return send_money,receive_money, get_balance

# send_money,receive_money, get_balance=transaction(400000)
# print(send_money(500000))
# print(receive_money(1000000))
# print(get_balance())