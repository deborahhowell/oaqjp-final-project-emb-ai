import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers=header)
    # Error handling
    if response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        de = None
    else:
        # Format the response as a json
        formatted_response = json.loads(response.text)
        # Get the scores and store as floats (they are already floats, no need to type-cast)
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
        #Find the dominant emotion
        scores = [anger_score,disgust_score,fear_score,joy_score,sadness_score]
        idx = scores.index(max(scores)) #Find the index of the max value
        em = ['anger','disgust','fear','joy','sadness' ]
        de = em[idx]
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': de
    }

# from EmotionDetection.emotion_detection import emotion_detector
# emotion_detector("I hate working long hours.")