import os

name = "Nidhish"
# Function to rename multiple files
def rename1():
	i = 1
	path=f"Preprocessed Data/{name}/"
	for filename in os.listdir(path):
		my_dest =f"1user.{str(name)}.{str(i)}.jpg"
		my_source =path + filename
		my_dest =path + my_dest
		# rename() function will rename all the files
		os.rename(my_source, my_dest)
		i += 1

def rename2():
	i = 1
	path=f"Preprocessed Data/{name}/"
	for filename in os.listdir(path):
		my_dest =f"user.{str(name)}.{str(i)}.jpg"
		my_source =path + filename
		my_dest =path + my_dest
		# rename() function will rename all the files
		os.rename(my_source, my_dest)
		i += 1

rename1()
rename2()