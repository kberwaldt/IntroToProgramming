stateAndCapital = [['Alabama', 'Montgomery'],
['Alaska', 'Juneau'],
['Arizona','Phoenix'],
['Arkansas','Little Rock'],
['California','Sacramento'],
['Colorado', 'Denver'],
['Connecticut', 'Hartford'],
['Delaware', 'Dover'],
['Florida', 'Tallahassee'],
['Georgia', 'Atlanta'],
['Hawii', 'Honolulu'],
['Idaho', 'Boise'],
['Illinois', 'Springfield'],
['Indiana', 'Indianapolis'],
['Iowa', 'Des Moines'],
['Kansas', 'Topeka'],
['Kentucky', 'Frankfort'],
['Louisiana', 'Baton Rouge'],
['Maine', 'Augusta'],
['Maryland', 'Annapolis'],
['Massachusetts', 'Boston'],
['Michigan', 'Lansing'],
['Minnesota', 'Saint Paul'],
['Mississippi','Jackson'],
['Missouri', 'Jefferson City'],
['Montana', 'Helena'],
['Nebraska','Lincoln'],
['Nevada', 'Carson City'],
['New Hampshire', 'Concord'],
['New Jersey', 'Trenton'],
['New Mexico', 'Santa Fe'],
['New York', 'Albany'],
['North Carolina', 'Raleigh'],
['North Dakota', 'Bismarck'],
['Ohio', 'Columbus'],
['Oklahoma', 'Oklahoma City'],
['Oregon', 'Salem'],
['Pennsylvania', 'Harrisburg'],
['Rhode Island', 'Providence'],
['South Carolina', 'Columbia'],
['South Dakota', 'Pierre'],
['Tennessee', 'Nashville'],
['Texas', 'Austin'],
['Utah', 'Salt Lake City'],
['Vermont', 'Montpelier'],
['Virginia', 'Richmond'],
['Washington', 'Olympia'],
['West Virginia', 'Charleston'],
['Wisconsin', 'Madison'],
['Wyoming', 'Cheyenne']]

"""Defined game levels"""
gamelevels = ['easy', 'medium', 'hard']

"""Selecting game difficulty and validating correct entry"""
print "USA States and Capitals!"
str_levels = ""
index = 0
while index < len(gamelevels) - 1:
    str_levels += gamelevels[index] + ", "
    index += 1
str_levels += "or " + gamelevels[index] + "."

user_input = raw_input("Select a game difficulty " + str_levels + " ")

def gamedifficulty(difficulty):
    """Looping through game difficulty choice until a valid entry is chosen"""
    while difficulty.lower() not in gamelevels:
        difficulty = raw_input("Type a game difficulty " + str_levels + " ")
    return difficulty.lower()

import random
def gamesample(difficulty):
    """Choosing random states and capitals based off difficulty"""
    listrange = len(stateAndCapital) - 1
    if difficulty == 'easy':
        return random.sample(xrange(0,listrange),4)
    if difficulty == 'medium':
        return random.sample(xrange(0,listrange),8)
    if difficulty == 'hard':
        return random.sample(xrange(0,listrange),12)

def play_game(sample):
    """Using the previous functions to determine the amount of times to loop through the states"""
    index = 0
    wrongEntry = 0
    user_input_question = ""
    while index < len(sample) and user_input_question.title() != stateAndCapital[sample[index]][1]:
        #Creating Question
        str_state = stateAndCapital[sample[index]][0]
        str_capital = stateAndCapital[sample[index]][1]
        user_input_question = raw_input("The capital of " + str_state + " is? ")
        if user_input_question.title() == stateAndCapital[sample[index]][1]:
            print "Correct! " + str_capital + " is the capital of " + str_state + "."
            index += 1
        else:
            wrongEntry += 1
    if wrongEntry > 0:
        return "Can you do better next time? " + str(wrongEntry) + " incorrect guesses"
    else:
        return "Great Work!"

print play_game(gamesample(gamedifficulty(user_input)))
