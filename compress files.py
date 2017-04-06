#! /usr/bin/python3


import os, os.path
join = os.path.join

dirs_with_css = ('./theme/css', )
dirs_with_js = ('./theme/js', )
dirs_with_html = ('./', )


def compress(file_addr):
	"""Compresses input file: removes it's tabs and \\n."""
	with open(file_addr, 'tr') as tmp_file:
		text = tmp_file.read()
	text = text.replace('\n', '')
	text = text.replace('\t', '')
	with open(file_addr, 'tw') as tmp_file:
		tmp_file.write(text)


def receive_files():
	cur_dir = os.path.dirname(__file__)
	
	all_dirs = dirs_with_css + dirs_with_js + dirs_with_html
	all_dirs = [join(cur_dir, x1) for x1 in all_dirs]
	all_files = []
	
	for direct in all_dirs:
		files = [join(direct, x2) for x2 in os.listdir(direct)]
		all_files.extend(files)
	
	all_files = [x1 for x1 in all_files if (x1.endswith('.css')) or (x1.endswith('.html')) or (x1.endswith('.js'))]
	
	print('all_files:')
	for x1 in all_files:
		print(x1)
	
	return all_files


file_list = receive_files()
for x in file_list:
	compress(x)

print()
print("All operations done.")
