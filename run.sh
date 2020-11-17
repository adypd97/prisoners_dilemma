#!/bin/bash

# Run multiple simulations with various combinations of strategies, interaction
# probabilities and iterations

strategies=("tft" "all_D" "majority_seeker" "randomer" "alt" "trusting_fool")

# For w = 0.99, n = 100
#for choice_1 in "${strategies[@]}"; do
#	for choice_2 in "${strategies[@]}"; do
#		echo -e "\n ${choice_1}  vs ${choice_2}"
#		./axelrod.py --s1="${choice_1}" --s2="${choice_2}" --n=100
#	done
#done

# For w = 0.99, n = 200

for choice_1 in "${strategies[@]}"; do
	for choice_2 in "${strategies[@]}"; do
		echo -e "\n ${choice_1}  vs ${choice_2}"
		./axelrod.py --s1="${choice_1}" --s2="${choice_2}" --n=200
	done
done
