import re, collections

""" 

Spell checking class. Modified version of Peter Norvig's spell checker.

""" 

class spell_checker(object): 
  def __init__(self):

    self.NWORDS = self.train(self.words(file('/Users/shilpa/CS242/subrahm2/FinalProject/big.txt').read()))
    self.alphabet = 'abcdefghijklmnopqrstuvwxyz'


  def words(self, text): return re.findall('[a-z]+', text.lower()) 

  def train(self, features):
      """ train the model on the default dictionary 
          @param features: a set of features on which we need to train our default dictionary 
          @return a model that has been trained by the input features 
      """ 

      model = collections.defaultdict(lambda: 1)
      for f in features:
          model[f] += 1
      return model


  def edits1(self, word):
    """ Determines words that are one edit distance away from input word 
    @param word: the word for which we want to determine all the words 1 edit distance away 
    @return a set of words that are one edit distance away """ 

    splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes    = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
    replaces   = [a + c + b[1:] for a, b in splits for c in self.alphabet if b]
    inserts    = [a + c + b     for a, b in splits for c in self.alphabet]
    return set(deletes + transposes + replaces + inserts)

  def known_edits2(self, word):
    """ Determines words that are two edit distance away from input word 
    @param word: the word for which we want to find all words within one
    @return set of words that are two edit distances away from the original word (not the input param)"""
     
    return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1) if e2 in self.NWORDS)


  def known(self, words): 
    """ Determine if a given word is "known" or for the purposes of this spell checker, correctly spelled 
    @param words: set of words 
    @return set of the words that are "known" or correctly spelled"""

    return set(w for w in words if w in self.NWORDS)

  def correct(self, word):
      """ Given a word, returns the same word if the word is spelled correctly. Returns corrected word if word is spelled incorrectly 
          @param word: a given word 
          @return the suggested correct form of the input word 
      """ 

      candidates = self.known([word]) or self.known(self.edits1(word)) or self.known_edits2(word) or [word]
      return max(candidates, key=self.NWORDS.get)




