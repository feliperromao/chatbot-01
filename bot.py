import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
from intent_responses import get_random_response
from helpers import prepare_dataset

np.random.seed = 20

dataset = pd.read_csv('dataset.csv', sep=';')
dataset['text_2'] = prepare_dataset(dataset, 'text')

# Criando extraindo features dos textos
vectorizer = CountVectorizer(lowercase=False)
bag_of_words = vectorizer.fit_transform(dataset['text_2'])

features = vectorizer.get_feature_names()

matriz = pd.DataFrame.sparse.from_spmatrix(bag_of_words, columns=features)


# Separando dados de treino e teste
x_train, x_test, y_train,y_test = train_test_split(
  matriz,
  dataset['intent'],
  test_size=0.25,
  stratify=dataset['intent'],
)

# Treinando modelo e calculando taxa de acerto
model = LogisticRegression()
model.fit(x_train, y_train)

score = model.score(x_test, y_test) * 100

print(f'Taxa de acerto do modelo é de: {score} %')

def predict(text, model_features):

  vectorizer_text = CountVectorizer(lowercase=False)
  vectorizer_text.fit_transform([text])
  text_features = vectorizer_text.get_feature_names()

  data_series = []
  for mf in model_features:
    if mf in text_features:
      data_series.append(1)
    else:
      data_series.append(0)

  result = model.predict([data_series])
  return result[0]


while True:
    text = input('USER: ')
    response = predict(text, features)
    print('BOT: ' + get_random_response(response))