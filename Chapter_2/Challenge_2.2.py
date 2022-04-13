length_lawn = int(input("Enter the length of the lawn: "))
width_lawn = int(input("Enter the width of the lawn: "))

def calculate_required_seeds(length_lawn, width_lawn):
    return (length_lawn * width_lawn) * 50

print("The amount of seeds required is: ", calculate_required_seeds(length_lawn, width_lawn), "grams")
