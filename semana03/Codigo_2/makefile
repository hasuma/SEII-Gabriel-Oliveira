CXX := g++
CXXFLAGS := 
CPPFLAGS = 

CPPSRCS += main.cpp
OBJS += src/main.o
HEADERS += 
INCLUDES:= -I ./include # -include $(HEADERS)

BIN := bin
SRC := src
INCLUDE := 


LIBRARIES := # -larmadillo -llapack -lblas
EXECUTABLE := bin/executavel

all:	$(EXECUTABLE)

# run:	
#	clear	
#	@echo "Executing..."
#	@./$(EXECUTABLE)

$(EXECUTABLE):	$(OBJS)
	@echo "Building Executable..."
	@$(CXX) $(CXXFLAGS) -o $@ $< $(LIBRARIES)
	@echo 'Finished building target: $@'
		
$(OBJS): $(CPPSRCS)
	@echo 'Building Object: $@'
	@$(CXX) $(CXXFLAGS) -o $@ -c $< $(INCLUDES)
	@echo 'Finished building: $@'
	@echo ''
	
clean:
	@echo "Clearing..."
	@rm -rf $(OBJS)
	@rm -rf $(EXECUTABLE)
