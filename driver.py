"""
The driver to evaluate all test cases
of a problem in one go!

The only useful method is `main`.

Run `python driver.py ProblemA`
to evaluate all test cases of ProblemA.
"""

from pathlib import Path
import os
import sys
import pytest


TOP = Path(os.getcwd())
DATA = TOP / "data"
DATA_INPUT = DATA / "input"
DATA_OUTPUT = DATA / "output"
PROBLEM = TOP / "solutions"


def given_problem(problem_name: str, input_test_case: str):
    """
    Run the problem in a shell and
    collect the outputs (not prints)
    and return it.

    :param problem_name: The name of the problem to be tested.
    :param input_test_case: The name of the input test case.
    :return: The calculated output.
    """
    command = """
                python solutions/{prob}.py < data/input/{case}
            """.format(
        prob=problem_name, case=input_test_case
    )
    try:
        output = os.popen(command)
    except BrokenPipeError as _e:
        print(_e)
        output = None
    return output


def all_cases_per_problem(problem_name):
    """
    Given a problem name, test it
    against the test_cases defined
    in the data/input and data/output
    directories.

    :param problem_name: The name of the problem.
    :return: None
    """

    sample_cases_input = DATA_INPUT.glob(f"{problem_name}*")
    sample_cases_output = DATA_OUTPUT.glob(f"{problem_name}*")
    print(f"Testing Problem: {problem_name}")

    for case in zip(sorted(sample_cases_input), sorted(sample_cases_output)):
        case_inp, case_out = case
        solution_output = given_problem(problem_name, str(os.path.basename(case_inp)))
        calculated_output = [i.rstrip() for i in solution_output]
        with open(case_out, "r") as f_output:
            expected_output = [i.rstrip() for i in f_output]
        passed = calculated_output == expected_output

        if passed:
            print(
                f"Test Case: {str(os.path.basename(case_inp))}", "passed successfully!"
            )
        else:
            print(f"Test Case: {str(os.path.basename(case_inp))}", "FAILED!")
            print(
                "Output:", str(calculated_output), "\t\t", "Expected:", expected_output
            )
            return False
    return True


def get_problems(fname="problem_names.txt"):
    """
    Get the list of problems in `fname`.
    :param fname: The name of the file that has problems.

    """
    if os.path.exists(fname):
        with open(fname, "r") as problem_file:
            raw = problem_file.readlines()
            return list(map(lambda _x: _x.strip(), raw))
    return []


@pytest.mark.parametrize("problem", get_problems())
def test_all_cases(problem):
    """
    Test all the cases of a parametrized problem.
    """
    assert all_cases_per_problem(problem)


def main():
    """
    Test the problems passed in CLI arguments
    against all of its test cases.
    """
    problems = sys.argv[1:]
    for _p in problems:
        all_cases_per_problem(_p)


if __name__ == "__main__":
    main()
