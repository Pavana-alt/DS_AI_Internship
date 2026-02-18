# Task 1
import random

trials = 1000

count = 0

for i in range(trials):

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    total = die1 + die2

    if total == 7:
        count = count + 1

probability = count / trials

print("Total trials:", trials)
print("Times sum was 7:", count)
print("Experimental probability:", probability)

#Task 2
import random

p_heads = 1/2
p_six = 1/6
p_and = p_heads * p_six

print("Independent Event:")
print("P(Heads AND 6) =", p_and)

red = 5
blue = 5
total = red + blue

p_first_red = red / total

red_remaining = red - 1
total_remaining = total - 1

p_second_red = red_remaining / total_remaining

p_both_red = p_first_red * p_second_red

print("\nDependent Event:")
print("P(Both marbles are Red) =", p_both_red)

print("\nReflection:")
print("The denominator changed because the first marble was not replaced.")
print("After picking one marble, the total number of marbles decreased.")
print("This makes the second event dependent on the first event.")

print("\nSimulation Verification:")

trials = 10000
count = 0

bag = ["Red"] * 5 + ["Blue"] * 5

for _ in range(trials):
    temp_bag = bag.copy()
    first = random.choice(temp_bag)
    temp_bag.remove(first)
    second = random.choice(temp_bag)

    if first == "Red" and second == "Red":
        count += 1

experimental_probability = count / trials

print("Experimental probability (Both Red) =", experimental_probability)

#Task 3
P_spam = 0.1
P_ham = 0.9

P_free_given_spam = 0.9
P_free_given_ham = 0.05

P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)

P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("P(Spam) =", P_spam)
print("P(Ham) =", P_ham)
print("P(Free | Spam) =", P_free_given_spam)
print("P(Free | Ham) =", P_free_given_ham)

print("\nTotal Probability of 'Free':")
print("P(Free) =", P_free)

print("\nBayes Theorem Result:")
print("P(Spam | Free) =", P_spam_given_free)

print("\nInterpretation:")
print("If an email contains the word 'Free', the probability it is Spam is", round(P_spam_given_free, 3))

