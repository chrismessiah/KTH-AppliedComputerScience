class Hashtabell(object):

	def __init__(self):
		self.d = {}
		
	def put(self, key, atom):
		if key in self.d.keys():
			print("BOOM")
		else:
			self.d[key] = atom
	
	def get(self,key):
		if key in self.d.keys():	
			return self.d[key]
		else:
			return None









