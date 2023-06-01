# OpenAI Whisper Transcriber

## Introduction

This is a demo showing how to transcribe an .m4a audio file using [OpenAI Whisper](https://huggingface.co/docs/transformers/model_doc/whisper). 

[```whisper-large ```model card](https://huggingface.co/openai/whisper-large)

## Pre-requisites

* Ubuntu 20.04 LTS Focal
* ffmpeg 4.2.7

### Python 

* pytorch == 2.0.1
* transformers == 4.29.2

### Proxy usage

Please set ```REQUESTS_CA_BUNDLE``` according. E.g.

```
REQUESTS_CA_BUNDLE="/home/<user>/certs/cacert.pem"
```

See [requirements.txt](./requirements.txt)

## Preprocessing

The audio sample needs to be downsampled into 16kHz, and `.WAV` format. FFMPEG can be used as follows:

```
ffmpeg -i magnets.m4a -ar 16000 magnets16K.wav
```

## License

[Apache 2.0](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiP2pLD06H_AhXAd2wGHSX3BTUQFnoECAgQAQ&url=https%3A%2F%2Fwww.apache.org%2Flicenses%2FLICENSE-2.0&usg=AOvVaw0oAoArQLfDyX9tvE1z2_Ix)