import re
import os
SWY = bytes("SWY", 'utf-8')
END = bytes("END", "utf-8")

def pack(files:list, output):
    for file in files:
        with open(file, "rb") as f:
            image_data = f.read()
        with open(output, "ab") as f:
            fname = bytes(file, "utf-8")
            image_data = SWY+fname+END+image_data
            f.write(image_data)
            f.close()
        os.remove(file)



def unpack(input:str):
    f = open(input, "rb")
    data = f.read()
    f.close()

    ind_start = [m.start() for m in re.finditer(SWY, data)]
    ind_start.append(len(data)-1)

    ind_end = [m.start() for m in re.finditer(END, data)]
    
    for i in range(len(ind_end)):
        name = data[ind_start[i]+3:ind_end[i]].decode("utf-8")
        with open(name, "wb") as f:
            start = ind_end[i] + 3
            end = ind_start[i+1]
            f.write(data[start:end])
    os.remove(input)
    
