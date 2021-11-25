import os
import spacy
import codecs
import random

from model.AnswerExtract import AnswerExtract
from model.DataRetrieval import DataRetrieval
from flask import Flask, render_template, jsonify, request

from model.UrlCompare import UrlCompare

app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())




@app.route('/chatbot', methods=["GET", "POST"])

def analyzer():
    spacy_model = os.environ.get('HOME', 'en_core_web_sm')
    nlp = spacy.load(spacy_model, disable=['ner', 'parser', 'textcat'])
    passage_retriever = DataRetrieval(nlp)

    qa_model = os.environ.get('QA_MODEL', 'distilbert-base-cased-distilled-squad')
    answer_extractor = AnswerExtract(qa_model, qa_model)
    greeting_inputs = (
        "hello", "hi", "good morning", "good afternoon", "good evening", "greetings", "sup", "what's up", "hey",)
    greeting_responses = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"]
    goodbye_inputs = ("bye", "see you later", "goodbye", "ok bye", "bye bye")
    goodbye_responses = ["See you soon!", "Have a nice day", "Sure Bye", "See you later"]
    name_inputs = (
        "what is your name", "whats your name", "tell me your name", "who are you", "tell me about yourself")
    name_responses = ["I am IIT assistant", "My name is IIT ", "you can call me IIT"]
    thanks_inputs = ("thanks", "thank you", "that's helpful", "awesome, thanks", "thanks for helping me")
    thanks_responses = ["Happy to help!", "no problem ", "You are welcome"]

    with open("textextract/important_links.txt", "r+", encoding='utf-8') as data:

        contents = data.readlines()
    n = len(contents)
    ob = UrlCompare()
    count = 0

    if (request.method == 'POST'):
        question = request.form['question']
        while (count != 23):
            for i in range(0, n):
                if (ob.compare(question.lower(), contents[i])) >= 3:
                    return jsonify({"link": contents[i]})
                else:
                    count += 1

        if (question.lower() in greeting_inputs):
            return jsonify({'greetings': random.choice(greeting_responses)})
        elif (question.lower() in name_inputs):
            return jsonify({'names': random.choice(name_responses)})
        elif (question.lower() in goodbye_inputs):
            return jsonify({'bye': random.choice(goodbye_responses)})


        elif (question.lower() in thanks_inputs):
            return jsonify({'thanks': random.choice(thanks_responses)})
        else:
            doc = codecs.open('books/english.txt.', 'r', 'UTF-8').read()
            passage_retriever.fit(doc)
            passages = passage_retriever.most_similar(question)
            answers = answer_extractor.extract(question, passages)
            print(answers)
            return jsonify({'answer': answers})

    else:
        return render_template('index.html')





if __name__ == '__main__':
    app.run()