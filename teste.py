import itertools

def evaluate_expression(variables, connective):
    if connective == 1:  # ^
        return all(variables)
    elif connective == 2:  # v
        return any(variables)
    elif connective == 3:  # #
        return not all(variables)
    elif connective == 4:  # →
        return (not variables[0]) or variables[1]
    elif connective == 5:  # ↔
        return all(x == variables[0] for x in variables)

def create_truth_table(num_variables, connective):
    variable_names = [f"p{i}" for i in range(1, num_variables + 1)]
    header = "\t".join(variable_names + ["Result"])
    print(header)
    print("-" * len(header.expandtabs()))

    for values in itertools.product([True, False], repeat=num_variables):
        result = evaluate_expression(values, connective)
        row = "\t".join(str(value) for value in values) + f"\t{result}"
        print(row)

def main():
    num_variables = int(input("Quantas variáveis na expressão? "))
    print("Escolha o conectivo:")
    print("1 = ^")
    print("2 = v")
    print("3 = #")
    print("4 = →")
    print("5 = ↔")
    connective = int(input("> "))

    create_truth_table(num_variables, connective)

if __name__ == "__main__":
    main()
