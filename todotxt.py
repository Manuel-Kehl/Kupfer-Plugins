__kupfer_name__ = _("Todo.txt")
__kupfer_sources__ = ()
__kupfer_text_sources__ = ()
__kupfer_actions__ = ("AddTask", )
__description__ = _("A plugin to integrate Gina Trapani's Todo.txt into Kupfer")
__version__ = "1.0"
__author__ = "Manuel Kehl"

import gio
from kupfer.objects import Action, TextLeaf
from kupfer import plugin_support


__kupfer_settings__ = plugin_support.PluginSettings(
    {
        "key" : "path_to_file",
        "label": _("Path to your Todo.txt"),
        "type": str,
        "value": "",
    },
)

class AddTask (Action):
	def __init__(self):
		Action.__init__(self, _("Add to Todo.txt"))
	      
	def item_types(self):
		yield TextLeaf
		
	def get_description(self):
		return _("Adds a task to your Todo.txt file")
	      
	def get_icon_name(self):
		return "list-add"

	def activate(self, text):
		file = gio.File(__kupfer_settings__["path_to_file"])
		stream = file.append_to()
		stream.write(text.object)
		stream.close