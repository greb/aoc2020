class Console:
    def __init__(self, code):
        self.code = [Console.decode(op) for op in code.splitlines()]
        self.reset()

    def reset(self):
        self.acc = 0
        self.pc = 0

    def step(self):
        opcode, arg = self.code[self.pc]

        if opcode == 'acc':
            self.acc += arg
            self.pc += 1

        elif opcode == 'jmp':
            self.pc += arg

        elif opcode == 'nop':
            self.pc += 1

        else:
            raise Exception('Invalid opcode')

    def toggle_opcode(self, addr):
        opcode, arg = self.code[addr]
        if opcode == 'nop':
            self.code[addr] = ('jmp', arg)
        elif opcode == 'jmp':
            self.code[addr] = ('nop', arg)
        else:
            return False

        return True

    @staticmethod
    def decode(op):
        opcode, arg = op.split()
        return opcode, int(arg)


def part1(inp):
    console = Console(inp)

    trace = []
    while True:
        if console.pc in trace:
            return console.acc

        trace.append(console.pc)
        console.step()


def part2(inp):
    console = Console(inp)

    for addr in range(len(console.code)):
        if not console.toggle_opcode(addr):
            continue
        console.reset()

        trace = []
        while True:
            if console.pc in trace:
                # Loop detected
                break

            trace.append(console.pc)
            console.step()
            if console.pc >= len(console.code):
                return console.acc

        # Change code back to original state
        console.toggle_opcode(addr)
