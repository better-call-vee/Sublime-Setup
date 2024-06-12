import sublime
import sublime_plugin

class InsertAfterMainCommand(sublime_plugin.TextCommand):
    def run(self, edit, block_text=""):
        # Search for the 'main() {' pattern in the view
        main_region = self.view.find(r'main\(\) \{', 0)
        
        # If 'main() {' is found
        if main_region:
            # Find the line containing 'main() {'
            main_line = self.view.line(main_region)
            
            # Find the position to insert the block text
            # We insert the text just after the 'main() {' line
            insert_pos = main_line.end() + 1
            
            # Add a newline character before and after the block text
            # to ensure it is inserted in a new line and followed by a new line
            block_text = '\n' + block_text + '\n'
            
            # Insert the block text at the calculated position
            self.view.insert(edit, insert_pos, block_text)
