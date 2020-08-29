import nltk

list_irregular = []#irregular past tense
list_regular = []#regular past tense

if __name__ == '__main__':
    try:
        print("stop this process：CTRL+C")
        print('\033[31m'+'past simple'+'\033[0m'+' '+'\033[35m'+'past continue'+'\033[0m'+' '+'\033[33m'+'past perfect simple'+'\033[0m'+' '+'\033[34m'+'past perfect continue'+'\033[0m')
        while True:
            print("")
            print("please input sentence:")
            s = input()
            morph = nltk.word_tokenize(s)#separate all words
            pos = nltk.pos_tag(morph)#set tags
            
            print("")
            print("result:")
            #Identify and output
            i = 0
            while i < len(pos): #loop all
                #find irregular past tense and output
                if ('VBD' in pos[i][1] and (False == pos[i][0].endswith('ed'))) or pos[i][0] == 'Did':
                    list_irregular.append(pos[i][0])
                    if pos[i+1][0] == '.' or pos[i+1][0] == ',' or pos[i+1][0] == '?':
                        #identify past perfect simple and past perfect continue
                        if pos[i][0] == 'had':
                            #past perfect simple
                            if(pos[i+1][1] == 'VBD' or pos[i+1][1] == 'VBN') and pos[i+1][0] != 'been':
                                print('\033[33m\033[4m'+pos[i][0]+'(irregular)'+' '+pos[i+1][0]+'\033[0m',end = '')
                                i = i + 1
                            elif (pos[i+2][1] == 'VBD' or pos[i+2][1] == 'VBN') and pos[i+2][0] != 'been':
                                print('\033[33m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m'+' '+pos[i+1][0]+' '+'\033[33m\033[4m'+pos[i+2][0]+'\033[0m',end = '')
                                i = i + 2
                            #past perfect continue
                            elif pos[i+1][0] == 'been':
                                print('\033[34m\033[4m'+pos[i][0]+'(irregular)'+' '+pos[i+1][0]+' '+pos[i+2][0]+'\033[0m',end = '')
                                i = i + 2
                            else: 
                                print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m',end = '')
                        #identify past continue
                        elif (pos[i][0] == 'was' or pos[i][0] == 'were'):
                            if True == pos[i+1][0].endswith('ing'):
                                print('\033[35m\033[4m'+pos[i][0]+'(irregular)'+' '+pos[i+1][0]+'\033[0m',end = '')
                                i = i + 1
                            elif True == pos[i+2][0].endswith('ing'):
                                print('\033[35m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m'+' '+pos[i+1][0]+' '+'\033[35m\033[4m'+pos[i+2][0]+'\033[0m',end = '')
                                i = i + 2
                            else : print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m',end = '')
                        elif pos[i][0] == 'did' and pos[i+2][1] == 'VB':
                            print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m'+' '+pos[i+1][0]+' '+'\033[31m\033[4m'+pos[i+2][0]+'\033[0m',end = '')
                            i = i + 2
                        else: print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m',end = '')
                    else: 
                         #identify past perfect simple and past perfect continue
                        if pos[i][0] == 'had':
                            #past perfect simple
                            if(pos[i+1][1] == 'VBD' or pos[i+1][1] == 'VBN') and pos[i+1][0] != 'been':
                                print('\033[33m\033[4m'+pos[i][0]+'(irregular)'+' '+pos[i+1][0]+'\033[0m',end = ' ')
                                i = i + 1
                            elif (pos[i+2][1] == 'VBD' or pos[i+2][1] == 'VBN') and pos[i+2][0] != 'been':
                                print('\033[33m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m'+' '+pos[i+1][0]+' '+'\033[33m\033[4m'+pos[i+2][0]+'\033[0m',end = ' ')
                                i = i + 2
                            #past perfect continue
                            elif pos[i+1][0] == 'been':
                                print('\033[34m\033[4m'+pos[i][0]+'(irregular)'+' '+pos[i+1][0]+' '+pos[i+2][0]+'\033[0m',end = ' ')
                                i = i + 2
                            else: 
                                print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m',end = ' ')
                         #identify past continue
                        elif (pos[i][0] == 'was' or pos[i][0] == 'were'):
                            if True == pos[i+1][0].endswith('ing'):
                                print('\033[35m\033[4m'+pos[i][0]+'(irregular)'+' '+pos[i+1][0]+'\033[0m',end = ' ')
                                i = i + 1
                            elif True == pos[i+2][0].endswith('ing'):
                                print('\033[35m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m'+' '+pos[i+1][0]+' '+'\033[35m\033[4m'+pos[i+2][0]+'\033[0m',end = ' ')
                                i = i + 2
                            else : print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m',end = ' ')
                        elif pos[i][0] == 'did' and pos[i+2][1] == 'VB':
                            print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m'+' '+pos[i+1][0]+' '+'\033[31m\033[4m'+pos[i+2][0]+'\033[0m',end = ' ')
                            i = i + 2
                        else: print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m',end = ' ')
                #find regular past tense and output
                elif 'VBD' == pos[i][1] and pos[i][0].endswith('ed') :
                    list_regular.append(pos[i][0])
                    if pos[i+1][0] == '.' or pos[i+1][0] == ',' or pos[i+1][0] == '?':
                        print('\033[31m\033[4m'+pos[i][0]+'(regular)'+'\033[0m',end = '')
                    else: print('\033[31m\033[4m'+pos[i][0]+'(regular)'+'\033[0m',end = ' ')
                    

                #',''.'processing and other output
                else: 
                    if i == len(pos)-1: print(pos[i][0])
                    elif pos[i+1][0] == '.' or pos[i+1][0] == ',' or pos[i+1][0] == '?':
                        print(pos[i][0],end = '')
                    else: print(pos[i][0],end = ' ')
                
                i = i + 1

                

    #ctrl + c 
    except KeyboardInterrupt:
        print("")
        print("finish this process")
