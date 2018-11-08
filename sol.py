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

def summarize(text, ratio=0.2, language="english"):    
    # Gets a list of processed sentences.
    sentences = clean_text_by_sentences(text, language)

    # Creates the graph and calculates the similarity coefficient for every pair of nodes.
    graph = build_graph([sentence.token for sentence in sentences])
    _set_graph_edge_weights(graph)

    # Remove all nodes with all edges weights equal to zero.
    remove_unreachable_nodes(graph)

    # PageRank cannot be run in an empty graph.
    if len(graph.nodes()) == 0:
        return []

    # Ranks the tokens using the PageRank algorithm. Returns dict of sentence -> score
    pagerank_scores = pagerank_weighted(graph)

    # Adds the summa scores to the sentence objects.
    _add_scores_to_sentences(sentences, pagerank_scores)

    # Extracts the most important sentences with the selected criterion.
    extracted_sentences = _extract_most_important_sentences(sentences, ratio)

    # Sorts the extracted sentences by apparition order in the original text.
    extracted_sentences.sort(key=lambda s: s.index)

    #return 0
    return _format_results(extracted_sentences)


def _format_results(extracted_sentences):
    return "\n".join([sentence.text for sentence in extracted_sentences])

def get_text_from_test_data(file):
    pre_path = os.path.join(os.path.dirname(__file__))
    with open(os.path.join(pre_path, file), mode='r', encoding="utf-8") as f:
        return f.read()

text = get_text_from_test_data("mihalcea_tarau.txt")
generated_summary = summarize(text)

print(generated_summary)