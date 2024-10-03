''' Executing this function starts emotion detector on port 5000
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This function analyzes the text received over html
    and returns emotion scores
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    r1 = emotion_detector(text_to_analyze)
    if r1['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    w = (f"For the given statement, the system response is 'anger':{r1['anger']}," +
    f" 'disgust': {r1['disgust']}, 'fear': {r1['fear']}, 'joy': {r1['joy']} and " +
    f" 'sadness': {r1['sadness']}. The dominant emotion is {r1['dominant_emotion']}.")
    return w

@app.route("/")
def render_index_page():
    ''' This function renders the main application
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
