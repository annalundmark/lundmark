import os
import argparse
import sys

def main():
	indata = check_indata()
	repo_dir(indata.path)

def check_indata(): 
	argparser = argparse.ArgumentParser(description='TEST', formatter_class=argparse.RawTextHelpFormatter,)
	argparser.add_argument('-p',dest='path',metavar='PATH',type=str,required=True,default='.',help='Path to check (default is ".").')
	indata = argparser.parse_args()
	return indata

class repo_dir(object): 
	def __init__(self, path): 
		self.original_path = os.getcwd()
		self.path = path
		
	def __enter__(self): 
		os.chdir(self.path)

	def __exit__(self, type, value, traceback): 
		os.chdir(self.original_path)

class CourseRepo(object): 
	def __init__(self, lastname): 
		self.lastname = lastname
		self.required = [".git", "setup.py", "README.md", "scripts/check_repo.py", self.lastname + "/__init__.py", self.lastname + "/session3.py"]
	
	def check(self): 
		output="PASS"
		for path in self.required: 
			if not os.path.exists(path): 
				output="FAIL"
		return output
				
	def __enter__(self):
		pass
    
	def __exit__(self, type, value, traceback):
		pass
    
	@property
	def surname(self): 
		return self.lastname
    
	@surname.setter
	def surname(self, name): 
		self.surname = name
		self.required[-2] = self.lastname+'/__init__.py'
		self.required[-1] = self.lastname+'/session3.py'
        
if __name__ == "__main__":
	main()