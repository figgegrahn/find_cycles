## Build and run using docker
Script to detect cyclic dependencies in your application

```
$ docker build -t find_cycles .
$ docker run --rm -i find_cycles:latest < ./foo.dot.RbdDisp
```
 
Or plain python with dependencies in your local env

`python3 findCycles.py ./foo.dot.RbdDisp`

Results are printed to stdout as a list of the depending libs like this:
```
['RbdQtGui', 'RbdQtGuiDeployment']
['RbdSim', 'RbdIoSimDeployment']
['ComponentsPortTypes', 'ComponentsInterface']
```