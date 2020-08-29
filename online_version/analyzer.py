import re
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


class Analyzer:
    def tense_analyze(self, value_str):
        if(len(value_str) > 0 and "." != value_str[-1]):
            value_str = value_str+"."
        s = value_str
        morph = nltk.word_tokenize(value_str)
        pos = nltk.pos_tag(morph)
        result = [[0] * 3 for i in range(len(pos))]
        #[0,0,0][0,0,0]....[0,0,0] [0,0,0]xlen(pos)
        #[0,0,0] = [word,regular(1) or irrgular(2), past simple(1) or past continiue(2) or past perfect simple(3) or past perfect continue(4)]
        list_irregular = []#irregular past tense
        list_regular = []#regular past tense
        i = 0
        while i < len(pos): #loop all
                #find irregular past tense and output
                if ('VBD' in pos[i][1] and (False == pos[i][0].endswith('ed'))) or pos[i][0] == 'Did':
                    list_irregular.append(pos[i][0])
                    if pos[i+1][0] == '.' or pos[i+1][0] == ',' or pos[i+1][0] == '?':
                        if pos[i][0] == 'had':
                            if(pos[i+1][1] == 'VBD' or pos[i+1][1] == 'VBN') and pos[i+1][0] != 'been':
                                #print('\033[33m\033[4m'+pos[i][0]+'(irregular)'+' '+pos[i+1][0]+'\033[0m',end = '')
                                result[i][0] = pos[i][0]
                                result[i][1] = 2
                                result[i][2] = 3
                                result[i+1][0] = pos[i+1][0]
                                result[i+1][2] = 3
                                i+=1
                            elif (pos[i+2][1] == 'VBD' or pos[i+2][1] == 'VBN') and pos[i+2][0] != 'been':
                                #print('\033[33m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m'+' '+pos[i+1][0]+' '+'\033[33m\033[4m'+pos[i+2][0]+'\033[0m',end = '')
                                result[i][0] = pos[i][0]
                                result[i][1] = 2
                                result[i][2] = 3
                                result[i+1][0] = pos[i+1][0]
                                result[i+2][0] = pos[i+2][0]
                                result[i+2][2] = 3
                                i+=2
                            elif pos[i+1][0] == 'been':
                                #print('\033[34m\033[4m'+pos[i][0]+'(irregular)'+' '+pos[i+1][0]+' '+pos[i+2][0]+'\033[0m',end = '')
                                result[i][0] = pos[i][0]
                                result[i][1] = 2
                                result[i][2] = 4
                                result[i+1][0] = pos[i+1][0]
                                result[i+1][2] = 4
                                result[i+2][0] = pos[i+2][0]
                                result[i+2][2] = 4
                                i+=2
                            else: 
                                #print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m',end = '')
                                result[i][0] = pos[i][0]
                                result[i][1] = 2
                                result[i][2] = 1
                        elif (pos[i][0] == 'was' or pos[i][0] == 'were'):
                            if True == pos[i+1][0].endswith('ing'):
                                #print('\033[35m\033[4m'+pos[i][0]+'(irregular)'+' '+pos[i+1][0]+'\033[0m',end = '')
                                result[i][0] = pos[i][0]
                                result[i][1] = 2
                                result[i][2] = 2
                                result[i+1][0] = pos[i+1][0]
                                result[i+1][2] = 2
                                i+=1
                            elif True == pos[i+2][0].endswith('ing'):
                                #print('\033[35m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m'+' '+pos[i+1][0]+' '+'\033[35m\033[4m'+pos[i+2][0]+'\033[0m',end = '')
                                result[i][0] = pos[i][0]
                                result[i][1] = 2
                                result[i][2] = 2
                                result[i+1][0] = pos[i+1][0]
                                result[i+2][0] = pos[i+2][0]
                                result[i+2][2] = 2
                                i+=2
                            else : 
                                #print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m',end = '')
                                result[i][0] = pos[i][0]
                                result[i][1] = 2
                                result[i][2] = 1

                        elif pos[i][0] == 'did' and pos[i+2][1] == 'VB':
                            #print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m'+' '+pos[i+1][0]+' '+'\033[31m\033[4m'+pos[i+2][0]+'\033[0m',end = '')
                            result[i][0] = pos[i][0]
                            result[i][1] = 2
                            result[i][2] = 1
                            result[i+1][0] = pos[i+1][0]
                            result[i+2][0] = pos[i+2][0]
                            result[i+2][2] = 1
                            i += 2 

                        else: 
                            #print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m',end = '')
                            result[i][0] = pos[i][0]
                            result[i][1] = 2
                            result[i][2] = 1
                    else: 
                        if pos[i][0] == 'had':
                            if(pos[i+1][1] == 'VBD' or pos[i+1][1] == 'VBN') and pos[i+1][0] != 'been':
                                #print('\033[33m\033[4m'+pos[i][0]+'(irregular)'+' '+pos[i+1][0]+'\033[0m',end = '')
                                result[i][0] = pos[i][0]
                                result[i][1] = 2
                                result[i][2] = 3
                                result[i+1][0] = pos[i+1][0]
                                result[i+1][2] = 3
                                i+=1
                            elif (pos[i+2][1] == 'VBD' or pos[i+2][1] == 'VBN') and pos[i+2][0] != 'been':
                                #print('\033[33m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m'+' '+pos[i+1][0]+' '+'\033[33m\033[4m'+pos[i+2][0]+'\033[0m',end = '')
                                result[i][0] = pos[i][0]
                                result[i][1] = 2
                                result[i][2] = 3
                                result[i+1][0] = pos[i+1][0]
                                result[i+2][0] = pos[i+2][0]
                                result[i+2][2] = 3
                                i+=2
                            elif pos[i+1][0] == 'been':
                                #print('\033[34m\033[4m'+pos[i][0]+'(irregular)'+' '+pos[i+1][0]+' '+pos[i+2][0]+'\033[0m',end = '')
                                result[i][0] = pos[i][0]
                                result[i][1] = 2
                                result[i][2] = 4
                                result[i+1][0] = pos[i+1][0]
                                result[i+1][2] = 4
                                result[i+2][0] = pos[i+2][0]
                                result[i+2][2] = 4
                                i+=2
                            else: 
                                #print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m',end = '')
                                result[i][0] = pos[i][0]
                                result[i][1] = 2
                                result[i][2] = 1
                        elif (pos[i][0] == 'was' or pos[i][0] == 'were'):
                            if True == pos[i+1][0].endswith('ing'):
                                #print('\033[35m\033[4m'+pos[i][0]+'(irregular)'+' '+pos[i+1][0]+'\033[0m',end = '')
                                result[i][0] = pos[i][0]
                                result[i][1] = 2
                                result[i][2] = 2
                                result[i+1][0] = pos[i+1][0]
                                result[i+1][2] = 2
                                i+=1
                            elif True == pos[i+2][0].endswith('ing'):
                                #print('\033[35m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m'+' '+pos[i+1][0]+' '+'\033[35m\033[4m'+pos[i+2][0]+'\033[0m',end = '')
                                result[i][0] = pos[i][0]
                                result[i][1] = 2
                                result[i][2] = 2
                                result[i+1][0] = pos[i+1][0]
                                result[i+2][0] = pos[i+2][0]
                                result[i+2][2] = 2
                                i+=2
                            else : 
                                #print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m',end = '')
                                result[i][0] = pos[i][0]
                                result[i][1] = 2
                                result[i][2] = 1

                        elif pos[i][0] == 'did' and pos[i+2][1] == 'VB':
                            #print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m'+' '+pos[i+1][0]+' '+'\033[31m\033[4m'+pos[i+2][0]+'\033[0m',end = '')
                            result[i][0] = pos[i][0]
                            result[i][1] = 2
                            result[i][2] = 1
                            result[i+1][0] = pos[i+1][0]
                            result[i+2][0] = pos[i+2][0]
                            result[i+2][2] = 1
                            i += 2 

                        else: 
                            #print('\033[31m\033[4m'+pos[i][0]+'(irregular)'+'\033[0m',end = '')
                            result[i][0] = pos[i][0]
                            result[i][1] = 2
                            result[i][2] = 1
                #find regular past tense and output
                elif 'VBD' == pos[i][1] and pos[i][0].endswith('ed') :
                    list_regular.append(pos[i][0])
                    if pos[i+1][0] == '.' or pos[i+1][0] == ',' or pos[i+1][0] == '?':
                        #print('\033[31m\033[4m'+pos[i][0]+'(regular)'+'\033[0m',end = '')
                        result[i][0] = pos[i][0]
                        result[i][1] = 1
                        result[i][2] = 1
                    else: 
                        #print('\033[31m\033[4m'+pos[i][0]+'(regular)'+'\033[0m',end = ' ')
                        result[i][0] = pos[i][0]
                        result[i][1] = 1
                        result[i][2] = 1
                    

                #',''.'processing and other output
                else: 
                    if i == len(pos)-1: 
                        #print(pos[i][0])
                        result[i][0] = pos[i][0]
                    elif pos[i+1][0] == '.' or pos[i+1][0] == ',' or pos[i+1][0] == '?':
                        #print(pos[i][0],end = '')
                        result[i][0] = pos[i][0]
                    else: 
                        #print(pos[i][0],end = ' ')
                        result[i][0] = pos[i][0]

                i += 1


        return result