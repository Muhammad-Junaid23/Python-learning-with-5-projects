# we will learn about file handling

summary = "This is unknownX, a soft engg at DevX working Remotely as Team lead."

#old way of writing to a file
# pf= open('profile.txt','w')
# pf.write(summary)
# pf.close()



# write a file through reference
# with open('profile.txt','w') as pf:
    # pf.write(summary)


# reading a file
with open('profile.txt','r') as rp:
    text=rp.read()
    print(text)


# if we write to a file with existing text then write function will overwrite it and
# therefore it is safe to use append so we have previous text in the file and next text is added to last

with open('profile.txt','a') as ap:
    ap.write('Specialization in React and Next js')

print(text)