import sublime
import sublime_plugin
import subprocess
import os
import re

class InsertExecutionTimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Get the current file path
        file_path = self.view.file_name()
        if not file_path or not file_path.endswith(('.cpp', '.cxx', '.cc')):
            sublime.error_message("Not a valid C++ file!")
            return

        # Backup the original content
        original_content = self.view.substr(sublime.Region(0, self.view.size()))

        # Add the timing code to the program
        timing_code_start = """
#include <ctime>
clock_t start_time, end_time;
start_time = clock();
"""
        timing_code_end = """
end_time = clock();
double execution_time = double(end_time - start_time) / double(CLOCKS_PER_SEC);
cout << "// Execution time: " << execution_time << " seconds" << endl;
"""

        self.view.insert(edit, 0, timing_code_start)
        self.view.insert(edit, self.view.size(), timing_code_end)

        # Save the modified file
        self.view.run_command("save")

        # Compile the code
        compiled_name = os.path.splitext(file_path)[0]
        compile_command = ["g++", "-std=c++17", file_path, "-o", compiled_name]
        try:
            subprocess.check_call(compile_command, stderr=subprocess.STDOUT, timeout=60)
        except subprocess.CalledProcessError:
            sublime.error_message("Compilation failed!")
            return

        # Execute the program to get the execution time
        try:
            result = subprocess.check_output(compiled_name, stderr=subprocess.STDOUT, timeout=60).decode('utf-8')
            execution_time = re.search(r"// Execution time: (.+?) seconds", result).group(1)
        except (subprocess.CalledProcessError, AttributeError):
            sublime.error_message("Execution failed or could not extract the timing!")
            return

        # Restore the original content and insert the execution time at the cursor position
        self.view.replace(edit, sublime.Region(0, self.view.size()), original_content)
        for region in self.view.sel():
            self.view.insert(edit, region.end(), f"\n// Execution time: {execution_time} seconds\n")
