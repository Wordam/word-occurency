from collections import Counter,OrderedDict
import string, sys
f = open(sys.argv[1],'r')
text = f.read()
f.close()
stripped_text = ''.join(ch for ch in text if ch not in set(string.punctuation))
histogram = Counter(stripped_text.split(' '))
max_word_len = max(len(x) for x in histogram.keys())
histogram = OrderedDict(reversed(histogram.most_common()))
for i in histogram.items():
    print i[0] + (max_word_len - len(i[0])) * ' ', i[1], i[1] * '*'
total = str(sum(c[1] for c in histogram.items()))
print 'TOTAL' + (max_word_len - len('TOTAL')) * ' ', total, 'words'
