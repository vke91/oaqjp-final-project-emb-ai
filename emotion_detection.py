import requests, json

def emotion_detector(text_to_analyse):

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(URL, json = Input, headers=Headers)
    formatted_response = json.loads(response.text)

    emotion_data = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_data, key = emotion_data.get)

    output = {
        'anger': emotion_data['anger'],
        'disgust': emotion_data['disgust'],
        'fear': emotion_data['fear'],
        'joy': emotion_data['joy'],
        'sadness': emotion_data['sadness'],
        'dominant_emotion': dominant_emotion
    }

    return output