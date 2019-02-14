import time

StartTime = time.time()

# Input
# TO-DO: Change to read XLSX files
RawAnswers = "10,8,6,9,10,8,10,7,10,9,10,10,8,10,0,5,9,10,9,7,7,10,9,10,2,8,10,9,0,7,10,9,10,10,5,9,8,9,8,5,10,10,10,10,10,5,10,10,5,9,10,9,10,7,10,9,7,7,10,4,10,10,10,6,9,8,6,10,3,9,10,10,5,3,8,5,9,5,8,5,7,10,5,4,7,10,5,0,5,8,10,9,10,8,10,10,4,8,10,7,5,5,8,9,8,9,10,0,10,10"
Answers = RawAnswers.split(",")

# Checks if any list answers are invalid
def validateAnswers(answers):

	for a in answers:

		if a.isdigit() == False:
			return False
		
		answer = int(a);

		if answer < 0 or answer > 10:
			return False

	return True

# Checks if an answer is in the given range
def checkAnswer(answer, min, max):

	IntAnswer = int(answer)

	return IntAnswer >= min and IntAnswer <= max

# Filter answers that are in a given range
def filterTotalAnswers(answers, min, max):

	return len(list(filter(lambda answer: checkAnswer(answer, min, max), answers)))

# Get percent value
def getPercent(value, total):

	return (value / total) * 100

# Get NPS zone
def getZone(nps):

	if nps > 75 and nps <= 100:

		return "Excellence"
	elif nps > 50 and nps <= 75:

		return "Quality"

	elif nps > 0 and nps <= 50:

		return "Improvement"
	else:

		return "Critical"

if validateAnswers(Answers) == False:

	print("There are some invalid answer values in your input. Please check!");
else:

	TotalAnswers = len(Answers)
	TotalDetractors = filterTotalAnswers(Answers, 0, 6)
	TotalPassives = filterTotalAnswers(Answers, 7, 8)
	TotalPromoters = filterTotalAnswers(Answers, 9, 10)

	PercentDetractors = getPercent(TotalDetractors, TotalAnswers)
	PercentPassives = getPercent(TotalPassives, TotalAnswers)
	PercentPromoters = getPercent(TotalPromoters, TotalAnswers)

	NPS = int(PercentPromoters - PercentDetractors)
	Zone = getZone(NPS)

	print("\n|--------------|")
	print("|  PYTHON NPS  |")
	print("|--------------|\n")
	print("Total answers: {}\n".format(TotalAnswers))
	print("Detractors: {} ({}%)".format(TotalDetractors, round(PercentDetractors, 2)))
	print("Passives: {} ({}%)".format(TotalPassives, round(PercentPassives, 2)))
	print("Promoters: {} ({}%)\n".format(TotalPromoters, round(PercentPromoters, 2)))
	print("YOUR NPS: {}\n".format(NPS))
	print("You are at [{}] Zone.\n".format(Zone))
	print("Result given in {} sec.\n".format(round(time.time() - StartTime, 5)))