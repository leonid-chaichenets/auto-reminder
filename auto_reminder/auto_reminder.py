#!/usr/bin/python3
# SPDX-License-Identifier: MIT

u'''Reminder for cleaning duties.'''

import datetime
import locale
from email.mime.text import MIMEText

# Version
ver = 20170123-1

# Reminder’s address.
me = 'Autoreminder <email@example.com>'

# Flatmates and their addresses.
Fs = [('Roomie1',
	'First1 Last1 <email1@example.com>'),
	('Roomie2', 'First2 Last2 <email2@example.com>'),
	('Roomie3', 'First3 Last3 <email3@example.com>')]

# The date on which the agreement on cleaning duties had been fixed.
d_0 = datetime.date(2017,1,9)

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
	['Clean the mirrors and wipe the furniture in the common ' \
		'areas.'],
	['Clean exhaust hood and wipe the tiled wall in the kitchen.']]

if __name__ == "__main__":

	# Enforce locale.
	locale.setlocale(locale.LC_TIME, "de_DE.utf8")

	# Current date.
	d_1 = datetime.date.today()

	# ISO week number.
	iso_week = d_1.isocalendar()[1]

	# Dates of Monday and Sunday of the current week.
	dow = d_1.weekday()
	mon = d_1 + datetime.timedelta(days=-dow)
	mon_str = mon.strftime('%x')
	sun = d_1 + datetime.timedelta(days=6-dow)
	sun_str = sun.strftime('%x')

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

	# Add headers.
	msg = MIMEText(mail_body)
	msg['Subject'] = \
		'Cleaning duties reminder for ISO week %s (%s - %s).' \
	        % (iso_week, mon_str, sun_str)
	msg['To'] = Fs[f][1]
	msg['From'] = me
	msg['Bcc'] = me
	
	print(msg)
