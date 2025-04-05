def is_anagram(s, t):
    if sorted(s) == sorted(t):
    	return True
    else:
    	return False
	
# the sorted() function in Python can be used for strings. 
# When applied to a string, it sorts the characters alphabetically based on their Unicode code points and returns 
# a new list containing the sorted characters.