"""
    Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

#
@app.route("/emotionDetector")

def sent_analyzer():
    """
        This code receives the text from the HTML interface and 
        runs sentiment analysis over it using emotion_detector()
        function. The output returned shows the emotions and their 
        score for the provided text.
    """
    text_to_analyse = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        response_output = "Invalid text! Please try again!"
    else:
        response_output = "For the given statement, the system response is "
        response_output = response_output + "'anger': "
        response_output = response_output + str(response['anger'])
        response_output = response_output + ", 'disgust': "
        response_output = response_output + str(response['disgust'])
        response_output = response_output + ", 'fear': "
        response_output = response_output + str(response['fear'])
        response_output = response_output + ", 'joy': "
        response_output = response_output + str(response['joy'])
        response_output = response_output + ", and 'sadness': "
        response_output = response_output + str(response['sadness'])
        response_output = response_output + ". The dominant emotion is '"
        response_output = response_output + response['dominant_emotion']
        response_output = response_output + "."

    return response_output

#
@app.route("/")

def render_index_page():
    """
        This function initiates the rendering of the main application
        page over the Flask channel
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
