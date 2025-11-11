def main():
    num_input = input("Please enter a number in either decimal or hexidecimal. ")
    return num_input
#
#
#
the_real_input = main()
print(the_real_input)
#
#
def parse_input(num_input):
    is_hex_YN = False
    if '0x' in num_input:
        is_hex_YN = True
    return is_hex_YN
#
#
the_real_truth = parse_input(the_real_input)
#
#
def decimal_to_binary(dec):
    binary = bin(int(dec)).replace("0b", "")
    return binary
#
def hex_to_binary(hex):
    newhex = hex.replace("0x", "")
    decimal = str(int(newhex, 16))
    binary = decimal_to_binary(int(decimal))
    #
    #TEST CODE: REMOVE BEFORE SUBMISSION
    print(newhex)
    print(decimal)
    print(binary)
    #
    return int(binary)
#
#
def convert_to_binary(unconverted_number):
    if the_real_truth == True:
        converted_number = hex_to_binary(unconverted_number)
    if the_real_truth == False:
        converted_number = decimal_to_binary(unconverted_number)
    return converted_number
#
#
the_real_output = convert_to_binary(the_real_input)
#
#
# Testing code below
def test():
    print(f"Your input: {the_real_input}")
    print(f"Number is Hex: {the_real_truth}")
    print(f"Your converted number is: {the_real_output}")
#
test()