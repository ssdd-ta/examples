#!/usr/bin/python3

import sys
import Ice
Ice.loadSlice('Calculator.ice')
import Example


class CalculatorI(Example.Calculator):
    n = 0

    def add(self, a, b, current=None):
        res = a + b
        print(f'{n}: {a}+{b}={res}')
        sys.stdout.flush()
        self.n += 1


class Server(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        servant = CalculatorI()

        adapter = broker.createObjectAdapter("CalculatorAdapter")
        proxy = adapter.add(servant, broker.stringToIdentity("calculator1"))

        print(proxy)
        sys.stdout.flush()

        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0


server = Server()
sys.exit(server.main(sys.argv))
