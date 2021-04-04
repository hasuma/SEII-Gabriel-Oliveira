CXX := g++
CXXFLAGS := 
CPPFLAGS = 

CPPSRCS += tcp_client.cpp tcp_server.cpp
OBJS += src/tcp_client.o src/tcp_server.o

HEADERS += -I ./include
HEADERS_CPP += 
INCLUDES:=  $(HEADERS) $(HEADERS_CPP)

LIBRARIES := -pthread
EXECUTABLE +=	

BIN := bin
SRC := src

MD := mkdir -p


all:	directories bin/client bin/server

directories:
	@echo "Building Directories if not exist..."
	@$(MD) $(BIN)
	@$(MD) $(SRC)
	@echo 'Finished building directories'
	@echo ''
	
bin/client:	src/tcp_client.o
	@echo "Building Executable..."
	@$(CXX) $(CXXFLAGS) -o $@ $< $(LIBRARIES)
	@echo 'Finished building target: $@'
	@echo ''
		
src/tcp_client.o: tcp_client.cpp
	@echo 'Building Object: $@'
	@$(CXX) $(CXXFLAGS) -o $@ -c $< #$(INCLUDES)
	@echo 'Finished building: $@'
	@echo ''
	
bin/server:	src/tcp_server.o
	@echo "Building Executable..."
	@$(CXX) $(CXXFLAGS) -o $@ $< $(LIBRARIES)
	@echo 'Finished building target: $@'
	@echo ''
		
src/tcp_server.o: tcp_server.cpp
	@echo 'Building Object: $@'
	@$(CXX) $(CXXFLAGS) -o $@ -c $< #$(INCLUDES)
	@echo 'Finished building: $@'
	@echo ''	
clean:
	@echo "Clearing..."
	@rm -rf $(OBJS)
	@rm -rf $(EXECUTABLE)
