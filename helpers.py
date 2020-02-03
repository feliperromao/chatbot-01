from nltk import tokenize
from string import punctuation
import nltk
import unidecode


def prepare_dataset(dataset, text_column):

    list_phrases = list()

    for phrase in dataset[text_column]:
        # Remove palavras sem importancia
        new_phrase = remove_stopwords(phrase)

        # Remove pontuação
        new_phrase = remove_punctuation(new_phrase)

        # Remove acentos
        new_phrase = unidecode.unidecode(new_phrase)

        list_phrases.append(new_phrase)

    return list_phrases


def remove_stopwords(text):
    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('portuguese')
    new_phrase = list()

    token_space = tokenize.WhitespaceTokenizer()
    words_text = token_space.tokenize(text)

    for word in words_text:
        if word not in stopwords:
            new_phrase.append(word)

    return ' '.join(new_phrase)


def remove_punctuation(text):
    new_text = list()

    # Cria lista com as pontuações de texto
    list_punctuation = [value for value in punctuation]

    # Cria token por pontuação
    token_punctuation = tokenize.WordPunctTokenizer()
    # Separa palavras do texto pelo token de pontuação
    words_text = token_punctuation.tokenize(text)

    # Filtra palavras
    for word in words_text:
        if word not in list_punctuation:
            new_text.append(word)
    
    # Junta as palavras que passaram no filtro e retorna as mesmas em uma única string
    return ' '.join(new_text)


def print_wordcloud(dataset):
    pass


def print_most_used(dataset):
    pass