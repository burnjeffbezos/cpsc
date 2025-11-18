# main() will collect the user input.
def main():
    num_input = input("Please enter a number in either decimal or hexidecimal. ")
    return num_input
#
#
# run() will establish variables and when/how we use them.
def run():
    global the_real_input
    the_real_input = main()
    global the_real_truth
    the_real_truth = parse_input(the_real_input)
    global the_real_output
    the_real_output = convert_to_binary(the_real_input)
    return the_real_input, the_real_output, the_real_truth
#
#
# parse_input() will tell us if the number is hex or decimal.
def parse_input(num_input):
    is_hex_YN = False
    if '0x' in num_input.lower():
        is_hex_YN = True
    return is_hex_YN
#
#
# decimal_to_binary() will conver any decimal input into a binary output minus the 0b that usually precedes in Python.
# if a string without "0x" or "0X" is inputted but does not only contain numerical values, this will cause an error in Python.
def decimal_to_binary(dec):
    binary = bin(int(dec)).replace("0b", "")
    return binary
#
#
# hex_to_binary() will first convert our hex number to binary, then convert our binary number into decimal using the previous function.
# if a string including "0x" or "0X" is used but contains a letter beyond f, this will cause an error in Python.
def hex_to_binary(hex):
    newhex = hex.replace("0x", "").replace("0X", "")
    decimal = str(int(newhex, 16))
    binary = decimal_to_binary(int(decimal))
    #
    print(f"Your Hex number: {newhex}")
    print(f"Its Decimal equivalent: {decimal}")
    #
    return binary
#
#
# convert_to_binary() will perform the necessary actions to our input.
def convert_to_binary(unconverted_number):
    global the_real_truth
    if the_real_truth == True:
        converted_number = hex_to_binary(unconverted_number)
    if the_real_truth == False:
        converted_number = decimal_to_binary(unconverted_number)
    return converted_number
#
#
#
# test() prints the results of our operations
def test():
    print(f"Your input: {the_real_input}")
    print(f"Number is Hex: {the_real_truth}")
    print(f"Your number in Binary is: {the_real_output}")
    go_again = input("Would you like to go again? Type Y for yes or type N for no")
    if go_again.lower() == "y":
        run()
        test()
#
#
# 
#
#
#
#
# now we run the code! :)
run()
test()