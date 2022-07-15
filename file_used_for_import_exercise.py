





def is_two(x):
    if x=='2'or x==2:
        return True
    else: 
        return False 


is_two(5)







def calculate_tip(tip,bill):
    tip_amt = tip * bill
    return tip_amt


    
    
calculate_tip(.2,100)






def handle_commas(string_input):
    string_input=string_input.replace(',','')

    number_output= int(string_input)
    return number_output

handle_commas('123,456')



def is_vowel(str):
    if str in['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

is_vowel(2)







def get_letter_grade(grade_num):
    if grade_num > 90:
        return 'A'
    elif grade_num > 80 and grade_num <=90:
        return 'B'
    elif grade_num > 70 and grade_num <=80:
        return 'C'
    elif grade_num > 60 and grade_num <=70:
        return 'D'
    else:
        return 'F'