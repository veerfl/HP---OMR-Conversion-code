import re
import sys
import csv
list1 = []
list2 = []
list3 = []

f = open("SET6.dat", "rb")   #INPUT file
wr = csv.writer(open("P2_zone_1.csv", "wb")) # output file
wr.writerow(["Bar_code","you_are","Date","udise_code","num_students","num_girls","num_boys","num_CWSN","num_rooms_used","num_teachers","num_special_edu","vacant_posts","unattended_class","drinking_water","electricity"\
	,"playground","seperate_toilets","clean_toilets","kitchen_separate","ICT_facility","Rural_urban"\
	,"CO1: class_taught","CO1: class_observed","CO1:Q_encouraged","CO1:Q_answered","CO1: activity","CO1: uses_blackboard","CO1: trained","CO1: TLM_use","CO1: ABL_performs","CO1: CCE_checklist_use","CO1: lesson_plan","CO1: assessment_sheet","CO1:student_intrest","CO1: teaching_quality","CO1: PMIS_code"\
	,"CO2: class_taught","CO2: class_observed","CO2:Q_encouraged","CO2:Q_answered","CO2: activity","CO2: uses_blackboard","CO2: trained","CO2: TLM_use","CO2: ABL_performs","CO2: CCE_checklist_use","CO2: lesson_plan","CO2: assessment_sheet","CO2:student_intrest","CO2: teaching_quality","CO2: PMIS_code"\
	,"CO3: class_taught","CO3: class_observed","CO3:Q_encouraged","CO3:Q_answered","CO3: activity","CO3: uses_blackboard","CO3: trained","CO3: TLM_use","CO3: ABL_performs","CO3: CCE_checklist_use","CO3: lesson_plan","CO3: assessment_sheet","CO3:student_intrest","CO3: teaching_quality","CO3: PMIS_code"\
	,"CO4: class_taught","CO4: class_observed","CO4:Q_encouraged","CO4:Q_answered","CO4: activity","CO4: uses_blackboard","CO4: trained","CO4: TLM_use","CO4: ABL_performs","CO4: CCE_checklist_use","CO4: lesson_plan","CO4: assessment_sheet","CO4:student_intrest","CO4: teaching_quality","CO4: PMIS_code"\
	,"overall_quality","comm_parent_participation","teacher_admin","attendance_register","aadhaar_attendance","SMC_meeting","SDP_complete","VER_maintained","braille_books","RTE_compliant","CCE_evaluation","report_card","RMSA_portal","civil_work_pending","activity_calendar","bal_sabha"\
	,"SC_inclusion","ST_inclusion","CWSN_inclusion","class3_students","class3_Hindi_A","class3_Hindi_B","class3_Hindi_C","class3_Hindi_D","class3_Hindi_E","class3_Math_A","class3_Math_B","class3_Math_C","class3_Math_D","class3_Math_E","class5_students","class5_Hindi_A","class5_Hindi_B","class5_Hindi_C"\
	,"class5_Hindi_D","class5_Hindi_E","class5_Math_A","class5_Math_B","class5_Math_C","class5_Math_D","class5_Math_E","class8_students","class8_Science_A","class8_Science_B","class8_Science_C","class8_Science_D","class8_Science_E","class8_Math_A","class8_Math_B","class8_Math_C"\
	,"class8_Math_D","class8_Math_E","G1_amt_received","G1_amt_spent","G2_amt_received","G2_amt_spent","G3_amt_received","G3_amt_spent"])

for lines in f.readlines():
	lines = lines.strip()
	x = len(lines)
	if x > 0:
		Sheet =lines[1:50]
		Bar_code = lines[40:46]
		you_are = lines[50:51]
		Date = lines[51:57]
		u_dise = lines[57:68]
		Num_students = lines[68:71]
		Num_girls = lines[71:74]
		Num_boys = lines[74:77]
		Num_CWSN = lines[77:79] 
		Num_rooms_used = lines[79:81]
		Num_teachers = lines[81:83]
		Num_special_edu = lines[83:85]
		Num_vacent_teacher_post = lines[85:86]
		Num_unattended_class = lines[86:87]
		Drinking_water_facility = lines[87:88]
		Electricity = lines[88:89]
		playground= lines[89:90]
		seperate_toilets = lines[90:91]
		School_toilets_clean = lines[91:92]
		Seperate_kitchen = lines[92:93]
		ICT_facility = lines[93:94]
		Rural_urban = lines[94:95]
		which_class_1 = lines[95:96]
		Classroom_observed= lines[96:97]
		Q_encouraged = lines[97:98]
		QA_satisfied = lines[98:99]
		Activity_class = lines[99:100]
		Use_blackboard = lines[100:101]
		Trained_in_last_12 =lines[101:102]
		Use_TLM = lines[102:103]
		Performs_ABL = lines[103:104]
		CCE_checklist = lines[104:105]
		has_lesson_pln = lines[105:106]
		Assessment_sheet = lines[106:107]
		student_intrest_class = lines[107:108]
		Teaching_quality = lines[108:109]
		Teachers_PMIS = lines[109:114]
		which_class_2 = lines[114:115]
		Classroom_observed_2 = lines[115:116]
		Q_encouraged_2 = lines[116:117]
		QA_satisfied_2 = lines[117:118]
		Activity_class_2 = lines[118:119]
		Use_blackboard_2 = lines[119:120]
		Trained_in_last_12_2 =lines[120:121]
		Use_TLM_2 = lines[121:122]
		Performs_ABL_2 = lines[122:123]
		CCE_checklist_2 = lines[123:124]
		has_lesson_pln_2 = lines[124:125]
		Assessment_sheet_2 = lines[125:126]
		student_intrest_class_2 = lines[126:127]
		Teaching_quality_2 = lines[127:128]
		Teachers_PMIS_2 = lines[128:133]
		which_class_3 = lines[133:134]
		Classroom_observed_3 = lines[134:135]
		Q_encouraged_3 = lines[135:136]
		QA_satisfied_3 = lines[136:137]
		Activity_class_3 = lines[137:138]
		Use_blackboard_3 = lines[138:139]
		Trained_in_last_12_3 =lines[139:140]
		Use_TLM_3 = lines[140:141]
		Performs_ABL_3 = lines[141:142]
		CCE_checklist_3 = lines[142:143]
		has_lesson_pln_3 = lines[143:144]
		Assessment_sheet_3 = lines[144:145]
		student_intrest_class_3 = lines[145:146]
		Teaching_quality_3 = lines[146:147]
		Teachers_PMIS_3 = lines[147:152]
		which_class_4 = lines[152:153]
		Classroom_observed_4 = lines[153:154]
		Q_encouraged_4 = lines[154:155]
		QA_satisfied_4 = lines[155:156]
		Activity_class_4 = lines[156:157]
		Use_blackboard_4 = lines[157:158]
		Trained_in_last_12_4 =lines[158:159]
		Use_TLM_4 = lines[159:160]
		Performs_ABL_4 = lines[160:161]
		CCE_checklist_4 = lines[161:162]
		has_lesson_pln_4 = lines[162:163]
		Assessment_sheet_4 = lines[163:164]
		student_intrest_class_4 = lines[164:165]
		Teaching_quality_4 = lines[165:166]
		Teachers_PMIS_4 = lines[166:171]
		Rate_overall_quality = lines[171:172]
		parent_community = lines[172:173]
		teacher_deliver_admin_work = lines[173:174]
		Attendance_register = lines[174:175]
		Aadhaar = lines[175:176]
		SMC_meeting = lines[176:177]
		complete_SDP = lines[177:178]
		VER_maintained = lines[178:179]
		braille_books = lines[179:180]
		RTE = lines[180:181]
		evaluation_CCE = lines [181:182]
		report_card_maintained = lines[182:183]
		RMSA_portal = lines[183:184]
		civil_work = lines[184:185]
		calender_activity = lines[185:186]
		Bal_sabha = lines[186:187]
		SC = lines[187:188]
		ST = lines[188:189]
		CWSN = lines[189:190]
		no_students_class3 = lines[190:192]
		GradeA_hindi = lines [192:194]
		GradeB_hindi = lines [194:196]
		GradeC_hindi = lines [196:198]
		GradeD_hindi = lines [198:200]
		GradeE_hindi = lines [200:202]
		GradeA_Math = lines [202:204]
		GradeB_Math = lines [204:206]
		GradeC_Math = lines [206:208]
		GradeD_Math = lines [208:210]
		GradeE_Math = lines [210:212]
		no_students_class5 = lines[212:214]
		GradeA_hindi_5 = lines [214:216]
		GradeB_hindi_5 = lines [216:218]
		GradeC_hindi_5 = lines [218:220]
		GradeD_hindi_5 = lines [220:222]
		GradeE_hindi_5 = lines [222:224]
		GradeA_Math_5 = lines [224:226]
		GradeB_Math_5 = lines [226:228]
		GradeC_Math_5 = lines [228:230]
		GradeD_Math_5 = lines [230:232]
		GradeE_Math_5 = lines [232:234]
		no_students_class8 = lines[234:236]
		GradeA_science_8 = lines [236:238]
		GradeB_science_8 = lines [238:240]
		GradeC_science_8 = lines [240:242]
		GradeD_science_8 = lines [242:244]
		GradeE_science_8 = lines [244:246]
		GradeA_Math_8 = lines [246:248]
		GradeB_Math_8 = lines [248:250]
		GradeC_Math_8 = lines [250:252]
		GradeD_Math_8 = lines [252:254]
		GradeE_Math_8 = lines [254:256]
		G1_amt_received = lines [256:259]
		G1_amt_spent = lines [259:262]
		G2_amt_received = lines[262:265]
		G2_amt_spent = lines[265:268]
		G3_amt_received = lines [268:271]
		G3_amt_spent = lines[271:274]
		 

		
		
		
		out=([Bar_code,you_are,Date,u_dise,Num_students,Num_girls,Num_boys,Num_CWSN,Num_rooms_used,Num_teachers,Num_special_edu,Num_vacent_teacher_post,Num_unattended_class,Drinking_water_facility,Electricity\
			,playground,seperate_toilets,School_toilets_clean,Seperate_kitchen,ICT_facility,Rural_urban,which_class_1,Classroom_observed,QA_satisfied,Q_encouraged,Activity_class,Use_blackboard,Trained_in_last_12\
			,Use_TLM,Performs_ABL,CCE_checklist,has_lesson_pln,Assessment_sheet,student_intrest_class,Teaching_quality,Teachers_PMIS\
			,which_class_2,Classroom_observed_2,Q_encouraged_2,QA_satisfied_2,Activity_class_2,Use_blackboard_2,Trained_in_last_12_2,Use_TLM_2,Performs_ABL_2,CCE_checklist_2,has_lesson_pln_2,Assessment_sheet_2,student_intrest_class_2,Teaching_quality_2,Teachers_PMIS_2\
			,which_class_3,Classroom_observed_3,Q_encouraged_3,QA_satisfied_3,Activity_class_3,Use_blackboard_3,Trained_in_last_12_3,Use_TLM_3,Performs_ABL_3,CCE_checklist_3,has_lesson_pln_3,Assessment_sheet_3,student_intrest_class_3,Teaching_quality_3,Teachers_PMIS_3\
			,which_class_4,Classroom_observed_4,Q_encouraged_4,QA_satisfied_4,Activity_class_4,Use_blackboard_4,Trained_in_last_12_4,Use_TLM_4,Performs_ABL_4,CCE_checklist_4,has_lesson_pln_4,Assessment_sheet_4,student_intrest_class_4,Teaching_quality_4,Teachers_PMIS_4\
			,Rate_overall_quality,parent_community,teacher_deliver_admin_work,Attendance_register,Aadhaar,SMC_meeting,complete_SDP,VER_maintained,braille_books,RTE,evaluation_CCE,report_card_maintained,RMSA_portal,civil_work,calender_activity,Bal_sabha,SC,ST,CWSN\
			,no_students_class3,GradeA_hindi,GradeB_hindi,GradeC_hindi,GradeD_hindi,GradeE_hindi,GradeA_Math,GradeB_Math,GradeC_Math,GradeD_Math,GradeE_Math\
			,no_students_class5,GradeA_hindi_5,GradeB_hindi_5,GradeC_hindi_5,GradeD_hindi_5,GradeE_hindi_5,GradeA_Math_5,GradeB_Math_5,GradeC_Math_5,GradeD_Math_5,GradeE_Math_5\
			,no_students_class8,GradeA_science_8,GradeB_science_8,GradeC_science_8,GradeD_science_8,GradeE_science_8,GradeA_Math_8,GradeB_Math_8,GradeC_Math_8,GradeD_Math_8,GradeE_Math_8\
			,G1_amt_received,G1_amt_spent,G2_amt_received,G2_amt_spent,G3_amt_received,G3_amt_spent])


		print(out)
		wr.writerow(out)
		


		
			


			



 
