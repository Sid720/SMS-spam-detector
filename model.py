import ssl
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# This bypasses the SSL Certificate error
ssl._create_default_https_context = ssl._create_unverified_context

# 1. Load Data
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])
df['label_num'] = df.label.map({'ham': 0, 'spam': 1})

# 2. Train Model
cv = CountVectorizer()
X = cv.fit_transform(df.message)
y = df.label_num
model = MultinomialNB()
model.fit(X, y)

# 3. Save "Brain" files
pickle.dump(cv, open('cv.pkl', 'wb'))
pickle.dump(model, open('model.pkl', 'wb'))
print("SUCCESS: cv.pkl and model.pkl have been created!")