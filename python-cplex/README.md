# About this image

Installs dependencies required to run CPLEX 22.1. However, it is not bundles with CPLEX.

## Build image

```
docker build -t python-cplex .
```

## Testing of built image

To run the following with CPLEX binaries in the same directory to verify that it works:

#### Bash

```
docker run --rm \
  -v $(pwd)/python-cplex/cplex:/cplex \
  -v $(pwd)/python-cplex/solve.py:/solve.py \
  python-cplex \
  sh -c "docplex config --upgrade /cplex && python /solve.py"
```

#### Powershell

```
docker run --rm `
  -v ${PWD}/cplex:/cplex `
  -v ${PWD}/solve.py:/solve.py `
  python-cplex `
  sh -c "docplex config --upgrade /cplex && python /solve.py"
```

#### Expected output

```
Performing copies:
    /cplex/cplex/bin/x86-64_linux/libcplex2212.so -> /usr/src/app/.venv/lib/python3.12/site-packages/cplex/_internal/libcplex2212.so
    /cplex/cplex/bin/x86-64_linux/libcplex2212.so -> /usr/src/app/.venv/bin/libcplex2212.so
    /cplex/cpoptimizer/bin/x86-64_linux/cpoptimizer -> /usr/src/app/.venv/bin/cpoptimizer
Version identifier: 22.1.2.0 | 2024-11-26 | 0edbb82fd
CPXPARAM_Read_DataCheck                          1
Found incumbent of value 0.000000 after 0.00 sec. (0.05 ticks)
Tried aggregator 1 time.
MIP Presolve eliminated 1 rows and 2002 columns.
All rows and columns eliminated.
Presolve time = 0.00 sec. (0.46 ticks)

Root node processing (before b&c):
  Real time             =    0.00 sec. (0.58 ticks)
Parallel b&c, 28 threads:
  Real time             =    0.00 sec. (0.00 ticks)
  Sync time (average)   =    0.00 sec.
  Wait time (average)   =    0.00 sec.
                          ------------
Total (root+branch&cut) =    0.00 sec. (0.58 ticks)
Solution status: integer optimal solution
Objective value: 2020.0
x = 0
y = 10.0
sum(zs) = 2000.0
```
