all: compile

compile:
	protoc --python_out=. sensor.proto

clean:
	$(RM) *_pb2* *~
	$(RM) -rf __pycache__
