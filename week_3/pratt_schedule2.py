schedule = {
	"monday" :   ['Human-Information Behavior','Information Professions','Research Mthds/Law Lit','Strategic Leadership','Conservation and Preservation','Info Services & Resources'],
	"tuesday":   ['Information Arch/Inter Design','Information Professions','Acad Libraries and Scholarly','Info Services & Resources'],
	"wednesday": ['Info Services & Resources','Usability Theory & Practice','Mgmt of Archives/Sp Collection','Government Info Sources','Library Media Centers','Mgmt of Archives/Sp Collection'],
	"thursday": ['Information Science Research','Information Professions','Information Professions'],
}


#loop through each day in schedule, print the name of the day, and then loop through all the class names and print them out

# start reading at 0 in the list
for day in schedule:
#for each day in the schedule
	print(day)
	#print the day

	#variables:
	length_of_list = len(schedule[day])
	#monday has 6 courses. the length is 6
	locator = 0

	#loop:
	while(locator < length_of_list):
	#while the locator is less than 6
		print(schedule[day][locator])
		#print the class 0-6
		locator = locator + 1
		#locator moves to next spot

#output sample:

# ❯ python3 pratt_schedule2.py
# monday
# Human-Information Behavior
# Information Professions
# ...

