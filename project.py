print("Hi!")
#
#
# real code below
def main():
    num_input = input("Please enter a number in either decimal or hexidecimal. ")
    return num_input
#
#
# TEST: REMOVE BEFORE UPLOADING
the_real_input = main()
print(the_real_input)
#
#
def parse_input(num_input):
    is_hex_YN = False
    if 'x' in num_input:
        is_hex_YN = True
    return is_hex_YN
#
#
# TEST: REMOVE BEFORE UPLOADING
the_real_truth = parse_input(the_real_input)
print(the_real_truth)
#
#
def decimal_to_binary(dec):
    binary = bin(int(dec)).replace("0b", "")
    return binary
#
def hex_to_binary():
    pass
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
