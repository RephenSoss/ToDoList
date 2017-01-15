
def show_help():
	print ('What should we pick up at the store?')
	print ("""
	Enter "DONE" to stop adding items.
	Enter "HELP" to stop adding items.
	Enter "SHOW" to stop adding items.
		""")
show_help()


def add_to_list(new_item):
	shop_list.append(new_item)
	print("Added {}. List now had {} items.".format(new_item,len(shop_list)))
	pass


# Make list
shop_list = []

# Print instructions on how to use the app
while True:
	# ask for new items
	new_item = raw_input('> ')
	# be able to quit the app
	if new_item == "DONE":
		break
	elif new_item == "HELP":
		show_help()
		continue
	elif new_item == "SHOW":
		shop_list()
		continue
	add_to_list(new_item)




def show_list():
# print out the list
	print ("Here is your list: ")
	for item in shop_list:
		print (item)




