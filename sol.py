from utils.textcleaner import clean_text_by_sentences
from graphBuild import build_graph
from graphBuild import remove_unreachable_nodes
from graphBuild import _set_graph_edge_weights
from graphBuild import _create_valid_graph
from pagerank_weighted import pagerank_weighted
import os.path
from math import log10

def _get_similarity(s1, s2):
    words_sentence_one = s1.split()
    words_sentence_two = s2.split()

    common_word_count = _count_common_words(words_sentence_one, words_sentence_two)

    log_s1 = log10(len(words_sentence_one))
    log_s2 = log10(len(words_sentence_two))

    if log_s1 + log_s2 == 0:
        return 0

    return common_word_count / (log_s1 + log_s2)

def _count_common_words(words_sentence_one, words_sentence_two):
    return len(set(words_sentence_one) & set(words_sentence_two))


def _add_scores_to_sentences(sentences, scores):
    for sentence in sentences:
        if sentence.token in scores:
            sentence.score = scores[sentence.token]
        else:
            sentence.score = 0

def _extract_most_important_sentences(sentences, ratio):
    sentences.sort(key=lambda s: s.score, reverse=True)
    length = len(sentences) * ratio
    return sentences[:int(length)]


def summarize():
    return 0