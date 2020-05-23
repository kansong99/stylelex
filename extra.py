import spacy

nlp = spacy.load("en_core_web_md")
doc = nlp("Kofi was born in Manchester, Connecticut today.")

States = "Alabama Alaska Arizona Arkansas California Colorado Connecticut\
DelawareFloridaGeorgiaHawaiiIdahoIllinoisIndianaIowaKansasKentuckyLouisiana\
MaineMarylandMassachusettsMichiganMinnesotaMississippiMissouriMontanaNebraska\
NevadaNew HampshireNew JerseyNew MexicoNew YorkNorth CarolinaNorth DakotaOhio\
OklahomaOregonPennsylvaniaRhode IslandSouth CarolinaSouth DakotaTennesseeTexas\
UtahVermontVirginiaWashingtonWest VirginiaWisconsinWyoming"
count = len(doc.ents)
run = 0
prev = None
for ent in doc.ents:
	if run > 0:
		if prev == 'GPE' and ent.label_ == 'GPE':
			if (ent.text not in States) or "." in ent.text or ent.text != 'UK' or len(ent.text) == 2:
				print("Spell states out in full.")
	run += 1
	prev = ent.label_


	### Consider adding comma check after states, perhaps making it a preference. ###