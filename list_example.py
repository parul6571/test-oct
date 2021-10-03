list_example=[]
print(list_example)

# list_example=[1,2,3,4]
# print(list_example)

# sequences=["ATGATAAGAT","ATAGTATAA","ATAGTAGAAT"]
# print(sequences)

list_example=[1,2,3,4]
print(list_example)

sequences=["ATGATAAGAT","ATAGTATAA","ATAGTAGAAT"]
print(sequences)

#len==>get the length ofthelist
#syntax==>len(name_of_list)
print(len(sequences))
print(len(list_example))

list_example=[]
print(len(list_example))
sequences.append("ATCCCG")
print(sequences)
sequences.insert(0,"ATCCGG")
# Inserting element at any position
#list_name(index,data)
sequences.insert(0,"ATGC")
print(sequences)
sequences.insert(2,"ATGC")
print(sequences)
seq=[]
seq.append("ATCG")
seq.append("AATTCC")
seq.insert(0,"GGGGGG")
print(seq)

seq=[]
seq.append("ATGC")  #["ATGC"]
seq.append("AAA") #["ATGC","AAA"]
seq.insert(0,"CC")   #["CC","ATGC","AAA"]
print(seq)

sequences=["AATTTCCCG", "ATTGGCCCC","CGTAAAT","ATCG","AATTGGCC"]
#           0                    1       2        3          4    LEFT TO RIGHT
print(sequences[0])
print(sequences[1])
print(sequences[-2])

#SLICING IN LIST DATA
print(sequences[1:3])
print(sequences[1:5]) # ifvalue pass no syntax error

