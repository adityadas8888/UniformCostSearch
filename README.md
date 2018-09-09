# UniformCostSearch_AI-1
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>

<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
</head>
<body>
<div style="text-align: center;">
<img alt="Figure 1: Visual representation of input1.txt" title="Figure 1: Visual representation of input1.txt" src="https://github.com/adityadas8888/UniformCostSearch_AI-1/blob/master/t1_p1.gif"><br>
Figure 1: Text data of <a href="https://github.com/adityadas8888/UniformCostSearch_AI-1/blob/master/input1.txt">Input file</a></div>
<br>
Implement a search algorithm that can find a route between any two
cities. Your program will be called find_route, and will take exactly
commandline arguments as follows:<br>
<br>
<strong><em>find_route uninf/inf input_filename origin_city
destination_city</em></strong>&nbsp;<strong><em>heuristic_filename</em></strong><br>
<br>
An example command line is:<br>
<br>
find_route uninf input1.txt Munich Berlin<br>
<br>
The flag uninf is used to select uninformed search. Argument
input_filename
is the name of a text file such as <a href="https://github.com/adityadas8888/UniformCostSearch_AI-1/blob/master/input1.txt">input1.txt</a>,
that describes road connections between cities in some part of the
world. For example, the road system described by file input1.txt can be
visualized in Figure 1 shown above. You can assume that the input file
is formatted in the same way as <a href="https://github.com/adityadas8888/UniformCostSearch_AI-1/blob/master/input1.txt">input1.txt</a>:
each line contains three
items. The last line contains the items "END OF INPUT", and that is how
the program can detect that it has reached the end of the file. The
other lines of the file contain, in this order, a source city, a
destination city, and the length in kilometers of the road connecting
directly those two cities. Each city name will be a single word (for
example, we will use New_York instead of New York), consisting of upper
and lowercase letters and possibly underscores.<br>
<br>
<br>
The program will compute a route between the origin city and the
destination city, and will print out both the length of the route and
the list of all cities that lie on that route. For example,<br>
<br>
find_route uninf input1.txt Bremen Frankfurt<br>
<br>
should have the following:<br>
<br>
distance: 455 km<br>
route: <br>
Bremen to Dortmund, 234 km <br>
Dortmund to Frankfurt, 221 km <br>
<br>
and<br>
<br>
find_route uninf input1.txt London Frankfurt<br>
<br>
should have the following output:<br>
<br>
distance: infinity<br>
route: <br>
none<br>
<br>
<br>
If instead your program uses the flag inf. It has to do informed search
using the given heuristic. The heuristic file gives the estimate of
what the cost could be to get to the given destination from any start
state (note this is just an estimate). In this case the command line
would look like<br>
<br>
find_route&nbsp;inf input1.txt Munich Kassel h_kassel.txt<br>
<br>
Here the last argument contains a text file what has the heuristic
values for every state wrt the given destination city (note different
destinations will need different heuristic values). For example, you
have been provided a sample file <a href="https://github.com/adityadas8888/UniformCostSearch_AI-1/blob/master/h_kassel.txt">h_kassel.txt</a>
which gives the heuristic value for every state (assuming kassel is the
goal).
Your program should use this information to reduce the number of nodes
it ends up expanding. Other than that, the solution returned by the
program should be the same as the uninformed version.<br>
