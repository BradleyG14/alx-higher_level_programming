#!/usr/bin/python3
if __name__ == "__main__":
    form sys import argv, exit
    import calculator_1
    main(argv)

    def main(argv):
        argc = len(argv)
        ops = {
                "+": calculator_1.add,
                "-": calculator_1.sub,
                "*":calculator_1.mul,
                "/":calculator_1.div,
                }
        if argc != 4:
            print("usage: {:s} <a> <operator> <b>".format(argv[0]))
            exit(1)

            a = int(argv[1])
            b = int(argv[3])
            op = argv[2]
            
            if op not in "+-*/":
                print("unkown operator. Available operators: +, -, * and /")
                exit(1)

            res = ops[op](a, b)
            print("{:d} {:s} {:d}".format(a, op, b, res))
