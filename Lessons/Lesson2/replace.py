txt = 'Hello world!'
print(txt, id(txt))
txt = txt.replace(' ', '_')
print(txt, id(txt))


# Hello world! 1945220922480
# Hello_world! 1945220922544