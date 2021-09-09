import sys

version = sys.version_info.major
system = sys.platform

if system != "linux":
    sys.exit()

if version == 2:
    texto = raw_input("digite: ")
    print("oi", texto)

elif version ==3:
    texto = input("digite: ")
    print("oi", texto)