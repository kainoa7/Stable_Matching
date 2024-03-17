def stable_matching(men_preferences, women_preferences):
    # Initialize all men and women as free
    free_men = list(men_preferences.keys())
    engaged = {}
    
    # While there is at least one free man
    while free_men:
        man = free_men.pop(0)  # Choose a free man
        
        # Get the preferences of the current man
        preferences = men_preferences[man]
        
        # Iterate through the man's preferences
        for woman in preferences:
            if woman not in engaged:  # If the woman is free
                engaged[woman] = man
                break
            else:
                # Get the current engagement of the woman
                current_engagement = engaged[woman]
                
                # Check if the woman prefers the current man to her current engagement
                if women_preferences[woman].index(man) < women_preferences[woman].index(current_engagement):
                    engaged[woman] = man
                    free_men.append(current_engagement)  # Put the current man back to the pool of free men
                    break
    
    return engaged

# Example preferences (men and women preferences)
men_preferences = {
    'm1': ['w1', 'w2', 'w3'],
    'm2': ['w2', 'w1', 'w3'],
    'm3': ['w1', 'w2', 'w3']
}

women_preferences = {
    'w1': ['m1', 'm2', 'm3'],
    'w2': ['m3', 'm2', 'm1'],
    'w3': ['m1', 'm3', 'm2']
}

# Compute stable matching
engaged_pairs = stable_matching(men_preferences, women_preferences)
print("Stable matching:", engaged_pairs)
