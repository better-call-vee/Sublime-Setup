import sublime
import sublime_plugin

# Global variable to keep track of the last selected build system
last_build_system_index = 0

class ToggleBuildSystemCommand(sublime_plugin.WindowCommand):
    def run(self):
        global last_build_system_index

        # Define your build systems
        build_systems = [
            "Packages/User/Cppbuild.sublime-build",
            "Packages/User/CppIO.sublime-build"
        ]

        # Toggle to the other build system
        last_build_system_index = (last_build_system_index + 1) % len(build_systems)

        # Set the new build system
        self.window.run_command("set_build_system", {"file": build_systems[last_build_system_index]})
