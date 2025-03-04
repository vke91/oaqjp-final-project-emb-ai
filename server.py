from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    output = emotion_detector(text_to_analyze)

    anger = output['anger']
    disgust = output['disgust']
    fear = output['fear']
    joy = output['joy']
    sadness = output['sadness']
    dom_emotion = output['dominant_emotion']

    if dom_emotion is None:
        return "Invalid text! Please try again!"

    formatted_output = f"For the given statement, the system response is 'anger': {anger} , 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dom_emotion}."

    return formatted_output

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000'''
    app.run(host="0.0.0.0", port=8080)
    