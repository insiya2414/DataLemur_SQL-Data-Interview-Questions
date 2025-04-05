def is_palindrome(phrase: str) -> bool:
    # Filter out non-alphanumeric characters and convert to lowercase
    cleaned_phrase = ''.join(c.lower() for c in phrase if c.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_phrase == cleaned_phrase[::-1]

# ____________________________________________________________________________________________________________________________________
#DataLemur Solution:

def isPalindrome(phrase):
  # initialize pointers
  left = 0
  right = len(phrase)-1
  
  while left < right:
    # skip over non-alphanumeric
    if not phrase[left].isalnum():
      left = left+1
      continue
    if not phrase[right].isalnum():
      right = right-1
      continue
    
    # ready to compare opposite sides
    if phrase[left].lower() == phrase[right].lower():  
      left = left+1
      right = right-1
    else:
      return False
  
  # if no more comparisons left to make
  return True