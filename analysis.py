import matplotlib.pyplot as plt
from finaldata.getdata import getdata

allData = getdata()

x = ['Low Load', 'High Load', 'Degradaded Low Load']
y = []

listOfRT = [0, 0, 0]
listOfAllRT = []
counts = [0, 0, 0]

for data in allData:
	for d in data[5:]:
		if d[3] is not None and d[2].lower() == d[3][0]:
			if d[0] == 1 and d[1] == 1: # low load compatible
				listOfRT[0] += d[4]
				counts[0] += 1

			elif d[0] == 2 and d[1] == 1: # low load degradation compatible
				listOfRT[2] += d[4]
				counts[2] += 1

			elif d[0] == 3 and d[1] == 1: # high load compatible
				listOfRT[1] += d[4]
				counts[1] += 1

			listOfAllRT.append(d[4])

listOfMeanRT = []
print(listOfAllRT)

for i in range(len(counts)):
	listOfMeanRT.append(listOfRT[i] / counts[i])

compatibleConditionMean = sum(listOfMeanRT) / len(listOfMeanRT)

a = 0

for RT in listOfAllRT:
	a += (RT - compatibleConditionMean) ** 2

compatibleConditionSD = (a / len(listOfAllRT)) ** 0.5

y = listOfMeanRT
plt.plot(x, y)	

listOfRT = [0, 0, 0]
listOfAllRT = []
counts = [0, 0, 0]

for data in allData:
	for d in data[5:]:
		if d[3] is not None and d[2].lower() == d[3][0]:
			if d[0] == 1 and d[1] == 2: # low load incompatible
				listOfRT[0] += d[4]
				counts[0] += 1

			elif d[0] == 2 and d[1] == 2: # low load degradation incompatible
				listOfRT[2] += d[4]
				counts[2] += 1

			elif d[0] == 3 and d[1] == 2: # high load incompatible
				listOfRT[1] += d[4]
				counts[1] += 1

			listOfAllRT.append(d[4])

listOfMeanRT = []

for i in range(len(counts)):
	listOfMeanRT.append(listOfRT[i] / counts[i])

incompatibleConditionMean = sum(listOfMeanRT) / len(listOfMeanRT)

a = 0

for RT in listOfAllRT:
	a += (RT - incompatibleConditionMean) ** 2

incompatibleConditionSD = (a / len(listOfAllRT)) ** 0.5

y = listOfMeanRT
plt.plot(x, y)

listOfRT = [0, 0, 0]
listOfAllRT = []
counts = [0, 0, 0]

for data in allData:
	for d in data[5:]:
		if d[3] is not None and d[2].lower() == d[3][0]:
			if d[0] == 1 and d[1] == 3: # low load neutral
				listOfRT[0] += d[4]
				counts[0] += 1

			elif d[0] == 2 and d[1] == 3: # low load degradation neutral
				listOfRT[2] += d[4]
				counts[2] += 1

			elif d[0] == 3 and d[1] == 3: # high load neutral
				listOfRT[1] += d[4]
				counts[1] += 1

			listOfAllRT.append(d[4])

listOfMeanRT = []

for i in range(len(counts)):
	listOfMeanRT.append(listOfRT[i] / counts[i])

neutralConditionMean = sum(listOfMeanRT) / len(listOfMeanRT)

a = 0

for RT in listOfAllRT:
	a += (RT - neutralConditionMean) ** 2

neutralConditionSD = (a / len(listOfAllRT)) ** 0.5


y = listOfMeanRT
plt.plot(x, y)	
plt.legend(['Compatible', 'Incompatible', 'Neutral'])

# print(listOfRT)
# print(counts)
# print(listOfMeanRT)


plt.ylabel('Reaction time')
plt.show()

#################################################################

errorCount = [0, 0, 0]
notErrorCount = [0, 0, 0]
errorPercent = [0, 0, 0]

for data in allData:
	for d in data[:]:
		if d[3] is not None and d[2].lower() != d[3][0]:
			if d[0] == 1 and d[1] == 1: # low load compatible
				errorCount[0] += 1

			elif d[0] == 2 and d[1] == 1: # low load degradation compatible
				errorCount[2] += 1

			elif d[0] == 3 and d[1] == 1: # high load compatible
				errorCount[1] += 1
		elif d[3] is not None:
			if d[0] == 1 and d[1] == 1: # low load compatible
				notErrorCount[0] += 1

			elif d[0] == 2 and d[1] == 1: # low load degradation compatible
				notErrorCount[2] += 1

			elif d[0] == 3 and d[1] == 1: # high load compatible
				notErrorCount[1] += 1

y = []
for i in range(3):
	y.append((errorCount[i] * 100) / (errorCount[i] + notErrorCount[i]))

print(errorCount)
print(notErrorCount)
plt.plot(x, y)

errorCount = [0, 0, 0]
notErrorCount = [0, 0, 0]
errorPercent = [0, 0, 0]

for data in allData:
	for d in data[:]:
		if d[3] is not None and d[2].lower() != d[3][0]:
			if d[0] == 1 and d[1] == 2: # low load compatible
				errorCount[0] += 1

			elif d[0] == 2 and d[1] == 2: # low load degradation compatible
				errorCount[2] += 1

			elif d[0] == 3 and d[1] == 2: # high load incompatible
				errorCount[1] += 1
		elif d[3] is not None:
			if d[0] == 1 and d[1] == 2: # low load incompatible
				notErrorCount[0] += 1

			elif d[0] == 2 and d[1] == 2: # low load degradation incompatible
				notErrorCount[2] += 1

			elif d[0] == 3 and d[1] == 2: # high load incompatible
				notErrorCount[1] += 1

y = []
for i in range(3):
	y.append((errorCount[i] * 100) / (errorCount[i] + notErrorCount[i]))

print(errorCount)
print(notErrorCount)
plt.plot(x, y)

errorCount = [0, 0, 0]
notErrorCount = [0, 0, 0]
errorPercent = [0, 0, 0]

for data in allData:
	for d in data[:]:
		if d[3] is not None and d[2].lower() != d[3][0]:
			if d[0] == 1 and d[1] == 3: # low load neutral
				errorCount[0] += 1

			elif d[0] == 2 and d[1] == 3: # low load degradation neutral
				errorCount[2] += 1

			elif d[0] == 3 and d[1] == 3: # high load neutral
				errorCount[1] += 1
		elif d[3] is not None:
			if d[0] == 1 and d[1] == 3: # low load neutral
				notErrorCount[0] += 1

			elif d[0] == 2 and d[1] == 3: # low load degradation neutral
				notErrorCount[2] += 1

			elif d[0] == 3 and d[1] == 3: # high load neutral
				notErrorCount[1] += 1

y = []
for i in range(3):
	y.append((errorCount[i] * 100) / (errorCount[i] + notErrorCount[i]))

print(errorCount)
print(notErrorCount)
plt.plot(x, y)
plt.ylabel('Error %')
plt.legend(['Compatible', 'Incompatible', 'Neutral'])

plt.show()

#################################################################

x = ['Compatible', 'Incompatible', 'Neutral']
y = [compatibleConditionSD, incompatibleConditionSD, neutralConditionSD]
# plt.xticks(rotation =)
ax = plt.bar(x, y)
# plt.tight_layout()
plt.ylabel('Standard Deviation (in seconds)')
plt.xlabel('Conditions')
# plt.margins(x=0, y=0.02)

plt.show()

print(incompatibleConditionMean, compatibleConditionMean, neutralConditionMean)
print(incompatibleConditionSD, compatibleConditionSD, neutralConditionSD)