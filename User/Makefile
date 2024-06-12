CXX = C:\winlibs-x86_64-mcf-seh-gcc-13.2.0-llvm-16.0.6-mingw-w64ucrt-11.0.1-r2\mingw64\bin\g++
CXXFLAGS = -std=c++20

# List all source files here
SRC = main.cpp
# Generate object files from source files
OBJ = $(SRC:.cpp=.o)
# Name of the executable
EXE = main.exe

# The default target
all: $(EXE)

# Link the object files to create the executable
$(EXE): $(OBJ)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Compile each source file to an object file
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $<

# Clean up the build files
clean:
	del /Q *.o *.exe

run: all
	$(EXE)
