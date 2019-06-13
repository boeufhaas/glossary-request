from sys import exit

user_list = ['a', 'b', 'c', 'd']
context_list = ['oven', 'steamer', 'washing machine', 'tumble dryer', 'hob', 'range hood', 'microwave', 'coffeemaker', 'general use']
action_list = ['Add an entry', 'Modify an entry', 'Quit']
source_language_list  = ['German', 'English', 'Mixture']
entry_dict = {'1':'some_languages', '2':'all_languages', '3':'all_languages', '4':'some_languages'}
change_list = ['Add a language', 'Change an existing language']
all_languages_list = ['deCH', 'deDE', 'frCH', 'frFR', 'itCH', 'itIT', 'enGB', 'nlNL', 'ruRU', 'trTR', 'ukUA', 'zhCN', 'esES']
some_languages_list = ['deCH', 'frCH', 'itCH', 'enGB', 'nlNL', 'ruRU', 'trTR', 'ukUA', 'zhCN', 'esES']

entry_list = [   {'entry_id': '1',
                 'language': 'German',
                 'type': 'de-CH',
                 'term':'Hoi',
				 'id': '1234'},

                {'entry_id': '1',
                 'language': 'German',
                 'type': 'de-DE',
                 'term':'Hallo',
				 'id': '1235'},
				 
				{'entry_id': '1',
                 'language': 'French',
                 'type': 'fr-CH',
                 'term':'Salut',
				 'id': '1236'},
				 
				{'entry_id': '1',
                 'language': 'French',
                 'type': 'fr-FR',
                 'term':'Allo',
				 'id': '1237'},
				 
				{'entry_id': '1',
                 'language': 'Turkish',
                 'type': 'tr-TR',
                 'term':'Merhaba',
				 'id': '1238'},
				 
				{'entry_id': '2',
                 'language': 'German',
                 'type': 'de-CH',
                 'term':'Karotte',
				 'id': '2234'},
				 
				{'entry_id': '2',
                 'language': 'French',
                 'type': 'fr-CH',
                 'term':'Carotte',
				 'id': '2235'},
				 
				{'entry_id': '2',
                 'language': 'Turkish',
                 'type': 'tr-TR',
                 'term':'Havuc',
				 'id': '2236'},
				 
				 ]

g_logged_in = ""#g for global. is needed
entry_number = "" #see ATTEMPTS
summary = []#see def end_request()

# note 1: I first wanted to make the script run with the version you see below (lots of definitions)
# to then try to transform it into a more clean version with the use of the Cmd module.
# note 2: I did not manage to make the definition do_modify_entry() work (see all the ATTEMPTS), 
# which is why I did not yet use the Cmd module or build a repl.
# note 3: Next tasks: Using the Cmd module and building a repl.
# note 4: Next tasks: Finding out how to use list comprehensions and list comprehensions.
# note 5: Next tasks: Finding out why the ATTEMPTs did not work and in what context they make sense/can be purposefully used.

def end_request():
	print "Thank you very much. Your request will be evaluated."
	#summary of all the answers: 
	#I would like to collect the user's actions and display them
	#in this manner: New entry: abcd. Language: German. Translatable: yes. ...
	#The solution as of now is "summary.append()" within every definition.
	
	exit()

def do_add_definition(word):
	definition = "Please enter a definition of '%s'." % word
	print "%s" % definition
	entry_definition = raw_input() # summary.append(do_add_definition)
	end_request()

def device(word):

	while True:
		print "In which context is '%s' used? Please choose from the list." % word
		for ctxt in context_list:
			print "> %s" % ctxt
		user_input = raw_input()
		
		if user_input in context_list:
				do_add_definition(word)
		else:
			device(word)

def project_leader(word):
	
	print "Has your project leader authorized '%s'?" % word
	leader = raw_input()
	while True:
		
			if leader == "yes":
				device(word) # summary.append(project_leader)
			elif leader == "no":
				print "Please have '%s' authorized by your project leader." % word
				exit()
			else: 
				print "Please enter 'yes' or 'no':\n"
			project_leader(word)

def project(word):
	project_relation = raw_input()
		# summary.append(project_relation)
	while True:
		
			if project_relation == "yes":
				project_leader(word)
			elif project_relation == "no":
				device(word)
			else: 
				print "Please enter 'yes' or 'no'.\n"
			project(word)

def source_language(word):
	print "What is the source language of '%s'? Please choose from the list." % word
	for index, source_l in enumerate (source_language_list, start=1):
			print index, source_l
	
	chosen_language = raw_input()
		# summary.append(chosen_language)		
	if chosen_language == "2" or chosen_language == "3":
		print "Has legal protection confirmed '%s'?" % word
		legal_protection = raw_input()
		# summary.append(legal_protection)
		print "Is it allowed to have '%s' translated?" % word
		translation = raw_input()
		# summary.append(translation)
		project_leader(word)
		
	elif chosen_language == "1":
		print "Is '%s' related to an ongoing project?" % word
		project(word)
	
	else:
		return source_language()
		
def do_add_entry():
	print "Please enter the word."
	word = raw_input()
	return source_language(word)

def new_language():
	print "What language do you want to add?"
	analyze_entry()

def old_language():
	print "What language do you want to change?"
	analyze_entry()

def analyze_entry():
	for index, languages in enumerate (all_languages_list, start=1):
		print index, languages
		
	chosen_language = raw_input()
	
	if chosen_language in all_languages_list and chosen_language in some_languages_list:
		change()
			
	if chosen_language in some_languages and not chosen_language in all_languages_list:
		localize()
		
	exit()

def choose_change():
	print "What do you want to change about the entry?"
	for index, change in enumerate (change_list, start=1):
		print index, change
			
	chosen_change = raw_input()
	if chosen_change == "1":
			new_language()

	if chosen_change == "2":
			old_language()

	exit()


def do_modify_entry():
	print "Please choose the entry number you want to modify."
	chosen_entry = raw_input()
	
	for entry in entry_dict:
		if chosen_entry in entry_dict:
			choose_change()
			break
		else:
			print "It's not in the list."
			do_modify_entry()
			break
	
	exit()

# further ATTEMPTS: see description at the end of the script.



# def login_attempt():
	# print "Please enter your username"
	# user_input = raw_input()
	# for usr in user_list:
		# if usr = user_input:
			# g_logged_in = user_input
			# return True

	# return False


def start():

	continue_flag = True
	
	while continue_flag:
		# if g_logged_in = "":
			# successful_login = login_attempt()
			# if not successful_login:
				# exit()

		print "Please choose what you want to do:"
		for index, action in enumerate (action_list, start=1):
			print index, action
		
		chosen_action = raw_input()

		if chosen_action == "1":
				do_add_entry()

		if chosen_action == "2":
				do_modify_entry()

		if chosen_action == "3":
			continue_flag = False

	exit()

start()

#-------------------------------------------------------------------

# ATTEMPT 1:

# def find_entry(entry_list, entry_id):
	# for subVal in entry_list:
		# if entry_number in subVal:
			# return subVal[entry_number]
		# else:
			# return "Not found."
# entry_list[1] = find_entry
# while True:
	# print "Entry?(ENTER to quit)",
	# entry_number = raw_input()
	# if not entry_number: break
	
	# entry_found = entry_list[1](entry_list, entry_number)
	
	# print entry_found


# ATTEMPT 2: 

# def find_entry(thelist, entry_id):
	# if entry_id in thelist:
		# return thelist[entry_id]
	# else:
		# return "Not found."
# entry_list[''] = find_entry
# while True:
	# print "Entry?(ENTER to quit)",
	# entry_id = raw_input()
	# if not entry_id: break
	# entry_found = entry_list['_find'](entry_list, entry_id)
	# print entry_found


# ATTEMPT 3:

# sorted_entries_1 = sorted(entry_list, key=itemgetter('entry_id'), reverse=True)
# print sorted_entries_1


# ATTEMPT 4:

# sorted_entries = sorted(' '.items(), key=operator.itemgetter(0))
# print sorted_entries


# ATTEMPT 5:

# temp = {}
# def find_entry():
	# print "Please choose the entry number you want to modify."
	# chosen_entry = raw_input('>')
	# for chosen_entry in entry_list:
		# temp[chosen_entry['entry_id']] = temp.get(chosen_entry['entry_id'], 0) #int(chosen_entry['entry_id'])
		# if chosen_entry['id'] not in temp:
			# temp[chosen_entry['id']] = {}
		# temp_ce = temp[chosen_entry['id']]
		# temp_ce['entry_id'] = temp_ce.get('entry_id', 0) + int(chosen_entry['entry_id'])


# ATTEMPT 6:

# def find_entry(entry_list):
	# print "Please choose the entry number you want to modify."
	# chosen_entry = raw_input('>')
	# result = {}
	# for chosen_entry in entry_list:
		# resItem = result.get(chosen_entry['entry_id'], None)
		# choose_change()
		# if not resItem:
			# print "This is not in the list."
			# find_entry(entry_list)


# ATTEMPT 7:

# def find_entry(entry_list):
	# print "Please choose the entry number you want to modify."
	# chosen_entry = raw_input('>')
	# bar = {
		# k: [chosen_entry.get(k) for chosen_entry in entry_list]
		# for k in set().union(*entry_list)
		# }


# ATTEMPT 8:

# listOfDicts = [{'1': 'one', '3': 'three', '2': 'two', '5': 'five', '4': 'four'}]
# d = {'1': 'one', '3': 'three', '2': 'two', '5': 'five', '4': 'four'}

# def get_value(listOfDicts, key):
    # for subVal in listOfDicts:
        # if key in subVal:
            # return subVal[key]
# print "Choose a value."
# chosen_value = raw_input()
# get_value()


# ATTEMPT 9:

# test_list = [1, 2, 3, 4, 5]
# test_list = set(test_list)

# def entry_find():
	# print "Enter the entry number."
	# number = raw_input()
	# if number in test_list:
		# print "Exists"
	# else:
		# print "Good night."		
# entry_find()


# ATTEMPT 10:

# import operator
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_x = sorted(x.items(), key=operator.itemgetter(1))
# print sorted_x


# ATTEMPT 11:

# def do_modify_entry():

	# while True:
		# print "Please enter the entry number of the glossary entry you want to modify."
		# entry_number = raw_input()
		# if entry_number in entry_list:
				# change()
		# else:
			# do_modify_entry()


# ATTEMPT 12: 

# def do_modify_entry():
	# print "Please choose the entry number you want to modify."
	# for entry in (entry_list):
			# print entry
	# user_input = raw_input()
	# for i in range (1, 5):
		# if i = user_input:
			# entry_number = user_input
			# return True			
	# return False
# do_modify_entry()


# ATTEMPT 13:

# def do_modify_entry_2():
	# print "Please enter the entry number of the glossary entry you want to modify."
	# user_input = raw_input()
	# for i in range (1, 5):
		# if i == user_input:
			# print change()
		# else:
			# print do_modify_entry_2()
	# exit()


# ATTEMPT 14:

# def entry_attempt_1():
	# print "Please enter the entry number of the glossary entry you want to modify."
	# user_input = raw_input()
	# for i in range (1, 5):
		# if i == user_input:
			# entry_number = user_input
			# return True			
	# return False

# def do_modify_entry_3():	
	# while True:
		# if entry_number == "":
			# successful_entry = entry_attempt_1
			# if not successful_entry:
				# exit()		
		# change()
	# exit()
	

# ATTEMPT 15:

# def find_entry():
	# new_list = sorted(entry_list, key=lambda k:k['entry_id'])
	

# ATTEMPT 16:

# from operator import itemgetter
# import operator

# all_keys = set().union(*(d.keys() for d in entry_list))
# only_entry_id = all_keys.pop()

# newlist = sorted(entry_list, key=lambda k: k['entry_id'])
# new_list = entry_list.sort(key=operator.itemgetter('entry_id'))
# absolut = entry_list.sort(lambda x,y : cmp(x['entry_id'], y['entry_id']))

# print only_entry_id


# ATTEMPT 17:

# dict = {'Name': 'Valerie', 'Age': '34'}
# print "Value: %s" % dict.keys()


# ATTEMPT 18:

# def do_modify_entry():
	# print "Please enter the entry number:"
	# target = raw_input()
	# for i, value in enumerate (entry_list):
		# if value == target:
			# return i

	# return False
	
#-------------------------------------------------------------------