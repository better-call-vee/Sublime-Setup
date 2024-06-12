import sublime
import sublime_plugin


class FormatWholeDocumentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Save the current cursor positions
        original_positions = [region for region in self.view.sel()]

        # Select the entire document
        all_content = sublime.Region(0, self.view.size())
        self.view.sel().clear()
        self.view.sel().add(all_content)

        # Call ClangFormat
        self.view.run_command("clang_format")

        # Restore the original cursor positions
        self.view.sel().clear()
        for region in original_positions:
            self.view.sel().add(region)
