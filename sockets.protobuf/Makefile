all: compile

compile:
	protoc --python_out=. door.proto

clean:
	$(RM) *_pb2* *~
	$(RM) -rf __pycache__
