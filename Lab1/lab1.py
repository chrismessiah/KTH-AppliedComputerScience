# Author: Christian Abdelmassih, Alexandra Runhem



import time

# Inoke to create instances of a location with all corresponding data to that location.
# Will be called for each location once.
class GeoData(object):
	def __init__(self, name, description, latitud_coordinates, longitud_coordinates, up_date):
		self.name = name
		self.description = description
		self.latitud_coordinates = latitud_coordinates
		self.longitud_coordinates = longitud_coordinates
		self.up_date = up_date

	def  __str__(self): # Invoked by print(object-name)
		return("Namn: " + self.name + "\nBeskrivning: " + self.description + "\nLatitud: " + self.latitud_coordinates + "\nLongitud: " + self.longitud_coordinates + "\nUppdateringsdatum: " + self.up_date + "\n")

# Creates an instance of all operations available to process locations.
class GeoOperation(object):
	def __init__(self):
		self.geo_list = None # Used to store the location-data as a object list
		self.f_geo_list = None # Used by get_extreme_coordinates to store the filtered locations
		self.extreme_value = None # Used by get_extreme_coordinates to store the corresponding extreme-location value
		self.file_reader() # gets "self.geo_list"

	# Reads chosen textfile, creates a object-list of all locations in chosen textfile.
	def file_reader(self):
		#file_name = "geodataSW.txt"
		file_name = "geodataCH.txt"

		f = open(file_name,"r",encoding="utf-8")
		total_paragraphs = int((len(f.readlines())-1)/6)
		f.close()

		f = open(file_name,"r",encoding="utf-8")
		for i in range(0,6):
			f.readline()

		# Creation of location-object list
		self.geo_list = []
		for i in range(0,total_paragraphs):
			paragraph = [f.readline().replace("\n",""), f.readline().replace("\n",""), f.readline().replace("\n",""), f.readline().replace("\n",""), f.readline().replace("\n","")] #[name, description, lat-cord, long-cord, update]
			f.readline()
			self.geo_list.append(GeoData(paragraph[0], paragraph[1], paragraph[2], paragraph[3], paragraph[4])) #

	# Creating a new list filtered from "geo_list" based on parameter "list_type"
	def list_extractor(self, list_type):
		new_list = []
		for obj in self.geo_list:
			if list_type == "name":
				new_list.append(obj.name)
			elif list_type == "description":
				new_list.append(obj.description)
			elif list_type == "latitud":
				new_list.append(int(obj.latitud_coordinates))
			elif list_type == "longitud":
				new_list.append(int(obj.longitud_coordinates))
			elif list_type == "up_date":
				new_list.append(obj.up_date)
		return new_list

	# Creates a filtered object-list depending on "direction" e.g. north, west, south etc.
	def get_extreme_coordinates(self, direction):
		self.f_geo_list = []
		if direction == "Ö" or direction == "V":
			coordinate_list = self.list_extractor("longitud")
			self.get_extreme_value(coordinate_list, direction)
			for obj in self.geo_list:
				if int(obj.longitud_coordinates) == self.extreme_value:
					self.f_geo_list.append(obj)

		elif direction == "N" or direction == "S":
			coordinate_list = self.list_extractor("latitud")
			self.get_extreme_value(coordinate_list, direction)
			for obj in self.geo_list:
				if int(obj.latitud_coordinates) == self.extreme_value:
					self.f_geo_list.append(obj)

	# gets extremevalue of corresponding direction
	def get_extreme_value(self, data_list, direction):
		if direction == "S" or direction == "V":
			self.extreme_value = min(data_list)
		elif direction == "N" or direction == "Ö":
			self.extreme_value = max(data_list)

def menu(geo_box):
	usr_input = input("\nVälj alternativ genom att mata in respektive index\n\n1. Sök på platsers namn\n2. Sök efter tillhörande beskrivning\n3. Sök genom inmatning av koordinater\n4. Sök på uppdateringsdatum\n5. Sök efter valfri extremplats(dvs sydligaste, nordligaste etc.)\nVal: ")

	if usr_input == "1":
		usr_input_2 = input("Mata in namnet på den plats du söker: ")
		start_time = timer("start")
		print_location(geo_box.geo_list, "name", usr_input=usr_input_2)
		timer("stop",start_time=start_time)

	elif usr_input == "2":
		usr_input_2 = input("Mata in tillhörande beskrivning på platsen du söker: ")
		start_time = timer("start")
		print_location(geo_box.geo_list, "description", usr_input=usr_input_2)
		timer("stop",start_time=start_time)


	elif usr_input == "3":
		usr_input_2 = input("Vill du söka på 'latitud', 'longitud' eller 'båda': ")
		usr_input_2 = usr_input_2.upper()

		if usr_input_2 == "LATITUD":
			lat_cord = input("Mata in latitud-koordinaterna på den plats du söker med enbart siffor enligt GGMMSS: ")

			start_time = timer("start")
			print_location(geo_box.geo_list, "latitud", usr_input=lat_cord)
			timer("stop",start_time=start_time)

		elif usr_input_2 == "LONGITUD":
			long_cord = input("Mata in longitud-koordinaterna på den plats du söker med enbart siffor enligt GGMMSS: ")

			start_time = timer("start")
			print_location(geo_box.geo_list, "longitud", usr_input=long_cord)
			timer("stop",start_time=start_time)

		elif usr_input_2 == "BÅDA":
			lat_cord = input("Mata in latitud-koordinaterna på den plats du söker med enbart siffor enligt GGMMSS: ")
			long_cord = input("Mata in longitud-koordinaterna på den plats du söker med enbart siffor enligt GGMMSS: ")

			start_time = timer("start")
			print_location(geo_box.geo_list, "C-both", usr_input=lat_cord, usr_input_2=long_cord)
			timer("stop",start_time=start_time)

		else:
			print("Var god följ instruktionerna!")

	elif usr_input == "4":
		usr_input_2 = input("Mata in uppdateringsdatumet enligt YYYY-MM-DD: ")
		start_time = timer("start")
		print_location(geo_box.geo_list, "up_date", usr_input=usr_input_2)
		timer("stop",start_time=start_time)

	elif usr_input == "5":
			direction = input("I vilken riktning sökes extremplatsen? Nord, Syd, Öst eller Väst: ")

			f_direction = direction[0].upper()
			if f_direction == "Ö" or f_direction == "V" or f_direction == "N" or f_direction == "S":
				start_time = timer("start")
				geo_box.get_extreme_coordinates(f_direction)
				print_extreme_location(geo_box.f_geo_list, f_direction)
				timer("stop",start_time=start_time)
			else:
				print("Var god mata in enbart Öst, Väst, Nord, eller Syd")

	else:
		print("Vad god och följ instruktionerna")


# Prints extreme locations
def print_extreme_location(filtered_list, to_get_location):
	print("\nPå koordinaterna " + filtered_list[0].latitud_coordinates[:2] + "°" + filtered_list[0].latitud_coordinates[2:4] + "'" + filtered_list[0].latitud_coordinates[4:] + "”N " + filtered_list[0].longitud_coordinates[:2] + "°" + filtered_list[0].longitud_coordinates[2:4] + "'" + filtered_list[0].longitud_coordinates[4:] + "”E" + " hittar vi: \n")
	for obj in filtered_list:
		print(obj)

# Timer with two modes. prints at stop.
def timer(mode, start_time=0, prnt_str="Körtid: "):
	if mode == "start":
		return time.time()
	elif mode == "stop":
		print(prnt_str + str(round(time.time() - start_time,2)) + " sekunder")

# Prints locations based on "search_type" and "usr_input" (and "usr_input_2" for both latitud and longitud cord.)
def print_location(geo, search_type, usr_input = None, usr_input_2 = None):
	found_location = False
	print("")
	for obj in geo:
		if (search_type == "name" and obj.name == usr_input) or (search_type == "description" and obj.description == usr_input) or (search_type == "latitud" and obj.latitud_coordinates == usr_input) or (search_type == "longitud" and obj.longitud_coordinates == usr_input) or (search_type == "up_date" and obj.up_date == usr_input):
			found_location = True
			print(obj)
		elif search_type == "C-both" and usr_input == obj.latitud_coordinates and usr_input_2 == obj.longitud_coordinates:
			found_location = True
			print(obj)
	if found_location == False:
		print("Hittade ingen plats med det angivna kriteriet.\n")

def main():
	print("Ett ögonblick, programmet förberds.")
	start_time = timer("start")
	geo_box = GeoOperation()
	timer("stop", start_time=start_time, prnt_str="Tid för inläsning av textfil: ")
	while True:
		menu(geo_box)
main()
