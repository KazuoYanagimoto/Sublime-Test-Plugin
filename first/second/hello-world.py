import sublime, sublime_plugin

# command
# hello_world

class HelloWorldCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")
