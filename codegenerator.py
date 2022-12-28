
import random
import string

for i in range(30):
    # get random string of length 5 without repeating letters
    result_str = ''.join(random.sample(string.ascii_lowercase, 5))
    print(result_str)


