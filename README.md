# Gale-Shapley Stable Matching Algorithm

This repository contains an implementation of the Gale-Shapley Stable Matching Algorithm in Python.

## Description

The Gale-Shapley Stable Matching Algorithm addresses the Stable Matching Problem, which aims to find a stable matching between two sets of participants (e.g., men and women) based on their preference lists. In a stable matching, there is no incentive for any pair of participants to undermine the assignment by joint action.

Key characteristics of the stable matching problem include:
- Perfect matching: everyone is matched monogamously, with each man matched to exactly one woman, and vice versa.
- Stability: no unstable pairs exist in the matching, where an unstable pair consists of a man and a woman who prefer each other to their current partners.
- Incentive for eloping: unstable pairs could improve their situation by forming a pair outside of the assigned matching.

The Gale-Shapley algorithm efficiently finds a stable matching by iteratively proposing and accepting/rejecting proposals based on participants' preference lists.

## Implementation

The provided implementation of the Gale-Shapley Stable Matching Algorithm follows these steps:
1. Initialize all men and women as free.
2. While there is at least one free man:
   - Choose a free man.
   - Iterate through the man's preference list and propose to the highest-ranked woman to whom he hasn't proposed yet.
   - If the woman is free, engage the man and woman.
   - If the woman is already engaged, compare her preference between the current man and her current engagement. If she prefers the current man, break her current engagement and engage her with the current man.

## How to Use

To use this implementation of the Gale-Shapley Stable Matching Algorithm, follow these steps:
1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Open the `stable_matching.py` file in your preferred text editor or IDE.
4. Modify the preference lists for men and women as needed.
5. Run the `stable_matching.py` script.
6. The script will output the stable matching pairs.

# Requirements
python 3.x

## Example

Suppose we have the following preference lists for men and women:


``men_preferences = {
    'm1': ['w1', 'w2', 'w3'],
    'm2': ['w2', 'w1', 'w3'],
    'm3': ['w1', 'w2', 'w3']
}``

``women_preferences = {
    'w1': ['m1', 'm2', 'm3'],
    'w2': ['m3', 'm2', 'm1'],
    'w3': ['m1', 'm3', 'm2']
}``

returns the matching pairs by preferences
       
![Stable_Matching](https://github.com/kainoa7/Stable_Matching/assets/97155994/9b46948e-6184-448c-be71-5e9ecb2b7a98)




