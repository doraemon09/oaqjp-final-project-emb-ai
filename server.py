from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

#
@app.route("/emotionDetector")

def sent_analyzer():
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        response_output = "Invalid text! Please try again!"
    else:
        response_output = "For the given statement, the system response is "
        response_output = response_output + "'anger:'" + str(response['anger'])
        response_output = response_output + ", 'disgust:'" + str(response['disgust'])
        response_output = response_output + ", 'fear:'" + str(response['fear'])
        response_output = response_output + ", 'joy:'" + str(response['joy'])
        response_output = response_output + ", and 'sadness:'" + str(response['sadness'])
        response_output = response_output + ". The dominant emotion is '" + response['dominant_emotion']
        response_output = response_output + "."

    return response_output

#
@app.route("/")

def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)