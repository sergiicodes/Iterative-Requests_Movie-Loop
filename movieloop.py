# Dependencies
import requests               # Importing the requests library
from config import api_key    # Importing the api_key from a separate config file

# Creating the base URL for the API requests
url = "http://www.omdbapi.com/?apikey=" + api_key + "&t="

def get_movie_info(title, info_key):
    # Making the API request using the title and retrieving the response as JSON
    movie_data = requests.get(url + title).json()
    # Returning the requested information (the value of the specified key in movie_data)
    return movie_data[info_key]

# Starting the while loop to continuously prompt for user inputs
while True:
    # Prompting the user for a movie title
    movie = input("Enter a movie title (or type 'quit' to exit): ")
    # If the user enters 'quit', breaking out of the loop
    if movie == 'quit':
        break
    # Prompting the user for the information they want to retrieve
    key = input("Enter the info you want to retrieve (e.g. Director, Writer, Year, etc.): ")
    # Getting the requested information by calling the get_movie_info function with the movie title and key
    result = get_movie_info(movie, key)
    # Printing the result to the console
    print(f'The {key} of {movie} is {result}')
