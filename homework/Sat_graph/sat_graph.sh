#/bin/sh

## $1 solver Minisat
## $2 json graph file
## $3 nb colors

## chmod u+x
## exemple: ./s.sh MiniSat_v1.14_linux tmp.json 3

python __main__.py $2 $3 sat.in && ./$1 sat.in sat.out
test $? -eq 10 && echo "======== Model ========" && python model_printer.py sat.out sat.in
