#! /usr/bin/python3


import os, os.path
import shutil
join = os.path.join



def remove_previous_files():
	"""Removes previous files.
	"""
	exceptions = ['.hg', 'update files.py', 'commit and export.py', 'compress files.py']
	print("Are you sure? All files will be removed, except:")
	print(exceptions)
	input()
	print("Are you sure?")
	input()
	
	cur_dir = os.path.dirname(__file__)
	files_list = os.listdir(cur_dir)
	
	files_to_remove = set(files_list).difference(set(exceptions))
	print("Files to remove:")
	print(files_to_remove)
	
	for cur_file in files_list:
		file_addr = join(cur_dir, cur_file)
		
		if cur_file not in exceptions:
			if os.path.isfile(file_addr):
				os.remove(file_addr)
			elif os.path.isdir(file_addr):
				shutil.rmtree(file_addr)
				
	print("All files removed.")


def copy_files(source_dir="/home/vlad/Programs/my_projects/web/technics_repair_service/output"):
	"""Copies files from source directory to directory with this file.
	"""
	target_dir = os.path.dirname(__file__)
	files_to_copy = os.listdir(source_dir)
	
	print("Files to copy:")
	print(files_to_copy)
	
	for cur_file in files_to_copy:
		cur_addr = join(source_dir, cur_file)
		
		if os.path.isfile(cur_addr):
			shutil.copy2(cur_addr, target_dir)
		elif os.path.isdir(cur_addr):
			shutil.copytree(cur_addr, join(target_dir, cur_file))
	
	print("All files copied.")


remove_previous_files()
copy_files()
