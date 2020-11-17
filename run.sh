#!/bin/bash

# Run multiple simulations with various combinations of strategies, interaction
# probabilities and iterations

# For w = 0.99, n = 100
echo -e "TFT vs TFT "
./axelrod.py --s1=tft --s2=tft --show=True
echo -e "\nAll D vs TFT"
./axelrod.py --s1=all_D --s2=tft --show=True
echo -e "\nAlternate vs TFT "
./axelrod.py --s1=alt --s2=tft --show=True

