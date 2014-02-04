This is the README file for A0091539X's submission

== General Notes about this assignment ==

I followed mostly the method that was described in the assignment and slides with the following modifications:
1. When building the model, I stored the log() of the probabilities and added them in the predicting step since the floats were too small to multiply (ended up 0.0 before)

2. I normalized the probabilities depending on the number of ngrams found in the data set since this allows me to set a decent threshold for 'other' languages.

3. I arrived at a threshold for 'other' by running my code against the training data and taking a little less than the minimum of the scores of the predicted language of all lines (-9.63598066008, so I made the threshold as 10.0)

4. I also assigned a very small number as a start to each line's probabilities so that if no ngrams in the line were found in the LM, it would be lower than the threshold.

== Files included with this submission ==

build_test_LM.py => Main source code
run.sh => shell script to run my code and test it against the test data provided.
README.txt => Text file that describes all information about my submission
ESSAY.txt => Text file with answers to the essay questions

== Statement of individual work ==

Please initial one of the following statements.

[X] I, U000000X, certify that I have followed the CS 3245 Information
Retrieval class guidelines for homework assignments.  In particular, I
expressly vow that I have followed the Facebook rule in discussing
with others in doing the assignment and did not take notes (digital or
printed) from the discussions.

[ ] I, U000000X, did not follow the class rules regarding homework
assignment, because of the following reason:

<Please fill in>

I suggest that I should be graded as follows:

<Please fill in>

== References ==

<Please list any websites and/or people you consulted with for this
assignment and state their role>
