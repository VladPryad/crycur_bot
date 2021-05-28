from google.cloud import speech
import os
import requests
import config
from query_builder import queryBuilder
import audio_metadata

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config.GOOGLE_APPLICATION_CREDENTIALS

def nlp(file):

    url = file['file_path']

    r = requests.get(url, allow_redirects=True)

    id = file['file_unique_id'];
    path = f"{id}.ogg";

    open(path, 'wb').write(r.content);
    tag = audio_metadata.load(path);
    os.remove(path)

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(content = r.content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.OGG_OPUS,
        sample_rate_hertz=tag.streaminfo['source_sample_rate'],
        language_code="ru-RU",
    )

    response = client.recognize(config=config, audio=audio)
    isEmpty = response.results == []

    if(isEmpty):
        return "Can`t hear you"

    text = response.results[0].alternatives[0].transcript
    confidence = response.results[0].alternatives[0].confidence

    if(confidence < 0.5):
        return "What?"

    return queryBuilder(text)