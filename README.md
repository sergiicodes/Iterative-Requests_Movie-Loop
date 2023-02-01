# Iterative-Requests_Movie-Loop

This code is making API requests to the OMDb API to retrieve information about user inputted variables.
The logic of making an API request is done via a function get_movie_info which takes in the title and the info_key as arguments and returns the requested information. 
A while loop is used to continuously prompt the user for movie titles and keys until the user decides to quit by entering 'quit'. 
The input is then passed as arguments to the get_movie_info function and the result is printed to the console.
