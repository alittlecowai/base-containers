from docplex.mp.model import Model  # type: ignore


def solve_lp():
    # Create optimization model
    mdl = Model(name="simple_lp")

    # Decision variables
    x = mdl.continuous_var(name="x", lb=0)
    y = mdl.continuous_var(name="y", lb=0)
    zs = mdl.binary_var_list(2000)

    # Objective: maximize x + 2y
    mdl.maximize(x + 2 * y + sum(zs))

    # Constraint: x + y <= 10
    mdl.add_constraint(x + y <= 10, "c1")

    # Solve
    solution = mdl.solve(log_output=True)

    if solution:
        print("Solution status:", mdl.solve_details.status)
        print("Objective value:", solution.objective_value)
        print("x =", x.solution_value)
        print("y =", y.solution_value)
        print("sum(zs) =", sum(solution.get_values(zs)))
    else:
        print("No solution found")


if __name__ == "__main__":
    solve_lp()
