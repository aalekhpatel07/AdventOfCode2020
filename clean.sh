
function cleaner(){
    for fname in driver.py template.py ./solutions
        do
            echo "Linting $fname with autopep8."

            # Run autopep8 to lint it.
            if [[ -d $fname ]]; then
                autopep8 $fname --in-place --recursive --aggressive --aggressive --aggressive
            else
                autopep8 $fname --in-place --aggressive --aggressive --aggressive
            fi

            echo "Finished linting $fname with autopep8."
            echo ""
            echo "Linting $fname with black."

            # Run black to lint it yet again.
            black $fname

            echo "Finished linting $fname with black."
            echo ""
            echo "Evaluating code quality of $fname with pylint."
            echo ""

            # Run pylint to evluate final code rating.
            pylint $fname
        done
    return 0
}

cleaner
