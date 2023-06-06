import os
import json
from transformers import pipeline
from datasets import Dataset, Audio
import torch

def load_magnets_dataset():
    path = './data'
    wavfiles = [os.path.join(path, 'magnets16K.wav')]
    audio_dataset = Dataset.from_dict({"audio": wavfiles }).cast_column("audio", Audio())
    return audio_dataset

ds = load_magnets_dataset()
sample = ds[0]["audio"]
device = "cuda:0" if torch.cuda.device_count() > 0 else "cpu"

transcriptions = []

pipe = pipeline(
  "automatic-speech-recognition",
  model="openai/whisper-large",
  chunk_length_s=30,
  device=device
)

txt = pipe(sample.copy(), batch_size=8)["text"]

with open('output.txt','w') as f:
    f.write(txt)