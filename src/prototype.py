import nltk

list_irregular = []#irregular past tense
list_regular = []#regular past tense

if __name__ == '__main__':
    try:
        print("stop this process：CTRL+C")
        while True:
            print("")
            print("please input sentences:")
            s = input()
            morph = nltk.word_tokenize(s)#separate all words
            pos = nltk.pos_tag(morph)#set tags

            print("")
            print("result:")
            #Identify and output
            for i in range(len(pos)): #loop all
                #find irregular past tense and output
                if 'VBD' in pos[i][1] and (False == pos[i][0].endswith('ed')):
                    list_irregular.append(pos[i][0])
                    if pos[i+1][0] == '.' or pos[i+1][0] == ',':
                        print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m',end = '')
                    else: print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m',end = ' ')

                #find regular past tense and output
                elif 'VBD' == pos[i][1] and pos[i][0].endswith('ed') :
                    list_regular.append(pos[i][0])
                    if pos[i+1][0] == '.' or pos[i+1][0] == ',':
                        print('\033[32m\033[4m'+pos[i][0]+'(regular)'+'\033[0m',end = '')
                    else: print('\033[32m\033[4m'+pos[i][0]+'(regular)'+'\033[0m',end = ' ')

                #',''.'processing and other output
                else: 
                    if i == len(pos)-1: print(pos[i][0])
                    elif pos[i+1][0] == '.' or pos[i+1][0] == ',':
                        print(pos[i][0],end = '')
                    else: print(pos[i][0],end = ' ')
    #ctrl + c 
    except KeyboardInterrupt:
        print("")
        print("finish this process")
