#!/usr/bin/env python

from midiutil import MIDIFile

P_ORF_10 = "data/ORF10_protein_QIB84681_1"
P_ORF3a = "data/ORF3a_protein_QIB84674_1"
P_ORF6 = "data/ORF6_protein_QIB85677_1"
P_ORF7a = "data/ORF7a_protein_QIB84678_1"
P_ORF8 = "data/ORF8_protein_QIB84679_1"
P_ENVELOPE = "data/envelope_protein_QIB84675_1"
P_MEMBRANE_GLYCO = "data/membrane_glycoprotein_QIB84676_1"
P_NUCLEOCAPSID_PHOSPHO = "nucleocapsid_phosphoprotein_QIB84680_1"
P_ORFLAB = "data/orflab_polyprotein_QIB84672_1"
P_SURFACE_GLYCO = "data/surface_glycoprotein_QIB84673_1"

degrees  = [60, 62, 64, 65, 67, 69, 71, 72] # MIDI note number
track    = 0
channel  = 0
time     = 0   # In beats
duration = 1   # In beats
tempo    = 60  # In BPM
volume   = 100 # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
                     # automatically created)
MyMIDI.addTempo(track, time, tempo)

def parseProtein(proteinFilePath):
  with open(proteinFilePath) as f:
    while True:
      c = f.read(1)
      if not c:
        print "End of file"
        break
      parseCharacter(c)

def parseCharacter(character):
  ##TODO
  print "Parse: ", character

parseProtein(P_ORF_10)

#for pitch in degrees:
#    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
#    time = time + 1
#
#with open("test.mid", "wb") as output_file:
#    MyMIDI.writeFile(output_file)
