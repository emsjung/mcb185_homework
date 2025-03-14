# if health drops to <=0, unconscious/die
#roll d20
	# if <10, record a "failure"
	# if >=10, record a "success"
	# if collect 3 failures, you "die"
	# if collect 3 successes, you are "stable" but unconscious 
	# roll a 1, counts as 2 failures 
	# roll a 20, gain 1 health and "revived"

import random

def sim_deathsave():
    failure = 0
    success = 0
    while failure < 3 and success < 3:
        roll = random.randint(1, 20)
        if roll == 1:
            failure += 2
        elif roll == 20:
            return 20
        elif roll < 10:
            failure += 1
        elif roll >= 10:
            success += 1
    if failure == 3:
        return False
    elif success == 3:
        return True

def sim_revives(sim_num):
    num_revives = 0
    for i in range(sim_num):
        if sim_deathsave() == 20:
            num_revives += 1
    p_revives = num_revives / sim_num
    return p_revives

def sim_deaths(sim_num):
    num_death = 0
    for i in range(sim_num):
        if sim_deathsave() == False:
            num_death += 1
    p_death = num_death / sim_num
    return p_death

def sim_stabalize(sim_num):
    num_stable = 0
    for i in range(sim_num):
        if sim_deathsave() == True:
            num_stable += 1
    p_stable = num_stable / sim_num
    return p_stable


print('Probability of Revive: ', sim_revives(100000))
print('Probability of Death: ', sim_deaths(100000))
print('Probability of Stabilizing: ', sim_stabalize(100000))
	