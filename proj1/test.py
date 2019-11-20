def load_dict():
    word_dict = {}
    f = open('dic_ec.txt', 'r', encoding='gbk', errors='replace')
    while 1:
        line = f.readline()
        if line == '':
            break
        linelist = str(line).strip().split()
        if len(linelist) < 2:
            continue
        word_dict[linelist[0]] = ' '.join(linelist[1:len(linelist)])
    f.close()
    return word_dict


def noun_judge(word, word_dict):
    flag = False
    if not flag and 'ves' == word[-3:len(word)]:
        if word[0:-3] + 'f' in word_dict.keys():
            tmp = word[0:-3] + 'f'
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
        elif word[0:-3] + 'fe' in word_dict.keys():
            tmp = word[0:-3] + 'fe'
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
    if not flag and 'ies' == word[-3:len(word)]:
        if word[0:-3] + 'y' in word_dict.keys():
            tmp = word[0:-3] + 'y'
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
    if not flag and 'es' == word[-2:len(word)]:
        if word[0:-2] in word_dict.keys():
            tmp = word[0:-2]
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
    if not flag and 's' == word[len(word)-1]:
        if word[0:-1] in word_dict.keys():
            tmp = word[0:-1]
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
    return flag
        
def verb_judge(word, word_dict):
    flag = False
    if 'ies' == word[-3:len(word)]:
        if word[0:-3] + 'y' in word_dict.keys():
            tmp = word[0:-3] + 'y'
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
    if not flag and 'es' == word[-2:len(word)]:
        if word[0:-2] in word_dict.keys():
            tmp = word[0:-2]
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
    if not flag and 's' == word[len(word)-1]:
        if word[0:-1] in word_dict.keys():
            tmp = word[0:-1]
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
    if not flag and 'ing' == word[-3:len(word)] and word[-4] == word[-5]:
        if word[0:-4] in word_dict.keys():
            tmp = word[0:-4]
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
    if not flag and 'ing' == word[-3:len(word)]:
        if word[0:-3] in word_dict.keys():
            tmp = word[0:-3]
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
        elif word[0:-3] + 'e' in word_dict.keys():
            tmp = word[0:-3] + 'e'
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
    if not flag and 'ying' == word[-4:len(word)]:
        if word[0:-4] in word_dict.keys():
            tmp = word[0:-4]
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
    if not flag and 'ed' == word[-2:len(word)]:
        if word[0:-2] in word_dict.keys():
            tmp = word[0:-2]
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
        elif word[0:-2] + 'e' in word_dict.keys():
            tmp = word[0:-2] + 'e'
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
    if not flag and 'ed' == word[-2:len(word)] and word[-3] == word[-4]:
        if word[0:-3] in word_dict.keys():
            tmp = word[0:-3]
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
    if not flag and 'ied' == word[-3:len(word)]:
        if word[0:-3] + 'y' in word_dict.keys():
            tmp = word[0:-3] + 'y'
            print("original form: " + tmp)
            print("attribute: " + word_dict[tmp])
            flag = True
    return flag
            
def other_judge(word, word_dict):
    flag = False
    if word in word_dict.keys():
        tmp = word
        print("original form: " + tmp)
        print("attribute: " + word_dict[tmp])
        flag = True
    return flag

def unk(word):
    print("cann`t find this word in the dictionary")
        
def main():
    print("输入词")
    word_input = input("word: ")
    word_dict = load_dict()
    flag = False
    
    flag = noun_judge(word_input, word_dict)
    if flag != True:
        flag = verb_judge(word_input, word_dict)
    if flag != True:
        flag = other_judge(word_input, word_dict)
    if flag == False:
        unk(word_input)
        
        
if __name__ == '__main__':
    while 1:
        main()



       