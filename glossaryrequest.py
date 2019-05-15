user_list = ['a', 'b', 'c', 'd']
all_languages_list = ['deCH', 'deDE', 'frCH', 'frFR', 'itCH', 'itIT', 'enGB', 'nlNL', 'ruRU', 'trTR', 'ukUA', 'zhCN', 'esES']
some_languages_list = ['deCH', 'frCH', 'itCH', 'enGB', 'nlNL', 'ruRU', 'trTR', 'ukUA', 'zhCN', 'esES']
change_list = ['source language', 'other language', 'add language']
#I used user_list and entry_number 
#in order to show what I wanted the programme to do.
#They should later be replaced by data from other sources.
#They should appear in the form of a drop down menu or any of the like.
#I need to figure out how to import external sources.

def new_term(): #def new_term() should also be used within def other_language().
	print "Enter the new term in the given language:"
	newterm = raw_input(">")

def source_language():
	print new_term

def other_language():#depending on whether the entry number belongs
	#to the all_languages_list or the some_languages_list,
	print "xyz and if then plus new_term"

def add_language():
	print "please choose again"#depending on whether the entry number belongs
	#to the all_languages_list or the some_languages_list,
	#the user will be given different kinds of additional language lists
	#that are not yet defined in this code.

def start ():
	print "Choose your user name from the following list:"
	for user in user_list:
		print "\t>%s" %user
	username = raw_input("?")

# I tried to force the user to actually choose an element from the list
# but I haven't figured out yet how to read all the elements first and then
# ask for action. I only know the read function from reading a file - 
# considering that I'll be using data from a different source here: 
# could I adapt the read function also to external sources?
	#if username != user: 
		#print start()
	#else:
	print "Choose your glossary entry from the following list:"
	entry_number = []
	for i in range (1, 5):#I'm not happy about having defined the top number.
	#The output should display all the entries, starting from 1.
		print "\t>%d" % i
		entry_number.append(i)
	glossary_entry = raw_input("?")

	print "Choose what needs to be changed about the glossary entry"
	for change in change_list:
		print "\t>%s" % change
	chosen_change = raw_input("?")

	if chosen_change == "source language":
		print source_language

	elif chosen_change == "other language":
		print other_language

	elif chosen_change == "add language":
		print add_language

	else:
		print "Please choose one of the given possibilites."
		chosen_change = raw_input("!")

start()