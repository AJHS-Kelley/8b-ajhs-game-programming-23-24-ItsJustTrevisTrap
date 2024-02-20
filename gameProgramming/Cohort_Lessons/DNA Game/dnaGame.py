# DNA Replication Game, Trevis Brown, v0.0

# Import Entire Modules -- Get the whole tool box.
import time, datetime

# Import Specific Methods -- Get the specific tool.
from random import choice 

# Store the DNA Bases
dnaBases = ["A", "T", "G", "C"]

# GAME FUNCTIONS
def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("Please enter a positive integer of bases to generate.\n"))
    dnaSequence = ""
    while basesGenerated < basesRequested:
      dnaSequence += choice(dnaBases)
      basesGenerated += 1
    return dnaSequence

def doTranscription(dnaSequence: str) -> tuple:
    
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You will now generate the RNA Sequence that would match.\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence.\n")
    rnaStart = time.time() #time.time() returns the number of seconds since 00:00:00 Jan 01, 1970
    rnaSequence = input("Please enter the matching RNA sequence. Leave no spaces! Then press enter.\n").upper()
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime)
    # Tuples are ORDERED -- you can refrence elements with the index.
    # Tuples are UNCHANGABLE -- you cannot add, modify, or delete after creating
    # Tuples CAN have duplicate values.

def verifySequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    if len(dnaSequence) != len(rnaSequence):
        print("The sequences are diffrent lengths and cannot match.\n")
        return isMatch
    for dnaBase, rnaBase in zip(dnaSequence, rnaSequence):
        if dnaBase == "A" and rnaBase == "U":
            isMatch = True
        elif dnaBase == "C" and rnaBase == "G":
            isMatch = True
        elif dnaBase == "G" and rnaBase == "C":
            isMatch = True
        elif dnaBase == "T" and rnaBase == "A":
            isMatch = True
        else:
            print("Unable to identify correct base so no match.\n")
    return isMatch

def calcScore(rnaSequence: str, rnaTime: float) -> int:
    score = 0
    if rnaTime < 1.0: #Fastest Time, Highest Score
        score += 1000000
    elif rnaTime < 5.0:
        score += 900000
    elif rnaTime < 15.0:
        score += 700000
    elif rnaTime < 25.0:
        score += 500000
    else: # Slowest time, Lowest Score
        score += 250000

    scoreMulti = 0.0
    if len("rnaSequence") >= 30: # Longest Sequence, Highest Multiplier
       scoreMulti = 4.2
    elif len("rnaSequence") >= 25:  # Longest Sequence, Highest Multiplier
       scoreMulti = 3.5
    elif len("rnaSequence") >= 20:  # Longest Sequence, Highest Multiplier
       scoreMulti = 2.8
    elif len("rnaSequence") >= 15:  # Longest Sequence, Highest Multiplier
       scoreMulti = 2.1
    elif len("rnaSequence") >= 5:  # Longest Sequence, Highest Multiplier
       scoreMulti = 1.0
    else: # Shortest Sequence, Lowest Multiplier
       scoreMulti = 0.5
    # Increase score, multiplier should be > 1.0
    # Decrease score, multiplier should be < 1.0
    score *= scoreMulti
    return score

def saveScore(dnaSequence: str, rnaSequence: str, rnaTime: float, score: int) -> None:
    playerName = input("What is your first Name?\n")
    lastName = input("What is your last Name?\n")
    fullName = playerName + " " + lastName

    fileName = "dnaReplicationScore" + fullName +".txt"
    saveData = open(fileName, "a")
    # File Modes
    # "x" mode -- CREATE FILE, IF FILE EXISTS, EXIT WITH ERROR
    # "w" mode -- CREATE FILE, IF FILE EXISTS, OVERWRITE IT
    # "a" mode -- CREATE FILE, IF FILE EXISTS, APPEND TO IT
    saveData.write(f"\nScore Generated: {datetime.datetime.now()}\n")
    saveData.write(f"Player: {fullName}\n")
    saveData.write(f"DNA Sequence: {dnaSequence}\nRNA Sequence: {rnaSequence}\n")
    saveData.write(f"Transcription Time: {rnaTime}\n")
    saveData.write(f"Score: {score}\n")
    saveData.close()



dna = genDNA()
rna = doTranscription(dna)
if verifySequence(dna, rna[0]):
    score = (calcScore(rna[0], rna[1]))
    saveScore(dna, rna[0], rna[1], score)






















