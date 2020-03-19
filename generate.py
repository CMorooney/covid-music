#!/usr/bin/env python

from midiutil import MIDIFile

P_ORF_10 = "data/ORF10_protein_QIB84681_1"
P_ORF3a = "data/ORF3a_protein_QIB84674_1"
P_ORF6 = "data/ORF6_protein_QIB85677_1"
P_ORF7a = "data/ORF7a_protein_QIB84678_1"
P_ORF8 = "data/ORF8_protein_QIB84679_1"
P_ENVELOPE = "data/envelope_protein_QIB84675_1"
P_MEMBRANE_GLYCO = "data/membrane_glycoprotein_QIB84676_1"
P_NUCLEOCAPSID_PHOSPHO = "data/nucleocapsid_phosphoprotein_QIB84680_1"
P_ORFLAB = "data/orflab_polyprotein_QIB84672_1"
P_SURFACE_GLYCO = "data/surface_glycoprotein_QIB84673_1"

#middle-c to b
notes = { 'c':60, 'c#':61, 'd':62, 'd#':63, 'e':64, 'f':65, 'f#':66, 'g':67, 'g#':68, 'a':69, 'a#':70, 'b':71 }
rGroups = ['A', 'C', 'D', 'E', 'F','G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

fMinor = [notes['f'], notes['g'], notes['g#'], notes['a#'], notes['c'], notes['c#'], notes['d#']]
drums = [ 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47 ]

sequencerTrack    = 0
drumTrack = 1
channel  = 0
time     = 0   # In beats
duration = .5   # In quarter beats
tempo    = 145  # In BPM
volume   = 100 # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(2) # One track, defaults to format 1 (tempo track
                     # automatically created)
MyMIDI.addTempo(sequencerTrack, time, tempo)
MyMIDI.addTempo(drumTrack, time, tempo)

def parseProtein(proteinFilePath):
  with open(proteinFilePath) as f:
    while True:
      c = f.read(1)
      if not c or c.isspace():
        print "End of file"
        writeFile()
        break
      parseCharacter(c)

def parseCharacter(character):
  writeNote(character, fMinor)

def writeNote(rGroup, scale):
  index = rGroups.index(rGroup)

  note = 0
  drum = 0 

  scaleLength = len(scale)
  drumLength = len(drums)

  if(index < scaleLength):
    note = fMinor[index]    
  else:
    note = fMinor[index % scaleLength]

  if(index < drumLength):
    drum = drums[index]
  else:
    drum = drums[index % drumLength]

  MyMIDI.addNote(sequencerTrack, channel, note, time, duration, volume) 
  MyMIDI.addNote(drumTrack, channel, drum, time, duration, volume) 

  global time
  time = time + .5 

def writeFile():
  with open("test.mid", "wb") as output_file:
   MyMIDI.writeFile(output_file)

parseProtein(P_NUCLEOCAPSID_PHOSPHO)