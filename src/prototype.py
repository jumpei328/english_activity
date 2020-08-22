import nltk

list_irregular = []#irregular past tense
list_regular = []#regular past tense

print("please input sentence:")
s = input()
#"Two frogs, a father and his son, accidentally fell into a bucket of milk. They started swimming for their lives. They swam for a long time, but there seemed no hope of their getting out. The father soon gave up and drowned. The son carried on swimming. During this time, the milk had begun to form a ball of butter. Using this island of butter as a platform, he managed to hop out of the bucket"
morph = nltk.word_tokenize(s)#separate all words
pos = nltk.pos_tag(morph)#set tags

for i in range(len(pos)): #loop all
    #find irregular past tense
    if 'VBD' in pos[i][1] and (False == pos[i][0].endswith('ed')): 
        list_irregular.append(pos[i][0])
    #find regular past tense
    if 'VBD' == pos[i][1] and pos[i][0].endswith('ed') :
        list_regular.append(pos[i][0])

print("result:")
for text in pos:
    if text[1]=='VBD':
        if (False == text[0].endswith('ed')):
            print('\033[31m\033[4m'+text[0]+'(irregular)'+'\033[0m',end = ' ')
        else:
            print('\033[32m\033[4m'+text[0]+'(regular)'+'\033[0m',end = ' ')
    else:print(text[0],end = ' ')
    
print('.')
