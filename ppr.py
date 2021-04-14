import pykd
import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--offset', help="memory offset to search from")
parser.add_argument('-l', '--length', help="length of memory to search")
args = parser.parse_args()

if len(sys.argv) < 2:
    parser.print_help()
    exit(0)

addr = args.offset
length = args.length

# generate a list of pop, pop, ret sequences
ppr = []
for p1 in range(0x58, 0x5f):
    for p2 in range(0x58, 0x5f):
        ppr.append([hex(p1), hex(p2), hex(0xc3)])

# search for each of the sequences starting at addr
for p in ppr:
    print("searching for: {}".format(" ".join(p)))
    print(pykd.dbgCommand("s -b {} l{} {}".format(addr, length, " ".join(p))))
