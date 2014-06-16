Kupfer Plugins
==============

A place for collecting and publishing plugins that I have written for the super convenient "Kupfer" command launcher.
To install a plugin just copy the corresponding py file into `~/.local/share/kupfer/plugins/` and activate it in Kupfer's preferences.

File to Clipboard
-----------------

A plugin for copying a file's path or content to the clipboard from within Kupfer.
It depends on the [pyperclip](http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/)
python module for accessing the user's clipboard.

If you have [pip](https://pip.pypa.io/en/latest/) installed you can get the dependency
by executing `pip install pyperclip`.

Make new Directory
------------------

A plugin for creating a directory within the currently selected directory.

Parent Directory
----------------

A plugin for opening the directory containing the active file in your system's default filechooser. 
It may be necessary to install [xdg-open](http://portland.freedesktop.org/xdg-utils-1.0/xdg-open.html), if you have not done so before.
On Debian based systems it is contained in the package `xdg-utils`.
