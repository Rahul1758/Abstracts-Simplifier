import streamlit as st
import tensorflow as tf
import tensorflow_text as text
from data_preprocess import preprocess_data

# Load the saved model
@st.cache(allow_output_mutation=True)
def load_model(path):
    model = tf.keras.models.load_model(path)
    return model
loaded_model = load_model('./saved_model')

def main():
    html_temp = """<div style="background-color:tomato;padding:10px">
                   <h2 style="color:white;text-align:center;">Abstract Simplifier</h2>
                   </div>"""
                   
    st.markdown(html_temp,unsafe_allow_html=True)
    input_text = st.text_input("Abstract text")
    if st.button('Simplify'):
        preprocessor = preprocess_data(input_text)
        line_numbers, total_lines, sentences = preprocessor.prepare_dataset()
        output_dict = preprocessor.get_predictions(line_numbers, total_lines, sentences, loaded_model)

        for label in ['BACKGROUND','OBJECTIVE','METHODS','RESULTS','CONCLUSIONS']:
            st.write('### {}\n'.format(label))
            st.write('{} \n'.format(output_dict[label]))

if __name__=='__main__':
    main()