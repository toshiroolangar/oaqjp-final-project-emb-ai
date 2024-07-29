import requests
import json
import operator
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputjson = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = inputjson, headers=header)
    
    json_response = json.loads(response.text)
    json_response_dict = json_response['emotionPredictions'][0]['emotion']
    anger_score = json_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = json_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = json_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = json_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = json_response['emotionPredictions'][0]['emotion']['sadness']
    dominant_emotion, probability = max(json_response_dict.items(), key=operator.itemgetter(1))
    
    return {'anger' : anger_score,
            'disgust' : disgust_score,
            'fear' : fear_score,
            'joy' : joy_score,
            'sadness' : sadness_score,
            'dominant_emotion' : dominant_emotion
    }
    
    
