import tensorflow as tf
import streamlit as st
from spacy.lang.en import English

@st.cache
class preprocess_data:
    def __init__(self, abstract_text):
        self.abstract_text = abstract_text

    def prepare_dataset(self):
        nlp = English() 
        sentencizer = nlp.create_pipe("sentencizer")
        nlp.add_pipe(sentencizer) 
        doc = nlp(self.abstract_text) 
        abstract_lines = [str(sent) for sent in list(doc.sents)] 

        line_numbers = list(range(len(abstract_lines)))
        total_lines = [len(abstract_lines)-1]*(len(abstract_lines))

        line_numbers_one_hot = tf.one_hot(line_numbers, depth=20)
        total_lines_one_hot = tf.one_hot(total_lines, depth=20)

        return line_numbers_one_hot, total_lines_one_hot, abstract_lines
    
    def get_predictions(self, line_num, total_lines, sentences, model):
        labels_map = {0: 'BACKGROUND', 1: 'CONCLUSIONS', 2: 'METHODS', 3: 'OBJECTIVE', 4: 'RESULTS'}
        text_classified = {}
        pred_probs = model.predict(x=(line_num,
                                       total_lines,
                                       tf.constant(sentences)))
        preds = tf.argmax(pred_probs, axis=1).numpy()
        pred_labels = [labels_map[i] for i in preds]

        for i in labels_map.values():
            text_classified[i] = ''
        
        for label, line in zip(pred_labels, sentences):
            text_classified[label] = text_classified[label] + ' ' + line

        return text_classified


