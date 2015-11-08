This is a program that, when fed an itinerary of city locations, tells you the distance it takes to travel to each of them, in order.

The program file, Vacationing-Salesman.py, is a python file that runs with Python 3.
To use it, run it through terminal/command prompt and pipe in a .txt file that contains a list of line separated city names.

For instance, on my Windows git bash command prompt, I use the command:

    python Vacationing-Salesman.py < cities.txt
    
Q: Why python?

A: I chose python for this problem because I knew there'd be a lot of things I'd have to search up and figure out, and python is best for me when it comes to quickly prototyping new concepts.


Q: Talk about your design decisions.

A: I decided to make it a single file to make the work quick and concise. I choose the google geocoding API for grabbing the data, then the rest was just processing the GET request and handling the data.


Q: What features would you implement if you had more time?

A: All the optional bits suggested by the problem statement. First would be the use of flags to choose units. Then I could use Google Map's distance API to get different modes of travel. Optimizing paths would come after that (or at least my best attempt at it).
