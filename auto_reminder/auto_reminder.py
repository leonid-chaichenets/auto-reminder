#!/usr/bin/python3
# -*- coding: utf-8 -*-

u'''Reminder for cleaning duties.'''

import datetime

# Flatmates and their addresses
Fs = [('Roomie4'u, 'First4 Last4'u, 'email4@example.com'),
	('Roomie3'u 'First3 Last3'u, 'email3@example.com'),
	('Roomie1'u, 'First1 Last1',
         	'email1@example.com')]

# The date on which the agreement on cleaning duties had been fixed.
d_0 = datetime.date(2016,11,17)

# Each of the N flatmates is on duty every N weeks (and has # N-1 weeks
# to recover from the cleaning stress :)). Cleaning duties repeat
# regulary. Say there are M cleaning duties and each is repeated every M
# weeks. No flatmate should be excluded from a duty, i.e. the
# simultanious congruences w = f mod N and w = d mod M must be solvable
# for any 1 <= f <= N and any 1 <= d <= M (w = week number,
# f = flatmate, d = duty). By the Chinese remainder theorem the
# equivalent condition is gcd(N,M) = 1.

# M = 1
D_1 = [('Vacuum clean the common areas.'u,
        'Dispose of garbage.'u,
	'Unload the dish washer.'u,
	'Replentish toilet paper and paper towels, if necessary.')]

# M = 2
D_2 = [('Wipe the floors in the common areas.'u,
	'Renew towels in bathroom and kitchen.'),
	('Clean the sinks and wet clean the kitchen surfaces.'u,
	 'Replentish dish washing salt.'u)]

# M = 3 not possible

# M = 4
D_4 = [('Clean the toilet seat.'u),
	('Clean the shower (remove fungus).'u),
	('Clean the mirrors and wipe the furniture in the kitchen'u),
	('Clean exhaust hood and wipe the tiled wall in the kitchen.'u)]

if __name__ == "__main__":

	# Current date.
	d_1 = datetime.date.today()

	# Number of weeks passed.
	w = (d_1 - d_0).days // 7

	# Calculate person on duty this week.
	o = w % 3

	print("Week", "1st", "2nd", "3d", "4th", sep='\t')
	for i in range(52):
		print(i, i % 1, i % 2, i % 4, i % 5, sep='\t')
