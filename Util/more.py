"""
split and interactively page a string or file of text
"""
def more(text, numlines=15):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and input('More?') not in ['Y','y']: break

if __name__=='__main__':
    import sys
    try:
        more(open(sys.argv[1]).read(),10)
    except IndexError:
        print("Usage: more.py {Your File Name}")
