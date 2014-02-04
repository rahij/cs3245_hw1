#!/usr/bin/python
import re
import nltk
import sys
import getopt
import math

# for running against training data
def remove_lang(in_str):
  return " ".join(in_str.split()[1:])

def split_ngrams(in_str, n=4):
  i = 0
  ngrams = []
  in_str = in_str.lower()
  # in_str = in_str.split()
  for c in in_str:
    if i+n > len(in_str):
      break
    # ngrams.append(" ".join(in_str[i:i+n]))
    ngrams.append(in_str[i:i+n])
    i = i + 1
  return ngrams

def build_LM(in_file):
  """
  build language models for each label
  each line in in_file contains a label and an URL separated by a tab(\t)
  """
  print 'building language models...'
  LM = {}
  LM['tamil'] = {}
  LM['malaysian'] = {}
  LM['indonesian'] = {}
  num_ngrams = dict.fromkeys(LM, 0)
  with open(in_file) as f:
    for l in f.readlines():
      l = l.strip()
      lang = l.split()[0]
      ngram_list = split_ngrams(l)
      num_ngrams[lang] = num_ngrams[lang] + len(ngram_list)
      for ngram in ngram_list:
        for langs in LM:
          if ngram not in LM[langs]:
            LM[langs][ngram] = 1.0
        LM[lang][ngram] = LM[lang][ngram]+1.0

  for lang in LM:
    t_sum = 0
    for ngrams in LM[lang]:
      t_sum +=LM[lang][ngrams]
    for ngrams in LM[lang]:
      LM[lang][ngrams] = math.log(LM[lang][ngrams]/float(t_sum))
  return LM

def test_LM(in_file, out_file, LM):
  """
  test the language models on new URLs
  each line of in_file contains an URL
  you should print the most probable label for each URL into out_file
  """
  print "testing language models..."
  to_write = open(out_file, "w")
  with open(in_file) as f:
    for l in f.readlines():
      # l = remove_lang(l)
      prob = dict.fromkeys(LM, math.log(0.0000001))
      ngram_list = split_ngrams(l)
      for lang in LM:
        num_matches = 1
        for ngram in ngram_list:
          if ngram in LM[lang]:
            prob[lang] = prob[lang] + LM[lang][ngram]
            num_matches = num_matches + 1
        prob[lang] = prob[lang]/num_matches
      predicted_lang = max(prob, key=prob.get)
      if prob[predicted_lang] < -10.0:
        predicted_lang = 'other'
      to_write.write(predicted_lang + ' ' + l)

def usage():
  print "usage: " + sys.argv[0] + " -b input-file-for-building-LM -t input-file-for-testing-LM -o output-file"

input_file_b = input_file_t = output_file = None
try:
  opts, args = getopt.getopt(sys.argv[1:], 'b:t:o:')
except getopt.GetoptError, err:
  usage()
  sys.exit(2)
for o, a in opts:
  if o == '-b':
    input_file_b = a
  elif o == '-t':
    input_file_t = a
  elif o == '-o':
    output_file = a
  else:
    assert False, "unhandled option"
if input_file_b == None or input_file_t == None or output_file == None:
  usage()
  sys.exit(2)

LM = build_LM(input_file_b)
test_LM(input_file_t, output_file, LM)