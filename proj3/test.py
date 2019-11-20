word_dict = {}
#每个词和对应的词性
ActiveEdge = []
unActiveEdge = []
rules = []
#所有规则对应list的list
input_word = []
agenda = []
word2pos = []
#输入词及其词性
# =============================================================================
# pos = {'conj.', 'pref.', 'prep.', 'comb.', 'Vt.', 'vi.', 'adj.', 'aux.',
#        'suf.', 'pl.', 'int.', 'abbr.', 'adv.', 'n.', 'num.', 'pron.', 'v.',
#        'none.', 'vt.', 'vbl.', 'symb.', 'art.', 'vp.'}
#from nltk.stem import WordNetLemmatizer
#lemmatizer = WordNetLemmatizer()
#word = lemmatizer.lemmatize('running', 'v')
# =============================================================================

def load_dict():
    f = open('dic_ec.txt', 'r', encoding='gbk', errors='replace')
    while 1:
        line = f.readline()
        if line == '':
            break
        linelist = str(line).strip().split()
        if len(linelist) < 2:
            continue
        if linelist[1] == 'none.':
            linelist[1] = 'n.'
        word_dict[linelist[0]] = linelist[1][0:-1].upper()
    f.close()

def add_rule_from_file():
    f = open('rule.txt', 'r')
    while 1:
        line = f.readline()
        if line == '':
            break
        linelist = str(line).strip().split()
        rules.append(linelist)
    
    
def input_word():
    sentence = input('input a sentence: ')
    word_list = sentence.strip().split()
    for word in word_list:
        if word in word_dict:
            tmp = []
            tmp.append(word)
            wordpos_tmp = word_dict[word]
            tmp.append(wordpos_tmp)
            word2pos.append(tmp)
        else:
            print("cann`t find word in dictonary")
            break
    
def parser():
    start = 0
    index2word = 0
    while 1:
        if len(agenda) == start and index2word >= len(word2pos):
            break
        if len(agenda) == start:
            agenda_tmp = []
            agenda_tmp.append(word2pos[index2word][1])
            agenda_tmp.append(index2word)
            agenda_tmp.append(index2word + 1)
            agenda.append(agenda_tmp)
            index2word += 1
            print("获取下一个词词性{}、起点{}、终点{}".format(agenda_tmp[0], agenda_tmp[1], agenda_tmp[2]))
            print('------------------------------------------')
        tmp = agenda[start]
        unactiveedge_tmp = agenda[start]
        unActiveEdge.append(unactiveedge_tmp)
        start += 1
        print('从agenda中获取一个词词性{}、起点{}、终点{}'.format(tmp[0], tmp[1], tmp[2]))
        print('------------------------------------------')
        print('增加非活动边词性{}、起点{}、终点{}'.format(tmp[0], tmp[1], tmp[2]))
        print('------------------------------------------')
        for activeedge in ActiveEdge:
            if rules[activeedge[0]][activeedge[3]] == tmp[0] and activeedge[2] == tmp[1] and len(rules[activeedge[0]]) - 1 == activeedge[3]:
                agenda_tmp = []
                agenda_tmp.append(rules[activeedge[0]][0])
                agenda_tmp.append(activeedge[1])
                agenda_tmp.append(tmp[2])
                agenda.append(agenda_tmp)
                print('活动边扩展')
                print('应用规则{}'.format(rules[activeedge[0]]))
                print('将词性{}、起点{}、终点{}加入到agenda中'.format(rules[activeedge[0]][0], activeedge[1], tmp[2]))
                print('------------------------------------------')
            elif rules[activeedge[0]][activeedge[3]] == tmp[0] and activeedge[2] == tmp[1]:
                activeedge_tmp = []
                activeedge_tmp.append(activeedge[0])
                activeedge_tmp.append(activeedge[1])
                activeedge_tmp.append(tmp[2])
                activeedge_tmp.append(activeedge[3] + 1)
                ActiveEdge.append(activeedge_tmp)
                print('活动边扩展')
                print('应用规则{}'.format(rules[activeedge[0]]))
                print('将词性{}、起点{}、终点{}、即将规约的词位置{}加入到活动边中'.format(rules[activeedge[0]][0], activeedge[1], tmp[2], activeedge[3] + 1))
                print('------------------------------------------')
        for rule_index, rule in enumerate(rules):
            if rule[2].upper() == tmp[0] and len(rule) == 3:
                agenda_tmp = []
                agenda_tmp.append(rule[0])
                agenda_tmp.append(tmp[1])
                agenda_tmp.append(tmp[2])
                agenda.append(agenda_tmp)
                print('活动边增加')
                print('应用规则{}'.format(rule))
                print('将词性{}、起点{}、终点{}加入到agenda中'.format(rule[0], tmp[1], tmp[2]))
                print('------------------------------------------')
            elif rule[2].upper() == tmp[0]:
                activeedge_tmp = []
                activeedge_tmp.append(rule_index)
                activeedge_tmp.append(tmp[1])
                activeedge_tmp.append(tmp[2])
                activeedge_tmp.append(3)
                ActiveEdge.append(activeedge_tmp)
                print('增加活动边')
                print('应用规则{}'.format(rule))
                print('将词性{}、起点{}、终点{}、即将规约的词位置{}加入到活动边中'.format(rule[0], tmp[1], tmp[2], 3))
                print('------------------------------------------')
    if index2word == len(word2pos):
        print('successful')
        
if __name__ == '__main__':
    load_dict()
    print(word_dict)
    input_word()
#    print(word2pos)
    add_rule_from_file()
#    print(rules)
    parser()
    
        
    


      