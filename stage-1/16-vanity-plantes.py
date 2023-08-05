def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 6 >= len(s) >= 2:
        return False
    
  
    if s[0].isdigit() or s[1].isdigit():
        return False
    
    number_encountered = False
    for char in s:
        
        if char == "0" and number_encountered == False:
            return False
        
        if char.isdigit():
            number_encountered = True
        
        elif number_encountered:
            return False
    
 
    return True

main()
