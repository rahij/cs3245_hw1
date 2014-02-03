python build_test_LM.py -b input.train.txt -t input.test.txt -o input.predict.txt
python eval.py input.predict.txt input.correct.txt