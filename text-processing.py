import re
import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize

def get_year(file):
    """
    Complete this  function using the search function of the re library to obtain and return the year that a file in
    the gutenberg collection was written.
    :param file string with the file of the gutenberg collection
    :return the year as string or the empty string if not found
    >>> get_year('carroll-alice.txt')
    '1865'
    >>> get_year('shakespeare-hamlet.txt')
    '1599'
    """
    currentFile = gutenberg.raw(file)

    match = re.search(r'(\b\d{4}\s*[\]])', currentFile)
    if match:
        return match.group(0).split(']')[0]
    else:
        return ''


def find_mentions(text, file):
    """
    Complete this  function using the findall function of the re library to compute and report the number of times some
    text appears in a file of the gutenberg collection.
    :param file string with the file of the gutenberg collection
    :param text string that we are looking for inside the gutenberg collection file
    :return the number of times text appears in file
    >>> find_mentions('CHAPTER ', 'carroll-alice.txt')
    12
    >>> find_mentions('Caesar', 'shakespeare-caesar.txt')
    227
    >>> find_mentions('UNK', 'shakespeare-caesar.txt')
    0
    """
    currentFile = gutenberg.raw(file)

    match = re.findall(text, currentFile)
    if match:
        return len(match)
    else:
        return 0


def average_sentence_length(file):
    """
    Complete the following function to return the mean number of words in the sentences of a gutenberg file that is
    given as input. The number should be rounded to 2 decimals.
    :param file string with the file of the gutenberg collection
    :return average length of sentences in given file
    >>> average_sentence_length('shakespeare-caesar.txt')
    11.94
    >>> average_sentence_length('austen-emma.txt')
    24.82
    """
    words = 0
    sents = 0
    e = 0
    e2 = 0
    for sent in gutenberg.sents(file):
        words += len(sent)
        sents += 1
        sent_tokenize_list = word_tokenize(sent)
    result = words / sents
    result = round(result, 2)
    #sent_tokenize_list = sent_tokenize(currentFile)
    #print (sent_tokenize_list)

    #result = sum(len(sent) for sent in gutenberg.sents(file)) / len(gutenberg.sents(file))
    return result




get_year('shakespeare-hamlet.txt')
find_mentions('Caesar', 'shakespeare-caesar.txt')