read -p "Advent of Code 2020 Day: " day

read -p "Continue? (y/n): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

function copy_template(){
    if [ ! -f solutions/day_"$day"_a.py ]; then
        cp template.py solutions/day_"$day"_a.py
    fi
    if [ ! -f solutions/day_"$day"_b.py ]; then
        cp template.py solutions/day_"$day"_b.py
    fi
}

function create_data(){

    if [ ! -f data/input/day_"$day"_a.in ]; then
        touch data/input/day_"$day"_a.in
    fi

    if [ ! -f data/input/day_"$day"_b.in ]; then
        touch data/input/day_"$day"_b.in
    fi
    if [ ! -f data/output/day_"$day"_a.out ]; then
        echo "This is a template\!" > data/output/day_"$day"_a.out
    fi

    if [ ! -f data/output/day_"$day"_b.out ]; then
        echo "This is a template\!" > data/output/day_"$day"_b.out
    fi
}

function record_into_problem_names(){
    echo "day_${day}_a" >> problem_names.txt
    echo "day_${day}_b" >> problem_names.txt
}


copy_template
create_data
record_into_problem_names
