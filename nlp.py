from google.cloud import speech
import os
import config
import requests
import io
from query_builder import queryBuilder

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config.GOOGLE_APPLICATION_CREDENTIALS

def nlp(file):

    url = file['file_path']

    r = requests.get(url, allow_redirects=True)

    id = file['file_unique_id']
    path = f'{id}.ogg'

    client = speech.SpeechClient()

    gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"

    #audio = speech.RecognitionAudio(uri=gcs_uri)
    audio = speech.RecognitionAudio(content = r.content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.OGG_OPUS,
        sample_rate_hertz=48000,
        language_code="ru-RU",
    )

    response = client.recognize(config=config, audio=audio)
    isEmpty = response.results == []

    if(isEmpty):
        return "Ничего не слышу"

    text = response.results[0].alternatives[0].transcript
    confidence = response.results[0].alternatives[0].confidence

    if(confidence < 0.7):
        return "Чего-чего?"

    return queryBuilder(text)