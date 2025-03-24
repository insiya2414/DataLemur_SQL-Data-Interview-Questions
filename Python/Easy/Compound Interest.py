def compound_interest(principal, rate, contribution, years):
    r = rate / 100
    # Calculate compound interest on the initial investment
    initial_compound = principal * ((1 + r) ** years)
    # Calculate compound interest on the annual contributions
    contribution_compound = contribution * (((1 + r) ** years - 1) / r)
    # Sum the two parts for the total amount
    total = initial_compound + contribution_compound
    return round(total, 2)
