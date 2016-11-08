import csv

mega_a = []
mega_b = []
mega_c = []
Roll_no1 = ''
Roll_no2 = ''
p1_file = open("p_1.dat", "r")
c = csv.writer(open("P_con_fin.csv", "wb"))
c.writerow(["Sheet_id", "student_ID", "U_Dise","class code","Section code","Student Roll No","student sex","student Language","student Number","Q1","Q2","Q3","Q4","Sheet_id2","student_ID2","Starting day","Month","End Day","Month2","Q5a","Q5b","Q6a","Q6b","Q7a","Q7b","Q8a","Q8b","Q9a","Q9b","Q10a","Q10b","Q11","Q12","Q13","Q14","Q15a","Q15b"])

p1_lines = p1_file.readlines()
print("LINES : " + str(len(p1_lines)))
for p1_line in p1_lines:
	p1_line = p1_line.strip()
	p1_lineLenght = len(p1_line)

	if p1_lineLenght > 1:
		Sheet =p1_line[1:24]
		Sheet_id = p1_line[39:46]
		U_Dise = p1_line[46:57]
		class_code = p1_line[57:58]
		Section_code = p1_line[58:59]
		Roll_no1 = p1_line[59:84]
		Roll_no2 = p1_line[84:109] 
		sex = p1_line[109:134]
		Language = p1_line[134:159]
		Number = p1_line[159:184]
		Q1 = p1_line[184:209]
		Q2 = p1_line[209:234]
		Q3 = p1_line[234:259]
		Q4 = p1_line[259:284]

		for j in range(0,25):
			student_ID = j+1
			print len(Roll_no1)
			print len(Roll_no2)
			student_roll_no = Roll_no1[j] + Roll_no2[j]
			student_sex = sex[j]
			student_Language = Language[j]
			student_Number = Number[j]
			student_Q1 = Q1[j]
			student_Q2 = Q2[j]
			student_Q3 = Q3[j]
			student_Q4 = Q4[j]
			a=([Sheet_id, student_ID, U_Dise,class_code,Section_code,student_roll_no,student_sex,student_Language,student_Number,student_Q1,student_Q2,student_Q3,student_Q4])
			mega_a.append(a)
			#print(a)


p2_file = open("p_2.dat", "r")
for p2_line in p2_file.readlines():
	p2_line = p2_line.strip()
	p2_line_lenght = len(p2_line)
	if p2_line_lenght > 0:
		Bar_code2 =p2_line[39:46]
		Starting_day = p2_line[50:52]
		Month = p2_line[52:53]
		End_Day = p2_line[53:55]
		Month2 = p2_line[55:56]
		Q5a = p2_line[56:81]
		Q5b = p2_line[81:106]
		Q6a = p2_line[106:131] 
		Q6b = p2_line[131:156]
		Q7a = p2_line[156:181]
		Q7b = p2_line[181:206]
		Q8a = p2_line[206:231]
		Q8b = p2_line[231:256]
		Q9a = p2_line[256:281]
		Q9b = p2_line[281:306]
		Q10a = p2_line[306:331]
		Q10b = p2_line[331:356]
		Q11 = p2_line[356:381]
		Q12 = p2_line[381:406]
		Q13 = p2_line[406:431]
		Q14 = p2_line[431:456]
		Q15a = p2_line[456:481]
		Q15b = p2_line[481:506]
			
																		
		for y in range(0,25):
			student_ID2 = y+1
			#print("y : " + str(y))
			#print("Q5 : " + str(len(Q5a)))
			student_Q5a = Q5a[y]
			student_Q5b = Q5b[y]
			student_Q6a = Q6a[y]
			student_Q6b = Q6b[y]
			student_Q7a = Q7a[y]
			student_Q7b = Q7b[y]
			student_Q8a = Q8a[y]
			student_Q8b = Q8b[y]
			student_Q9a = Q9a[y]
			student_Q9b = Q9b[y]
			student_Q10a = Q10a[y]
			student_Q10b = Q10b[y]
			student_Q11 = Q11[y]
			student_Q12 = Q12[y]
			student_Q13 = Q13[y]
			student_Q14 = Q14[y]
			student_Q15a = Q15a[y]
			student_Q15b = Q15b[y]

			b=([Bar_code2,student_ID2,Starting_day,Month,End_Day,Month2,student_Q5a,student_Q5b,student_Q6a,student_Q6b,student_Q7a,student_Q7b,student_Q8a,student_Q8b,student_Q9a,student_Q9b,student_Q10a,student_Q10b,student_Q11,student_Q12,student_Q13,student_Q14,student_Q15a,student_Q15b])
			mega_b.append(b)
						

print(len(mega_a))
print(len(mega_b))
for i in mega_a:
	''
	#print(i)

for i in range(0,len(mega_a)):
	
	#mega_a[i].extend(mega_b[i])
	#mega_c.append(mega_a[i] + mega_b[i])
	#print mega_c
	m = mega_a[i] + mega_b[i]	
	print(m)																			
	c.writerows([m])
				
