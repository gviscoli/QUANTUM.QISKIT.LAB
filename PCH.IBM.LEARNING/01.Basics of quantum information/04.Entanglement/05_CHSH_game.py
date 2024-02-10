

from qiskit import QuantumCircuit
from qiskit_aer.primitives import Sampler
from numpy import pi
from numpy.random import randint

# 
# When we speak of a game in this context, we're not talking about something that's meant to be played for fun or sport, but rather a mathematical abstraction in the sense of game theory. 
# Mathematical abstractions of games are studied in economics and computer science, for instance, and have great utility.
#
# The letters CHSH refer to the authors — John Clauser, Michael Horne, Abner Shimony, and Richard Holt — of a 1969 paper where the example was first described. 
# They did not describe the example as a game, but rather as an experiment. It's description as a game, however, is both natural and intuitive.
#
#The CHSH game falls within a class of games known as nonlocal games. Nonlocal games are fascinating and have deep connections to physics, computer science, 
# and mathematics — holding mysteries that still remain unsolved. We'll begin the section by explaining what nonlocal games are, 
# and then we'll focus in on the CHSH game and what makes it interesting.
# 
# Nonlocal games
# ==============
# 
# A nonlocal game is a cooperative game where two players, Alice and Bob, work together to achieve a particular outcome. The game is run by a referee, 
# who behaves according to strict guidelines that are known to Alice and Bob.
#
# Alice and Bob can prepare for the game however they choose, but once the game starts they are forbidden from communicating. 
# We might imagine the game taking place in a secure facility of some sort — as if the referee is playing the role of a detective 
# and Alice and Bob are suspects being interrogated in different rooms. But another way of thinking about the set-up is that Alice and Bob are separated by a vast distance, 
# and communication is prohibited because the speed of light doesn't allow for it within the running time of the game. 
# That is to say, if Alice tries to send a message to Bob, the game will be over by the time he receives it, and vice versa.
#
# The way a nonlocal game works is that the referee first asks each of Alice and Bob a question. We'll use the letter X to refer to Alice's question and Y 
# to refer to Bob's question. Here we're thinking of X and Y as being classical states, and in the CHSH game X and Y are bits.
#
# The referee uses randomness to select these questions. To be precise, there is some probability p(X,Y) associated with each possible pair (X,Y)
# of questions, and the referee has vowed to choose the questions, at the time of the game, in this way. 
# Everyone, including Alice and Bob, knows these probabilities — but nobody knows specifically which pair (X,Y) will be chosen until the game begins.
#
# After Alice and Bob receive their questions, they must then provide answers: Alice's answer is B. Again, these are classical states in general, and bits in the CHSH game.
#
# At this point the referee makes a decision: Alice and Bob either win or lose depending on whether or not the pair of answers (A, B) is deemed correct for the pair of questions (X,Y)
# according to some fixed set of rules. Different rules mean different games, and the rules for the CHSH game specifically are described in the section following this one. 
# As was already suggested, the rules are known to everyone.

def chsh_game(strategy):
    """Plays the CHSH game
    Args:
        strategy (callable): A function that takes two bits (as `int`s) and
            returns two bits (also as `int`s). The strategy must follow the
            rules of the CHSH game.
    Returns:
        int: 1 for a win, 0 for a loss.
    """
    # Referee chooses x and y randomly
    x, y = randint(0, 2), randint(0, 2)

    # Use strategy to choose a and b
    a, b = strategy(x, y)

    # Referee decides if Alice and Bob win or lose
    if (a != b) == (x & y):
        return 1  # Win
    return 0  # Lose

def chsh_circuit(x, y):
    """Creates a `QuantumCircuit` that implements the best CHSH strategy.
    Args:
        x (int): Alice's bit (must be 0 or 1)
        y (int): Bob's bit (must be 0 or 1)
    Returns:
        QuantumCircuit: Circuit that, when run, returns Alice and Bob's
            answer bits.
    """
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.barrier()

    # Alice
    if x == 0:
        qc.ry(0, 0)
    else:
        qc.ry(-pi / 2, 0)
    qc.measure(0, 0)

    # Bob
    if y == 0:
        qc.ry(-pi / 4, 1)
    else:
        qc.ry(pi / 4, 1)
    qc.measure(1, 1)

    return qc

# Draw the four possible circuits

import os
os.system('cls')

print("(x,y) = (0,0)")
print(chsh_circuit(0, 0).draw())
print()

print("(x,y) = (0,1)")
print(chsh_circuit(0, 1).draw())
print()

print("(x,y) = (1,0)")
print(chsh_circuit(1, 0).draw())
print()

print("(x,y) = (1,1)")
print(chsh_circuit(1, 1).draw())

print()
print()

# Now we'll create a job using the Aer simulator that runs the circuit a single time for a given input pair (X,Y)

sampler = Sampler()

def quantum_strategy(x, y):
    """Carry out the best strategy for the CHSH game.
    Args:
        x (int): Alice's bit (must be 0 or 1)
        y (int): Bob's bit (must be 0 or 1)
    Returns:
        (int, int): Alice and Bob's answer bits (respectively)
    """
    # `shots=1` runs the circuit once
    result = sampler.run(chsh_circuit(x, y), shots=1).result()
    statistics = result.quasi_dists[0].binary_probabilities()
    bits = list(statistics.keys())[0]
    a, b = bits[0], bits[1]
    return a, b

# Finally, we'll play the game 1,000 times and compute the fraction of them that the strategy wins.

NUM_GAMES = 1000
TOTAL_SCORE = 0

for _ in range(NUM_GAMES):
    TOTAL_SCORE += chsh_game(quantum_strategy)

print()
print("STRATEGY 1")

print("Fraction of games won:", TOTAL_SCORE / NUM_GAMES)

print()
print()

# We can also define a classical strategy and see how well it works. Feel free to change the code to try out different strategies!

def classical_strategy(x, y):
    """An optimal classical strategy for the CHSH game
    Args:
        x (int): Alice's bit (must be 0 or 1)
        y (int): Bob's bit (must be 0 or 1)
    Returns:
        (int, int): Alice and Bob's answer bits (respectively)
    """
    # Alice's answer
    if x == 0:
        a = 0
    elif x == 1:
        a = 1

    # Bob's answer
    if y == 0:
        b = 1
    elif y == 1:
        b = 0

    return a, b

# Again let's play the game 1,000 times to see how well it works

NUM_GAMES = 1000
TOTAL_SCORE = 0

for _ in range(NUM_GAMES):
    TOTAL_SCORE += chsh_game(classical_strategy)

print()
print("STRATEGY 2")

print("Fraction of games won:", TOTAL_SCORE / NUM_GAMES)

print()
print()
