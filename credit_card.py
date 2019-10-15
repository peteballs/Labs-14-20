
def double(yes):
    return [2*n if i%2 else n for i, n in enumerate(yes)]
def new_list(no):
        new_list = []
        return [x-9 if x>9 else x for x in no]        
card_number = int(input("Please enter the credit card number.........."))
card_number = str(card_number)
list(card_number)
card_number_list = list(card_number)
print(card_number_list)
revised_card_list = card_number_list [:-1]
print(revised_card_list)
backward = revised_card_list [::-1]
print (backward)
num_backward= list(map(int, backward)) 
print (num_backward)
test_list = list(map(int, num_backward)) 
double_list = double(num_backward)
print(double_list)
subtract_nine = new_list(double_list)
print(subtract_nine)
final_check = (sum(subtract_nine))
print (final_check)
last_check = int(card_number [-1])
print(last_check)
verify = (final_check % 10)
print(verify)
if verify == last_check:
    print("Valid")
else:
    print("Invalid")

