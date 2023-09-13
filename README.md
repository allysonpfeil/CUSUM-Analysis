# Dunn's Analysis
Perform a posthoc Dunn's Analysis on five groups containing five variables each.

In this example, we have been given five cohorts of data, each containing five variables. The actual data has been redacted; fill in with whatever data you so choose.
Briefly, the data should be non-parametric, and previously validated as statistically variable by a Kruskal-Wallis test. The Kruskal-Wallis test will output whether or not the data is statistically variant, but it will not indicate which groups have variance. Thus, the posthoc Dunn's test is needed to determine where the variance lies. 

For context, this project is analyzing where the variance lies following P < .05 results from a Kruskal-Wallis test. The groups are the five stages of robotic knee surgery and are as follows:
  1. Exposure
  2. Pin Placement
  3. Registration
  4. Robotic Bone Cuts
  5. Trials
Inside these groups are time data that corresponds to how long each stage took place. This analysis sought to identify any time change over the course of implementing a new robot to perform the surgery. In other words, the time data corresponds to the learning curve that the surgeon experienced while acclimating to the new device.

The time data was grouped into cohorts of five patients and their time data, so as to minimize variance while also being realistic. So, we can establish that inside each surgical stage (exposure, pin placement, registration, robotic bone cuts, trials) exists five, chronological groups that house the time data. Here is an example:
  1. Exposure group 1 (patients 1-5)
  2. Exposure group 2 (patients 6-10)
  3. Exposure group 3 (patients 11-15)
  4. Exposure group 4 (patients 16-20)
  5. Exposure group 5 (patients 21-25)

Simply add the time data in question to the main.py and plug in. 
Now, let's go over how to interpret the results. The print should look something like this:

#EXPOSURE
      #1    2    3    4         5
#1.  1.000000  1.0  1.0  1.0  0.515612
#2.  1.000000  1.0  1.0  1.0  1.000000
#3.  1.000000  1.0  1.0  1.0  1.000000
#4.  1.000000  1.0  1.0  1.0  1.000000
#5.  0.515612  1.0  1.0  1.0  1.000000

This outputs a matrix containing the P values of the all-versus-all comparison. For this exposure stage, none of the stages experienced a statistically significant time change, since none of the P values in the matrix are < .05. Thus, the variance did not lie within the exposure stage of robotic surgery. When reading this matrix, use the row value to correspond to a column value. For instance, the value in row #1 and column #1 means "The P value from the comparison of exposure group 1 to exposure group 1." Obviously, this will output a statistically equivocal P value. As another example, the value in row #5 and column #1 means "The P value from the comparison of exposure group 1 to exposure group 5." Notice that the value in row 5 col 1 is the same as row 1 col 5. This is because the same comparison is being made: group 1 to group 5. These groups are interchangable and will output the same P value. 
