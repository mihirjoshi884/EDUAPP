


"""
This function  helps in generating unique student id for std_id which is a primary key
of table - stdinfo which belongs to  database - __edu_database__ .
In this function string , secerets , random module are used to build random and unique id .

STRING MODULE - The string module contains a number of useful constants and classes .
                deprecated legacy functions that are also available as methods on strings.
                In addition, Python’s built-in string classes support the sequence type methods described in the Sequence .
                This types — str, unicode, list, tuple,etc. and also the string-specific methods described in the String Methods section.

SECRETES MODULE - The secrets module is used for generating cryptographically strong random
                  numbers suitable for managing data such as passwords, account authentication,
                  security tokens, and related secrets.

                  In particularly, secrets should be used in preference to the default pseudo-random
                  number generator in the random module, which is designed for modelling and simulation,
                  not security or cryptography.

RANDOM MODULE -  This module implements pseudo-random number generators for various distributions.

                 For integers, there is uniform selection from a range. For sequences, there is uniform
                 selection of a random element, a function to generate a random permutation of a list in-place,
                 and a function for random sampling without replacement.

"""
import string ,secrets,random


#select a uppercase
upper=secrets.choice(string.ascii_uppercase)
# select a lowercase
lower=secrets.choice(string.ascii_lowercase)
# select a number
digit=secrets.choice(string.digits)
# put the selected 3 char together
selected_chars=list()
selected_chars.extend(upper)
selected_chars.extend(lower)
selected_chars.extend(digit)
#select rest chars in all allowed chars:6-3=3
allowedchars = upper + lower + digit
selected_rest_chars = [secrets.choice(allowedchars)for _ in range(3)]
# put the selected 3 chars with the rest 17 chars together
selected_rest_chars.extend(selected_chars)
#shuffle the 6 chars - this our id
random.shuffle(selected_rest_chars)
# combine the chars to our id
id ="".join(selected_rest_chars)
ap=print(id)
