import sublime
import sublime_plugin
import re

class DeleteBlockCommand(sublime_plugin.TextCommand):
    def run(self, edit, block_text=""):
        # Escape special characters in the block text for regex
        escaped_block_text = re.escape(block_text)
        
        # Create a regex pattern that matches the block text and possibly surrounding newline characters
        pattern = r'(\n)?' + escaped_block_text + r'(\n)?'
        
        # Find all occurrences of the block text
        occurrences = self.view.find_all(pattern, sublime.IGNORECASE)
        
        # Delete each occurrence from last to first (to maintain correct positions)
        for region in reversed(occurrences):
            # Check whether the matched region includes newline characters
            matched_text = self.view.substr(region)
            preceding_newline = matched_text.startswith('\n')
            following_newline = matched_text.endswith('\n')
            
            # Adjust the region to remove the correct newline character
            if following_newline and preceding_newline:
                region = sublime.Region(region.begin() + 1, region.end())
            elif not following_newline and not preceding_newline:
                # If there are no newline characters around the block,
                # insert a newline character after the block
                self.view.insert(edit, region.end(), "\n")
            
            # Erase the adjusted region
            self.view.erase(edit, region)
