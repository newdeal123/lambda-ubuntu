# Transformation audio from MusicXML
.musicxml 파일에서 MIDI를 생성하거나
 MIDI에서 wav, mp3로 전환

### Lambda handler:
1. s3에서 mid와 FluidSynth에 사용될 soundfont를 다운로드
2. mid에서 wav로 변환, 샘플레이트를 16000으로 변환하여 onsets_frames_transcription 모델이 사용된 lambda function 'extract-notes-by-time'에서 사용됨
3. wav에서 mp3변환, 용량을 축소
4. 변환된 wav와 mp3를 s3에 업로드


우분투 베이스의 aws 람다 이미지로 환경을 구성

## Environment
1. Music21
- `pip install music21==6.7.1`
2. FluidSynth(Midi2audio)
- `pip install midi2audio==0.1.1`
- `brew install fluidsynth`
3. Lame mp3 Encoder
- `sudo apt-get install -y lame==3.1`

## Usage

#### music21

In python:
```
from music21 import *
s = converter.parse("canon_in_d.xml")
s.write("midi", fp="ouput.mid")
```
In terminal:
`Midi2audio midi wav -g 1.0`

### FluidSynth(midi2audio)
```
from midi2audio import FluidSynth

fs = FluidSynth(sound_font='/tmp/Full Grand Piano.sf2',sample_rate=16000)
fs.midi_to_audio(local+'.mid',local+'.wav')
```

### Lame
`lame music.wav music.mp3`




