# UniformCostSearch_AI-1
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head>
<!-- saved from url=(0066)file:///C:/Users/Vamsi/Desktop/ai1/2k15/Web_Old/assmts/pa/pa1.html -->
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252"><title>Assignment 1</title>

</head>
<body>
<h1>Assignment 1</h1>
<h2>Programming Assignment - Search</h2>
<div style="text-align: center;">
<img alt="Figure 1: Visual representation of input1.txt" title="Figure 1: Visual representation of input1.txt" src="Assignment%201_files/t1_p1.gif"><br>
Figure 1: Visual representation of <a href="https://omega.uta.edu/~gopikrishnav/classes/2018/fall/4308_5360/assmts/assmt1_files/input1.txt">input1.txt</a></div>
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
is the name of a text file such as <a href="https://omega.uta.edu/~gopikrishnav/classes/2018/fall/4308_5360/assmts/assmt1_files/input1.txt">input1.txt</a>,
that describes road connections between cities in some part of the
world. For example, the road system described by file input1.txt can be
visualized in Figure 1 shown above. You can assume that the input file
is formatted in the same way as <a href="https://omega.uta.edu/~gopikrishnav/classes/2018/fall/4308_5360/assmts/assmt1_files/input1.txt">input1.txt</a>:
each line contains three
items. The last line contains the items "END OF INPUT", and that is how
the program can detect that it has reached the end of the file. The
other lines of the file contain, in this order, a source city, a
destination city, and the length in kilometers of the road connecting
directly those two cities. Each city name will be a single word (for
example, we will use New_York instead of New York), consisting of upper
and lowercase letters and possibly underscores.<br>
<br>
<span style="font-weight: bold;">IMPORTANT NOTE</span>:
MULTIPLE INPUT FILES WILL BE USED TO GRADE THE
ASSIGNMENT, FILE <a href="https://omega.uta.edu/~gopikrishnav/classes/2018/fall/4308_5360/assmts/assmt1_files/input1.txt">input1.txt</a>
IS JUST AN EXAMPLE. YOUR CODE SHOULD WORK
WITH ANY INPUT FILE FORMATTED AS SPECIFIED ABOVE.<br>
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
For full credit, you should produce outputs identical in format to the
above two examples.<br>
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
have been provided a sample file <a href="https://omega.uta.edu/~gopikrishnav/classes/2018/fall/4308_5360/assmts/assmt1_files/h_kassel.txt">h_kassel.txt</a>
which gives the heuristic value for every state (assuming kassel is the
goal).
Your program should use this information to reduce the number of nodes
it ends up expanding. Other than that, the solution returned by the
program should be the same as the uninformed version.<br>
<h2>Suggestions</h2>
The code needs to run on omega. If you have not even tried
logging in on omega until the last day, there is a high probability
that something
will go wrong. You may find it convenient to do the code development
and testing on your own laptop or home machine, but it is highly
recommended that you log in to omega and compile a toy program ASAP,
and that you compile and run an intermediate version of your code well
before the deadline. Notify the instructor for any problems you may
have. <br>
<br>
Pay close attention to all specifications on this page, including
specifications about output format, submission format. Even in cases
where the program works correctly, points will be taken off for
non-compliance with the instructions given on this page (such as a
different format for the program output, wrong compression format for
the submitted code, and so on). The reason is that non-compliance with
the instructions makes the grading process significantly (and
unnecessarily) more time consuming.<br>
<h2>Grading</h2>
The assignments will be graded out of 100 points.<br>
<ul>
<li>40 points: The program always finds a route between the
origin and the destination, as long as such a route exists.</li>
<li>20 points: The program
terminates and reports that no route can be found when indeed no route
exists that connects source and destination (e.g., if source is London
and destination is Berlin, in the above example).</li>
<li>20 points: In addition to the above requirements, the
program always returns optimal routes. In other words, no shorter route
exists than the one reported by the program.</li>
<li>20 points: Correct implementation of any informed search
method.</li>
<li>Negative points: penalty points will be awarded by the
instructor and
TA generously and at will, for issues such as: code not running on
omega, submission not including precise and accurate instructions for
how to run the code, wrong compression format for the submission, or
other failures to comply with the instructions given for this
assignment. Partial credit for incorrect solutions will be given ONLY
for code that is well designed and well documented. Code that is badly
designed and badly documented can still get full credit as long as it
accomplishes the required tasks.
</li>
</ul>
<h2>How to submit</h2>
Implementations in C, C++, Java and Python will be accepted. If you want to you can also use CLISP. If you
would like to use another language, make sure it will compile on omega
and clear it with the instructor beforehand. Points will be taken off
for failure to comply
with this requirement.<br>
The assignment should be submitted via <a href="http://elearn.uta.edu/">Blackboard</a>. Submit a
ZIPPED
directory called assignment1_&lt;net-id&gt;.zip (no other forms
of compression
accepted, contact the instructor or TA if you do not know how to
produce .zip files). The directory should contain source code.
Including binaries&nbsp;is not necessary as your code will be recompiled by the TA.
The submission should also contain a file called readme.txt, which
should specify precisely:<br>
<br>
<ul>
<li>Name and UTA ID of the student.</li>
<li>What programming language is used.</li>
<li>How the code is structured.</li>
<li>How to run the code, including very specific compilation
instructions,
if compilation is needed. Instructions such as "compile using g++" are
NOT considered specific.</li>
<li>Insufficient or unclear instructions will be penalized by
up to 10
points.</li>
<li><span style="font-weight: bold;">Code that
does not run on omega machines gets AT MOST&nbsp;75 points</span>.
</li>
</ul>
<h2>Submission checklist</h2>
Is the code running on omega?<br>
Does the submission include a readme.txt file, as specified?<br>
</body></html>
