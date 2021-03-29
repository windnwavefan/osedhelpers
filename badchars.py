# given a location in memory prints missing values from all possible byte values

import sys, argparse
from pykd import loadBytes

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--offset', help="memory offset to search from")
parser.add_argument('-d', '--discard', nargs='*', help="bytes to discard")
args = parser.parse_args()

offset = int(args.offset, 16)
omitted = [int(x, 16) for x in args.discard]

print("omitting: {}".format([hex(b) for b in omitted]))

# create a byte array
refArray = [x for x in range(256)]

# remove the omitted bytes
for b in omitted:
    refArray.remove(b)

print("reading {} bytes from offset {}".format(len(refArray), hex(offset)))

# compare to the memory offset given
memoryDump = loadBytes(offset, len(refArray), False)

for x in range(len(refArray)):
    if refArray[x] != memoryDump[x]:
        print("unable to find {} in memory!".format(hex(refArray[x])))
        break
    
#print(memoryDump)


