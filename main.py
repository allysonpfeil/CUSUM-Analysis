#VELYS Re-Analysis by Allyson Pfeil

#import libraries required
import scikit_posthocs as sp

###EXPOSURE###
#specify the EXPOSURE TIME for each group of five patients
exgroup1 = [insert time data here] #patients 1-5
exgroup2 = [insert time data here] #patients 6-10
exgroup3 = [insert time data here] #patients 11-15
exgroup4 = [insert time data here] #patients 16-20
exgroup5 = [insert time data here] #patients 21-25
exposure_data = [exgroup1, exgroup2, exgroup3, exgroup4, exgroup5]
exposure_results = sp.posthoc_dunn(exposure_data, p_adjust='bonferroni')
print("EXPOSURE")
print(exposure_results)

###PIN PLACEMENT###
#specify the PIN PLACEMENT for each group of five patients
pingroup1 = [insert time data here] #patients 1-5
pingroup2 = [insert time data here] #patients 6-10
pingroup3 = [insert time data here] #patients 11-15
pingroup4 = [insert time data here] #patients 16-20
pingroup5 = [insert time data here] #patients 21-25
pin_data = [pingroup1, pingroup2, pingroup3, pingroup4, pingroup5]
pin_results = sp.posthoc_dunn(pin_data, p_adjust='bonferroni')
print("PIN PLACEMENT")
print(pin_results)

###REGISTRATION###
#specify the REGISTRATION for each group of five patients
reggroup1 = [insert time data here] #patients 1-5
reggroup2 = [insert time data here] #patients 6-10
reggroup3 = [insert time data here] #patients 11-15
reggroup4 = [insert time data here] #patients 16-20
reggroup5 = [insert time data here] #patients 21-25
reg_data = [reggroup1, reggroup2, reggroup3, reggroup4, reggroup5]
reg_results = sp.posthoc_dunn(reg_data, p_adjust='bonferroni')
print("REGISTRATION")
print(reg_results)

###ROBOTIC BONE CUTS###
#specify the ROBOTIC BONE CUTS for each group of five patients
robgroup1 = [insert time data here] #patients 1-5
robgroup2 = [insert time data here] #patients 6-10
robgroup3 = [insert time data here] #patients 11-15
robgroup4 = [insert time data here] #patients 16-20
robgroup5 = [insert time data here] #patients 21-25
rob_data = [robgroup1, robgroup2, robgroup3, robgroup4, robgroup5]
rob_results = sp.posthoc_dunn(rob_data, p_adjust='bonferroni')
print("ROBOTIC BONE CUTS")
print(rob_results)

###TRIALS###
#specify the TRIALS for each group of five patients
trygroup1 = [7, 8, 9, 12, 12] #patients 1-5
trygroup2 = [8, 7, 6, 8, 4] #patients 6-10
trygroup3 = [10, 10, 6, 7, 8] #patients 11-15
trygroup4 = [6, 9, 8, 6, 8] #patients 16-20
trygroup5 = [5, 7, 7, 7, 19] #patients 21-25
try_data = [trygroup1, trygroup2, trygroup3, trygroup4, trygroup5]
try_results = sp.posthoc_dunn(try_data, p_adjust='bonferroni')
print("TRIALS")
print(try_results)
###END OF CODE###

###OUTPUT###
        #C:\dev\opencv.test>python VELYS.py
        #EXPOSURE
                #1    2    3    4         5
        #1  1.000000  1.0  1.0  1.0  0.515612
        #2  1.000000  1.0  1.0  1.0  1.000000
        #3  1.000000  1.0  1.0  1.0  1.000000
        #4  1.000000  1.0  1.0  1.0  1.000000
        #5  0.515612  1.0  1.0  1.0  1.000000
        
        #PIN PLACEMENT
                #1         2         3         4         5
        #1  1.000000  1.000000  0.103509  0.003372  0.125669
        #2  1.000000  1.000000  1.000000  0.434519  1.000000
        #3  0.103509  1.000000  1.000000  1.000000  1.000000
        #4  0.003372  0.434519  1.000000  1.000000  1.000000
        #5  0.125669  1.000000  1.000000  1.000000  1.000000
        
        #REGISTRATION
                #1    2    3    4         5
        #1  1.000000  1.0  1.0  1.0  0.212676
        #2  1.000000  1.0  1.0  1.0  1.000000
        #3  1.000000  1.0  1.0  1.0  1.000000
        #4  1.000000  1.0  1.0  1.0  1.000000
        #5  0.212676  1.0  1.0  1.0  1.000000
        
        #ROBOTIC BONE CUTS
                #1         2        3         4         5
        #1  1.000000  0.201313  1.00000  0.008907  0.033677
        #2  0.201313  1.000000  1.00000  1.000000  1.000000
        #3  1.000000  1.000000  1.00000  0.559740  1.000000
        #4  0.008907  1.000000  0.55974  1.000000  1.000000
        #5  0.033677  1.000000  1.00000  1.000000  1.000000
        
        #TRIALS
                #1         2    3    4    5
        #1  1.000000  0.469262  1.0  1.0  1.0
        #2  0.469262  1.000000  1.0  1.0  1.0
        #3  1.000000  1.000000  1.0  1.0  1.0
        #4  1.000000  1.000000  1.0  1.0  1.0
        #5  1.000000  1.000000  1.0  1.0  1.0
