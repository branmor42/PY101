countries = ['Australia', 'Cuba', 'Senegal']

alpha_insert(countries, 'Brazil')
print(', '.join(countries))  # Outputs "Australia, Brazil, Cuba, Senegal"

alpha_insert([], 'Brazil')             # Inserting into an empty list
alpha_insert(['Brazil'], 'Australia')  # At the beginning of a list
alpha_insert(['Brazil'], 'Cuba')       # At the end of a list
alpha_insert(['Brazil'], 'Brazil')     # Duplicate entry