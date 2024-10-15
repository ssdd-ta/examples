#

all: compile

compile:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello.proto

clean:
	$(RM) *~ hello_pb2*
	$(RM) -r __pycache__
