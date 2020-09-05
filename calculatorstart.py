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

