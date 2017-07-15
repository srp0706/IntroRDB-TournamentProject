# Udacity's Introduction to Relational Databases course

This repository was created to host my code for the final programming
assignment in the course, a simple database that yields Swiss Pairings
for players in a tournament.

For the complete course see here:
[UdacityIntroRDB](https://www.udacity.com/course/intro-to-relational-databases--ud197/ "Intro to Relational Databases - Udacity")

In order to use this code, some setup steps are required. The course
recommends the use of VirtualBox and Vagrant to setup a virtual machine
that runs the database. The virtual machine itself is provided by
Udacity, but the code in it must be replaced with the code in this
repository.

The crash course drill goes as follows:

1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads "VirtualBox downloads")  
   **A note to Ubuntu users**: if you use Ubuntu 14.04, install VirtualBox
from Ubuntu Software Center instead.
2. Install [Vagrant](https://www.vagrantup.com/downloads.html "Vagrant downloads")
3. Download the virtual machine configuration from [this zip file](https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip "Udacity VM configuration") or
fork their GitHub repository [https://github.com/udacity/fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm).
4. Replace the files in the *tournament* directory with the files in
this repository.
5. Launch Vagrant by issuing the command `vagrant up` from a terminal.
The first time you run this command, the system will download the
virtual machine system and libraries, and it may take quite a while
depending on your internet connection speed.
6. Login to your virtual machine with `vagrant ssh` in the terminal.
7. If all went well so far, you can now go to the tournament directory
and create the *tournament* database with the command 
`psql -f tournament.sql`.
8. Now run the unit tests by issuing the command `python tournament_test.py` 
from your vagrant shell. You should see detailed test messages and a 
final one stating "`Success!  All tests pass!`".

If not everything went as it should, there's a waaaay more detailed
explanation and a troubleshooting guide by the kind folks at Udacity.
Here you go: [VM Setup and troubleshooting](https://classroom.udacity.com/courses/ud197/lessons/3423258756/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)

... although I'm not sure this link will work without being enrolled
in the course.

Have fun exploring!  
srp
