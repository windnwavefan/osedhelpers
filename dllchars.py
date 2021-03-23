# enumerates DllCharacteristics from the IMAGE_OPTIONAL_HEADER of all loaded modules

from pykd import *

mods = getModulesList()

dllchars = {
    "HIGH_ENTROPY_VA" : 0x20,
    "DYNAMIC_BASE" : 0x40,
    "FORCE_INTEGRITY" : 0x80,
    "NX_COMPAT" : 0x100,
    "NO_ISOLATION" : 0x200,
    "NO_SEH" : 0x400,
    "NO_BIND" : 0x800,
    "APPCONTAINER" : 0x1000,
    "WDM_DRIVER" : 0x2000,
    "GUARD_CF" : 0x4000,
    "TS_AWARE" : 0x8000
}

for mod in mods:
    baseAddr = hex(mod.begin())
    # parse the value for e_lfanew (long file address?)
    e_lfanew = dbgCommand("dw {}+0x3c l1".format(baseAddr)).split()[1]
    # parse the value for DllCharacteristics
    dllcharacteristics = int(dbgCommand("dt ntdll!_image_optional_header {}+{}+0x18 dllcharacteristics".format(baseAddr, e_lfanew)).split()[3], 16)
    # determine which DllCharacterisics values have been set
    chars = ""
    for char in dllchars:
        if (dllchars[char] and dllcharacteristics):
            chars += char + "|"
    # print the list of modules and their characteristics
    print("Name: {}, Base: {}, DllCharacteristics: {}".format(mod.name(), baseAddr, chars))