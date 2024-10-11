import requests
import json

# Emotion Predict | Watson NLP Library
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    myobj = {"raw_document": {"text": text_to_analyse}}
    
    response = requests.post(url, json = myobj, headers=header)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)

        emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

        dominant_score = 0
        dominant_emotion = None
        
        for emotion, score in emotion_scores.items():
            if score > dominant_score:
                dominant_score = score
                dominant_emotion = emotion

        emotion_response = emotion_scores

        emotion_response['dominant_emotion'] = dominant_emotion
    else:
        emotion_response = { 'anger':None, 'disgust':None, 'fear':None, 'joy':None, 'sadness':None, 'dominant_emotion':None}

    return emotion_response
