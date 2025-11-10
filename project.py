print("Hi!")
#
#
# real code below
def main():
    num_input = input("Please enter a number in either decimal or hexidecimal. ")
    return num_input
#
#
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
the_real_truth = parse_input(the_real_input)
print(the_real_truth)
#
#
def convert_to_binary(unconverted_number):
    # this code converts hex or decimal to binary
    # pseudo code below
    #
    # if real truth = true
    #   this is a hex number
    #   convert this to binary
    #   converted number =
    # if real truth = false
    #   this is a decimal number
    #   convert this to binary
    #   converted number =
    # return converted_number
    pass
#
#
