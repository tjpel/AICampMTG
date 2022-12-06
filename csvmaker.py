import pandas as pd
import scrython, time

salt = {'Stasis':2.92, 'Winter Orb':2.91, 'Static Orb':2.71, 'Vorinclex, Voice of Hunger':2.60, 'Expropriate': 2.52, 'Armageddon': 2.47, "Thassa's Oracle": 2.43,
        'Jokulhaups': 2.4, 'Obliterate': 2.39, 'Devastation':2.39, 'Ravages of War': 2.37, 'Jin-Gitaxias, Core Augur':2.34, 'Urza, Lord High Artificer':2.32,
        'Dockside Extortionist':2.32, 'Cyclonic Rift':2.32, 'The Tabernacle at Pendrell Vale':2.32, 'Sunder':2.31, 'Rhystic Study':2.25, 'Decree of Annihilation':2.21,
        'Fierce Guardianship':2.21, 'Humility':2.2, 'Apocalypse':2.16, 'Smokestack':2.14, 'Mindslaver':2.11, 'Smothering Tithe':2.11, 'Hokori, Dust Drinker':2.29,
        'Rising Waters':2.08, 'Time Stretch':2.05, 'Drannith Magistrate':2.03, "Gaea's Cradle":2.03, 'Grand Arbiter Augustin IV':2.29, 'Blightsteel Colossus':1.96,
        'Opposition Agent': 1.95, 'Narset, Parter of Veils':1.94, 'Back to Basics':1.94, 'Nexus of Fate':1.93, 'Emrakul, the Promised End':1.93, 'Nether Void':1.92,
        'Blood Moon':1.91, 'Void Winnower':1.87, 'Sen Triplets':1.87, 'Jin-Gitaxias, Progress Tyrant':1.86, 'Tectonic Break':1.86, 'Oko, Thief of Crowns':1.84,
        "Thieves' Auction":1.83, 'Scrambleverse':1.83, 'Wake of Destruction':1.81, 'Teferi, Time Raveler':1.81, 'Ruination':1.8, 'Overwhelming Splendor':1.80,
        'Force of Will':1.79, 'Narset, Enlightened Master':1.79, 'Omniscience':1.78, 'Mana Vortex':1.78, 'Impending Disaster':1.78, 'Epicenter':1.77, 'Global Ruin':1.77,
        'Warp World':1.77, 'Mana Breach':1.75, 'Consecrated Sphinx':1.73, 'Edgar Markov':1.73, 'Jeweled Lotus':1.73, 'Time Warp':1.72, 'Elesh Norn, Grand Cenobite':1.71,
        'Mana Drain':1.71, 'Boil':1.71, 'Demonic Consultation':1.7, 'Craterhoof Behemoth':1.7, 'Korvold, Fae-Cursed King':1.7, 'Cataclysm':1.69, 
        'Ulamog, the Infinite Gyre': 1.69, 'Force of Negation':1.69, 'Gilded Drake':1.68, 'Ulamog, the Ceaseless Hunger':1.67, 'Divine Intervention':1.66, 'Mana Crypt':1.66,
        'Possessed Portal':1.65, "Gaddock Teeg":1.64, "Smoke":1.64, 'Chulane, Teller of Tales': 1.64, 'Contamination': 1.63, 'Catastrophe': 1.63, 'Embargo': 1.62, 
        'Temporal Manipulation': 1.62, 'Acid Rain': 1.61, 'Worldpurge': 1.61, 'Flashfires': 1.6, "Yuriko, the Tiger's Shadow": 1.6, 'Thoughts of Ruin': 1.6,
        'Fall of the Thran': 1.6, 'Triumph of the Hordes': 1.59, 'Oppression': 1.59, 'Agent of Treachery': 1.59, 'Torment of Hailfire': 1.58, 'Keldon Firebombers': 1.58,
        'Choke': 1.57, 'Temporal Mastery': 1.57, "Atraxa, Praetor's Voice": 1.57, 'Notion Thief': 1.56}

checkCL = lambda ci : ['CL'] if ci == [] else ci
checkMC = lambda ci : ['MC'] if len(ci) > 1 else ci

names = []
scores = []
cmc = []
ci = []
price = []
type = []
date = []
setCode = []

for key in salt:
    card = scrython.Named(exact = key)
    time.sleep(0.075)

    names.append(key) #add name
    scores.append(salt[key]) #add salt score
    cmc.append(card.cmc()) #add converted mana cost
    ci.append(checkMC(checkCL(card.color_identity()))) #add color identity -- MC for multicolored, CL for colorless
    price.append(card.prices("usd")) #add price
    type.append(card.type_line()) #add type line
    date.append(card.released_at()) #add initial release date
    setCode.append(card.set_name()) #add initial set code

df = pd.DataFrame(data = {'name': names, 'score': scores, 'cmc': cmc, 'colorid': ci, 'price': price, 'type': type, 'date': date, 'set': setCode})
df.to_csv("./top100salt.csv")

print("Done")