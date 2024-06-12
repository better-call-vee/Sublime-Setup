import sublime
import sublime_plugin

class SelectLinesCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Enter line range (x,y):", "", self.on_done, None, None)

    def on_done(self, text):
        try:
            x, y = map(int, text.split(','))
            view = self.window.active_view()
            if view:
                # Adjusting line numbers to be 0-based
                x_point = view.text_point(x - 1, 0)
                y_point = view.text_point(y - 1, 0)

                # Selecting from the start of the x line to the end of the y line
                y_line_end = view.full_line(y_point).b

                view.sel().clear()
                view.sel().add(sublime.Region(x_point, y_line_end))
                view.show_at_center(sublime.Region(x_point, y_line_end))
        except ValueError:
            sublime.error_message("Invalid line range. Please enter in format x,y")
        except Exception as e:
            sublime.error_message("Error: " + str(e))
