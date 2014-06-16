__kupfer_name__ = _("Parent Directory")
__kupfer_sources__ = ()
__kupfer_text_sources__ = ()
__kupfer_actions__ = ("OpenParentDirectory", )
__description__ = _("A plugin for opening the parent directory of the active file.")
__version__ = "1.0"
__author__ = "Manuel Kehl"

import os.path
import os
from kupfer.objects import Action, FileLeaf

class OpenParentDirectory (Action):
	def __init__(self):
		Action.__init__(self, _("Open parent directory"))
	      
	def item_types(self):
		yield FileLeaf
		
	def valid_for_item(self, item):
		return True
	
	def get_description(self):
		return _("Open the directory which contains the active file")
	      
	def get_icon_name(self):
		return "folder-open" 

	def activate(self, recent_file):
		path_to_parent = os.path.abspath(os.path.join(recent_file.object, os.pardir))
		# xdg-open for opening files in a portable and standard compliant manner
		os.system('xdg-open ' + path_to_parent)