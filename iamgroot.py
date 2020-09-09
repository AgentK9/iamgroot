from random import randint
iamgroot = "i am groot"

# I am groot.
while True:
    Iamgroot = input("I am Groot?\t")
    try:
        if Iamgroot.lower() == iamgroot:
            Iamgroot = randint(0, 100000)
        Iamgroot = int(Iamgroot)
        if Iamgroot > len(iamgroot):
            break
    except ValueError:
        continue


iAmgroot = ['.', '?', '!', ',']
iaMgroot = int(Iamgroot / (len(iamgroot) + 2))
for iamGroot in range(iaMgroot):
    iamgRoot = ''
    for iamgrOot in iamgroot:
        if randint(0, 1):
            iamgRoot += iamgrOot
        else:
            iamgRoot += iamgrOot.upper()
    print(iamgRoot + iAmgroot[randint(0, len(iAmgroot)-1)], end=' ')


