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