# See https://stackoverflow.com/q/75063300/553865

from music21 import *
import os
from pathlib import Path

def new_filename(corpus_name, pitch_name, major_minor, filetype):
    name = Path(corpus_name).stem
    if major_minor == 'minor':
      m = 'm'
    else:
      m = ''
    return f'{name}.in_{pitch_name}{m}.{filetype}'

def new_title(corpus_name, pitch_name, major_minor):
    name = Path(corpus_name).stem
    if major_minor == 'minor':
      m = 'm'
    else:
      m = ''
    return f'{name} in {pitch_name}{m}'

paths = corpus.getComposer('bach')
score = corpus.parse('bach/bwv114.7.mxl')
key_guessed = score.analyze('key') # <music21.key.Key of g minor>

if key_guessed.type == 'minor':
    target_pitch = pitch.Pitch('A') # <music21.pitch.Pitch A>
else:
    target_pitch = pitch.Pitch('C') # <music21.pitch.Pitch C>
if target_pitch.name != key_guessed.tonic.name: # 'A' != 'G'
    interval_desired = interval.Interval(key_guessed.tonic, target_pitch)
    transposed_score = score.transpose(interval_desired)
    new_key = transposed_score.analyze('key')
    transposed_score.metadata.title = new_title(score.corpusFilepath, target_pitch.name, key_guessed.type)

    filename = new_filename(score.corpusFilepath, target_pitch.name, key_guessed.type, 'mid')
    transposed_score.write('midi', filename)
