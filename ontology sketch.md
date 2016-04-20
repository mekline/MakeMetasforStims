#Ontology Sketch

##Stimulus types
() - top level

Movie

Audio

Picture

Linguistic - “this was made for ling purposes”

EventMovie

Sentence

##Set level properties

####() [All Sets]

string Filetype

string Citation (doi)

string Creator (person responsible)

string Contact email

list Stimulus Types <- Creator may not provide all dependencies, we should be able to reconstruct

list ItemVersions - If each item in a set has multiple versions (e.g. sad, happy, angry of actor 1, actor 2, and so on), list them here

####Linguistic

string Language 

string Kind (sentence, word, passage)

string Modality (spoken, written)

####EventMovie

list Participants - unique names for everything you define as a participant (Actor1, Actor2, beanbag, box, chair1, chair2)

list Roles - Thematic role list that you use {Agent, Patient, Recipient}

##Item level properties

####()

int ItemNo - Item number

string ItemVersion - if your set has multiple versions of the same item, which one is this?

####Movie

float Length

pair Size (h,w)

####Audio
float Length

####Picture

string Color (bw or color?)

pair Size (h,w)

####EventMovie

string PrimaryVerbDescription - the label the experimenter gave to the scene

list PrimarySentenceDescription - the sentences the experimenter used to describe the scene in the experiment

list VerboseDescription - Require 3 or more sentences with different verbs about what is happening (e.g. The girl throws the ball, the ball flies, the girl moves her arm)

int NParticipants - how many participants are there?

list ParticipantIDs - Unique id for each (should have length = NParticipants) e.g. {Actor1, chair}

list ParticipantRoles - Role of each of the participants e.g. {Agent, Patient}

list ParticipantIsAnimate - Boolean list NParticipants long

Intentional/Unintentional?

Typical/Novel?

Completed/Incompleted?
