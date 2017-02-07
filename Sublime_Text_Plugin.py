import sublime, sublime_plugin
import os,sys
import urllib
import urllib.request
# import requests
import math,json

class RunCompileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		RUN_URL = "http://api.hackerearth.com/code/run/"
		CLIENT_SECRET = "cac1db5448cc656abf0470f436d47f3e5d8d45c0"

		f = self.view.file_name()
		file = os.path.split(self.view.file_name())
		
		lang=""
		for x in str(file[1][::-1]):
			if x!=".":
				lang = x + lang
			else:
				break
		lang = "." + lang
		if lang == ".py":
			language = "python"
		elif lang == ".c":
			language = "c_cpp"
		elif lang == ".cpp":
			language = "c_cpp"
		elif lang == ".js":
			language = "javascript"

		with open(f,'r+') as f:
			source_code = f.read()
		print(source_code)
		# self.view.run('run_compile')
		with open("/home/shashank/Desktop/input.txt",'r') as input_file:
			args = input_file.read()
		language = language.upper()
		data = {
			'client_secret': CLIENT_SECRET,
			'async': 0,
			'source': source_code,
			'lang': language,
			'time_limit': 5,
			'memory_limit': 262144,
			'input':args,
		}
		# r = requests.post(RUN_URL,data=data)
		# print(r.json()['run_status'])
		data = urllib.parse.urlencode(data)
		data = data.encode()
		response = urllib.request.urlopen(RUN_URL,data)
		# response = json.loads(response)
		# print(response.read())
		response = (response.read().decode('utf-8'))
		# print(response)
		response = json.loads(response)
		# print(response)
		output = response['run_status']
		output = output['output_html']
		# output = BeautifulSoup(output)
		# output = output.a.string
		with open("/home/shashank/Desktop/output.txt",'w+') as f:
			f.write(output)
		print(output)