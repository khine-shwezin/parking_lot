# parking_lot
Application for parking_lot

-----------   $ bin/setup  -----------
To install all dependencies, compile and run tests.
It downloads and runs pytest, for customised test cases.
It calls bin\run_functional_tests, to verify the given standard test suits.
All should be passed.

-----------   bin/run_functional_tests  -----------
It runs and verifies the given standard test suits

-----------   $ bin/parking_lot file_inputs.txt  -----------
 To run the code so it accepts input from a file: $ bin/parking_lot file_inputs.txt
 file_inputs.txt can be placed any where under root, which is parking_lot folder.

 -----------   $ bin/parking_lot  -----------
Going into interactive mode, to run the program and launch the shell:

Assuming a parking lot with 6 slots, the following commands should be run in sequence by typing them in at a prompt and should produce output as described below the command. Note that  ​exit ​terminates the process and returns control to the shell.

$ create_parking_lot 6
Created a parking lot with 6 slots

$ park KA-01-HH-1234 White
Allocated slot number: 1

$ park KA-01-HH-9999 White
 Allocated slot number: 2

$ park KA-01-BB-0001 Black
Allocated slot number: 3

 $ park KA-01-HH-7777 Red
 Allocated slot number: 4

 $ park KA-01-HH-2701 Blue
 Allocated slot number: 5

 $ park KA-01-HH-3141 Black
 Allocated slot number: 6

 $ leave 4
 Slot number 4 is free

 $ status
 Slot No. Registration No Colour
 1     KA-01-HH-1234     White
 2     KA-01-HH-9999     White
 3     KA-01-BB-0001     Black
 5     KA-01-HH-2701      Blue
 6     KA-01-HH-3141     Black


$ park KA-01-P-333 White
Allocated slot number: 4

$ park DL-12-AA-9999 White
Sorry, parking lot is full

$ registration_numbers_for_cars_with_colour White
KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333

$ slot_numbers_for_cars_with_colour White
1, 2, 4

$ slot_number_for_registration_number KA-01-HH-3141
6

$ slot_number_for_registration_number MH-04-AY-1111
Not found

$ exit

---------------------------------------------
-----------   Khine Shwe Zin      -----------
-----------   shwezin.k@gmail.com -----------
-----------   20 June 2019        -----------
---------------------------------------------