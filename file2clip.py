__kupfer_name__ = _("File to Clipboard")
__kupfer_sources__ = ()
__kupfer_text_sources__ = ()
__kupfer_actions__ = ("PathToClipboard", "ContentToClipboard")
__description__ = _("Copies a file's path or content to the clipboard.")
__version__ = "1.0"
__author__ = "Manuel Kehl"

import gio
import pyperclip
from kupfer.objects import Action, FileLeaf

class PathToClipboard (Action):
	def __init__(self):
		Action.__init__(self, _("Copy Path To clipboard"))
	      
	def item_types(self):
		yield FileLeaf
		
	def get_description(self):
		return _("Copy file's path to the clipboard.")
	      
	def get_icon_name(self):
		return "edit-copy"

	def activate(self, file_name):
		file = gio.File(file_name.object)
		path = file.get_path()
		pyperclip.copy(path)
		
class ContentToClipboard (Action):
	def __init__(self):
		Action.__init__(self, _("Copy Content To clipboard"))
	      
	def item_types(self):
		yield FileLeaf
		
	def get_description(self):
		return _("Copy file's content to the clipboard.")
	      
	def get_icon_name(self):
		return "edit-copy"

	def activate(self, file_name):
		file = gio.File(file_name.object)
		stream = file.read()
		content = stream.read()
		stream.close()
		pyperclip.copy(content)