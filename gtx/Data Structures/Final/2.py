#Write a function called write_movie_info. write_movie_info
#will take as input two parameters: a string and a
#dictionary.
#
#The string will represent the filename to which to write.
#
#The keys in the dictionary will be strings representing
#movie titles. The values in the dictionary will be lists
#of strings representing performers in the corresponding
#movie.
#
#write_movie_info should write the list of movies to the file
#given by the filename using the following format:
#
# Title: Actor 1, Actor 2, Actor 3, etc.
#
#The movies and the actor names should be sorted
#alphabetically.
#
#So, for this dictionary:
#
# {"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"],
#  "Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}
#
#The file printed would look like this:
#
# Chocolat: Alfred Molina, Johnny Depp, Judi Dench, Juliette Binoche
# Skyfall: Daniel Craig, Javier Bardem, Judi Dench, Naomie Harris
#
#HINT: the keys() method of a Dictionary will return a list
#of the dictionary's keys. So, to get a sorted list of a_dict's
#keys, you could call key_list = a_dict.keys(), then call 
#key_list.sort().


#Write your function here!
def write_movie_info(fileName, movies):
    if type(movies) == dict:
        write_dict_info(fileName, movies)
    else:
        write_list_info(fileName, movies)

def write_list_info(fileName, movies):
    myFile = open(fileName, "w")
    for d in movies:
        for key, value in sorted(d.items()):
            value.sort()
            myFile.write(key + ": ")
            myFile.write(", ".join(value) + "\n")
        
    myFile.close()

def write_dict_info(fileName, movies):
    myFile = open(fileName, "w")
    for key, value in sorted(movies.items()):
        value.sort()
        myFile.write(key + ": ")
        myFile.write(", ".join(value) + "\n")
        
    myFile.close()


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print nothing -- however, it should write the same contents
#as Sample.txt to Test.txt.
movies = [{"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"], "Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}]
movies2 = {'Down and Out in Beverly Hills': ['Nick Nolte', 'Richard Dreyfuss', 'Bette Midler', 'Little Richard', 'Tracy Nelson', 'Elizabeth Pena', 'Paul Mazursky'], 'Nine Months': ['Hugh Grant', 'Julianne Moore', 'Jeff Goldblum', 'Tom Arnold', 'Joanne Cusack', 'Mia Ottell', 'Robin Williams', 'Paul Simon'], 'Con Air': ['Nicolas Cage', 'John Malkovich', 'Steve Buscemi', 'Ving Rhames', 'John Cusack'], 'Young Frankenstein': ['Gene Wilder', 'Peter Boyle', 'Madeline Kahn', 'Marty Feldman', 'Cloris Leachman', 'Teri Garr', 'Liam Dunn', 'Kenneth Mars', 'Gene Hackman', 'Mel Brooks'], 'The Count of Monte Cristo': ['Richard Chamberlain', 'Trevor Howard', 'Louis Jourdan']}
write_movie_info("Test.txt", movies2)



# Specifications says it expects a dictionary, but the first test case passes in a list of dicts

# We found a few things wrong with your code. The first one is shown below, and the rest can be found in full_results.txt in the dropdown in the top left:

# We tested your code with movie_dict = {'Down and Out in Beverly Hills': ['Nick Nolte', 'Richard Dreyfuss', 'Bette Midler', 'Little Richard', 'Tracy Nelson', 'Elizabeth Pena', 'Paul Mazursky'], 'Nine Months': ['Hugh Grant', 'Julianne Moore', 'Jeff Goldblum', 'Tom Arnold', 'Joanne Cusack', 'Mia Ottell', 'Robin Williams', 'Paul Simon'], 'Con Air': ['Nicolas Cage', 'John Malkovich', 'Steve Buscemi', 'Ving Rhames', 'John Cusack'], 'Young Frankenstein': ['Gene Wilder', 'Peter Boyle', 'Madeline Kahn', 'Marty Feldman', 'Cloris Leachman', 'Teri Garr', 'Liam Dunn', 'Kenneth Mars', 'Gene Hackman', 'Mel Brooks'], 'The Count of Monte Cristo': ['Richard Chamberlain', 'Trevor Howard', 'Louis Jourdan']}, filename = "AutomatedTest-RDwrpJ.txt". We expected write_movie_info to return the str 
# "Con Air: John Cusack, John Malkovich, Nicolas Cage, Steve Buscemi, Ving Rhames
# Down and Out in Beverly Hills: Bette Midler, Elizabeth Pena, Little Richard, Nick Nolte, Paul Mazursky, Richard Dreyfuss, Tracy Nelson
# Nine Months: Hugh Grant, Jeff Goldblum, Joanne Cusack, Julianne Moore, Mia Ottell, Paul Simon, Robin Williams, Tom Arnold
# The Count of Monte Cristo: Louis Jourdan, Richard Chamberlain, Trevor Howard
# Young Frankenstein: Cloris Leachman, Gene Hackman, Gene Wilder, Kenneth Mars, Liam Dunn, Madeline Kahn, Marty Feldman, Mel Brooks, Peter Boyle, Teri Garr". However, it instead encountered the following error:

# AttributeError: 'str' object has no attribute 'items'