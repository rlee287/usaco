sig_orig=str()
sig_new=list()
with open("cowsignal.in","r") as input_file:
    m,n,k=input_file.readline().split(" ")
    m,n,k=tuple(int(q) for q in [m,n,k])
    for _ in range(m):
        line=input_file.readline()
        sig_orig+=line

def writeamp(string):
    returnstring=str()
    charlist=list(string)
    for char in charlist:
        for _ in range(k):
            returnstring+=char
    return returnstring

sig_line=sig_orig.split("\n")
for line in sig_line:
    out_line=writeamp(line)
    for _ in range(k):
        if out_line!="":
            sig_new.append(out_line)
print(sig_new)
with open("cowsignal.out","w") as output_file:
    output_file.write("\n".join(sig_new))
    output_file.write("\n")
