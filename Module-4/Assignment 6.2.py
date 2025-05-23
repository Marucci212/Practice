# Justin Marucci 
# Assignment 6.2
# 02/09/2025

# Initialize a tuple with automobile types
formula_one_teams = (
    'Ferrari', 'Mercedes', 'Mclaren', 'Aston Martin', 'Alpine',
    'Williams', 'Renault', 'Alpha Romeo', 'Red Bull', 'Alpha Tauri',
    'Audi', 'Haas', 'Williams', 'Sauber', 'Jaguar'
)

# Display the contents in a single statement
print("Formula One Teams: ", formula_one_teams)

# Iterate through the collection, displaying the output as a complete sentence
for team in formula_one_teams:
    print(f'The best team in motorsport is {team}.')

# Repeat the output in reverse order using a different context string
for team in reversed(formula_one_teams):
    print(f'{team} is the most advanced team in the world.')