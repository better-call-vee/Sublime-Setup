import sublime
import sublime_plugin

class ExitCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        sublime.active_window().run_command('exit')
