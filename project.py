def main():
    num_input = input("Please enter a number in either decimal or hexidecimal. ")
    return num_input
#
#
def run():
    global the_real_input
    the_real_input = main()
    global the_real_truth
    the_real_truth = parse_input(the_real_input)
    the_real_output = convert_to_binary(the_real_input)
    return the_real_input, the_real_output, the_real_truth
#
#
def parse_input(num_input):
    is_hex_YN = False
    if '0x' in num_input.lower():
        is_hex_YN = True
    return is_hex_YN
#
#
def decimal_to_binary(dec):
    binary = bin(int(dec)).replace("0b", "")
    return binary
#
#
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
# Testing code below
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
#
run()
test()