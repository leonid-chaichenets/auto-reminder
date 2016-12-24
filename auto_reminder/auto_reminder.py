#!/usr/bin/python3
# -*- coding: utf-8 -*-

u'''Reminder for cleaning duties.'''

import datetime

# Flatmates and their addresses
Fs = [('Roomie2', 'First2 Last2', 'email2@example.com'),
	('Roomie3' 'First3 Last3', 'email3@example.com'),
	('Roomie1', 'First1 Last1',
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
Ds1 = [['Vacuum clean the common areas.',
        'Dispose of garbage.',
	'Unload the dish washer, if necessary.',
	'Replentish toilet paper and paper towels, if necessary.']]

# M = 2
Ds2 = [['Wipe the floors in the common areas.',
	'Renew towels in bathroom and kitchen.'],
	['Clean the sinks and wet clean the kitchen surfaces.',
	 'Replentish dish washing salt, if necessary.']]

# M = 3 not possible

# M = 4
Ds4 = [['Clean the toilet seat.'],
	['Clean the shower (remove fungus).'],
	['Clean the mirrors and wipe the furniture in the kitchen'],
	['Clean exhaust hood and wipe the tiled wall in the kitchen.']]

if __name__ == "__main__":

	# Current date.
	d_1 = datetime.date.today()

	# Number of weeks passed.
	w = (d_1 - d_0).days // 7

	# Number of flatmates.
	n = len(Fs)
        
	# Calculate person on duty this week.
	f = w % n

	# Calculate the duties for the week.
	d1 = w % 1
	d2 = w % 2
	d4 = w % 4

	# Assemble text of the email.
	opening = 'Hello ' + Fs[f][0] + ',\n\n'
	text = 'you are on cleaning duty this week. '
	duties_list = 'Your duties are as follows.\n'
	duties_list += '\n* One week period:\n\n'
	for i in Ds1[d1]:
		duties_list += '\t- ' + i + '\n'
	duties_list += '\n* Two week period:\n\n'
	for i in Ds2[d2]:
		duties_list += '\t- ' + i + '\n'
	duties_list += '\n* Four week period:\n\n'
	for i in Ds4[d4]:
		duties_list += '\t- ' + i + '\n'
	signature = '\n-- \n' + 'Kind regards\n' + 'Your autoreminder'
	mail_body = opening + text + duties_list + signature

	print(mail_body)
#	print("Week", "1st", "2nd", "3d", "4th", sep='\t')
#	for i in range(52):
#		print(i, i % 1, i % 2, i % 4, i % 5, sep='\t')
