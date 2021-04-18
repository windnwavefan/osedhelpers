# given a location in memory prints missing values from all possible byte values

import sys, argparse
import pykd

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--offset', help="memory offset to search from")
parser.add_argument('-d', '--discard', nargs='*', help="bytes to discard")
args = parser.parse_args()

if len(sys.argv) < 2:
    parser.print_help()
    exit(0)

addr = int(args.offset, 16)
omitted = [int(x, 16) for x in args.discard]

print("omitting: {}".format([b for b in args.discard]))

refArray = bytearray(range(256))

# remove the omitted bytes
for b in omitted:
    refArray.remove(b)

print("comparing bytes from offset {}".format(hex(addr)))

for x in range(len(refArray)):
    if pykd.isValid(pykd.ptrByte(addr + x)):
        if pykd.ptrByte(addr + x) != refArray[x]:
            print("unable to find {} in memory!".format(hex(refArray[x])))
            exit(0)
    else:
        print("address {} is not a valid memory address!".format(hex(addr + x)))
        exit(0)

print("found all bytes in memory!")
        

