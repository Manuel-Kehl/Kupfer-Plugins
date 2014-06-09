__kupfer_name__ = _("Make New Directory")
__kupfer_sources__ = ()
__kupfer_text_sources__ = ()
__kupfer_actions__ = ("MakeDirectory", )
__description__ = _("A plugin fo creating a new directory with a given name.")
__version__ = "1.0"
__author__ = "Manuel Kehl"

import gio
import os.path
from kupfer.objects import Action, FileLeaf, TextLeaf

class MakeDirectory (Action):
	def __init__(self):
		Action.__init__(self, _("Make a new directory..."))
	      
	def item_types(self):
		yield FileLeaf
		
	def valid_for_item(self, item):
		return os.path.isdir(item.object)
		
	def object_types(self):
		yield TextLeaf
		
	def requires_object(self):
		return True
		
	def get_description(self):
		return _("Make a new directory...")
	      
	def get_icon_name(self):
		return "folder-new"

	def activate(self, parent_dir, new_dir_name):
		path_to_new_dir = os.path.join(parent_dir.object, new_dir_name.object)
		new_dir = gio.File(path_to_new_dir)
		new_dir.make_directory()