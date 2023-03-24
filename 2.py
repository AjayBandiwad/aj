
def main():
    a = 10
    result = concat_funtion(a)
    my_string = "the entered value" + str(a) + "is even" "with remainder : "+str(result)
    display_result(my_string,result)
    
def concat_funtion(x):
  return x % 2
    
def display_result(my_string,result):
        if (result % 2==0):
            print("entered value is even\n",my_string)
        else:
            print("entered value is odd\n",my_string)
            
main()
    
