import os
import json
#from transformers import WhisperProcessor, WhisperForConditionalGeneration, pipeline
from transformers import pipeline
from datasets import Dataset, Audio

def load_magnets_dataset():
    path = './data'
    wavfiles = [os.path.join(path, 'magnets16K.wav')]
    audio_dataset = Dataset.from_dict({"audio": wavfiles }).cast_column("audio", Audio())
    return audio_dataset

# load model and processor
#processor = WhisperProcessor.from_pretrained("openai/whisper-large")
#model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large")
#model.config.forced_decoder_ids = None

# load dummy dataset and read audio files
ds = load_magnets_dataset()
sample = ds[0]["audio"]

transcriptions = []

pipe = pipeline(
  "automatic-speech-recognition",
  model="openai/whisper-large",
  chunk_length_s=30,
  device="cpu"
)
'''
for d in ds: 
    sample = d["audio"]
    input_features = processor(sample["array"], sampling_rate=sample["sampling_rate"], return_tensors="pt").input_features 
    # generate token ids
    predicted_ids = model.generate(input_features)
    # decode token ids to text
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
    transcriptions = transcriptions +  transcription

with open('output.txt','w') as f:
    txt = " ".join(transcriptions)
    f.write(txt)

'''
txt = pipe(sample.copy(), batch_size=8)["text"]

with open('output.txt','w') as f:
    f.write(txt)