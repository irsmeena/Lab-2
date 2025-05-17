
def display_main_menu():
    print ("Enter some numbers seperated by commas (ege.g. 5, 67, 32) : ")
    return None 


def get_user_input():
    #i declared a variable called user_input, and assigned it to input the numbers
     user_input = input(display_main_menu())
     # declared another variable called string_list and the values that were in user_input will be split by the commas
     string_list = user_input.split(",")
    # list of floats , .strip removes extra characters, num is the numbers in string_list, i am making my number into float type values
     float_list = [float(num.strip()) for num in string_list]
     
     print("List of floats: " + str(float_list ))

     return float_list 


def calc_average(float_list):
     
    float_list = get_user_input()
    average = sum(float_list) / len(list)
    print (str(average))
    return average

    



def find_min_max (float_list):
    float_list = get_user_input()
    minimum_value = min(float_list)
    maximum_value = max(float_list)
    print (f"minimum value is : {minimum_value}")
    print (f"maximum value is : {maximum_value}")
    float_min_max = [minimum_value , maximum_value]
    return float_min_max



def sort_temperature(float_list):
    float_list.sort() = get_user_input()
    print (str(float_list.sort()))

    return float_list.sort()



    



   
    