def read_dict():
    f = open("ce（ms-word）.txt")
    word_dict = set()
    while 1:
        line = f.readline()
        if line == '':
            break
        line_list = line.strip().split(',')
        word = line_list[0]
#        print(word)
        word_dict.add(word)
#        print(word_dict)
    f.close()
    return word_dict


def FMM(word, word_dict, window):
    word_len = len(word)
    index = 0
    tokens = []
    while index < word_len:
        for size in range(min(window + index, word_len), index, -1):
            tmp = word[index:size]
            if tmp in word_dict:
                index = size
                tokens.append(tmp)
                break
    return tokens

def RMM(word, word_dict, window):
    word_len = len(word)
    index = word_len
    tokens = []
    while index > 0:
        for size in range(max(0, index - window), index):
            tmp = word[size:index]
            if tmp in word_dict:
                index = size
                tokens.append(tmp)
                break
    return tokens

def BiMM(fmm_tokens, rmm_tokens):
    if len(fmm_tokens) > len(rmm_tokens):
        return rmm_tokens
    elif len(fmm_tokens) == len(rmm_tokens):
        if set(fmm_tokens) == set(rmm_tokens):
            return fmm_tokens
        else:
            fmm_count = 0
            rmm_count = 0
            for i in fmm_tokens:
                if len(i) == 1:
                    fmm_count += 1
            for i in rmm_tokens:
                if len(i) == 1:
                    rmm_count += 1
            if fmm_count < rmm_count:
                return fmm_tokens
            else:
                return rmm_tokens
    else:
        return fmm_tokens

    
def main():
    word_dict = read_dict()
#    print(word_dict)
    word = input("input a sentence: ")
    fmm_tokens = FMM(word, word_dict, 6)
    rmm_tokens = RMM(word, word_dict, 6)
    tokens = BiMM(fmm_tokens, rmm_tokens)
#    print(fmm_tokens, rmm_tokens)
#    print(tokens)
    print('/'.join(tokens))


if __name__ == "__main__":
    while 1:
        main()
    
