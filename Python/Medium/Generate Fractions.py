import math

def generate_fractions(n):
    result = []  
	 # Numerators from 1 up to n
    for numerator in range(1, n): 
    	 # Denominators > numerator
        for denominator in range(numerator + 1, n + 1): 
            '''
            Only add if the fraction is already in 
            simplest form (GCD is 1)
            '''
            if math.gcd(numerator, denominator) == 1:
            	# Add to result
                result.append([numerator, denominator])  

    return result