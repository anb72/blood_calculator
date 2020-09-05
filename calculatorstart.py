def interface():
    print("My Program")
    while True:
        print("Options:")
        print("9 - Quit")
        print("1-HDL")
        choice = input("Enter your choice: ")
        if choice=='9':
            return
        elif choice=='1':
            HDL_driver()
interface()

def HDL_driver():
#Get input 
    HDL_result = get_HDL_input()
# Check if HDL is normal 
#Output 
def get_HDL_input():
    HDL_input = input("Enter the HDL test result: ")
    return int(HDL_input)
def check_HDL():
    if HDL result >60
        print ("Normal")
    elif 40<=  && HDL < 60 
        print ("Borderline low")
    else
        print ("Low")
