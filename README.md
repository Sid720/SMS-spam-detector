# SMS Spam Detector

A real-time Machine Learning web application that classifies SMS messages as **Spam** or **Ham** (Normal) using Natural Language Processing (NLP).

##  Live Demo
[Click here to view the live app on Streamlit Cloud](PASTE_YOUR_STREAMLIT_LINK_HERE)

##  How it Works
1. **Data:** Trained on the UCI SMS Spam Collection dataset.
2. **Preprocessing:** Uses `CountVectorizer` to convert text into numerical features.
3. **Algorithm:** Implements a **Multinomial Naive Bayes** classifier, known for its efficiency in text classification.
4. **Interface:** Built with **Streamlit** for a responsive, user-friendly experience.

##  Tech Stack
* **Language:** Python 3.14
* **Libraries:** Scikit-Learn, Pandas, Pickle
* **Deployment:** Streamlit Cloud

## Local Setup
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the trainer: `python model.py`.
4. Launch the app: `streamlit run app.py`.

##  Accuracy & Testing
The model has been tested against common spam phrases and verified to provide instant feedback with a visual color-coded result (Red for Spam, Green for Ham).