def compute_score(judge_scores, *penalties):
    highest = max(judge_scores)
    judge_scores.remove(highest)
    lowest = min(judge_scores)
    judge_scores.remove(lowest)

    sums = sum(judge_scores)
    penalty = sum(penalties)

    score = sums - penalty
    
    return score


"""
Given an array of judge scores and optional penalties, 
calculate the final score for a figure skating routine.

The first argument is an array of 10 judge scores, each a number from 0 to 10. 
Remove the highest and lowest judge scores and sum the remaining 8 scores to get the base score.

Any additional arguments passed to the function are penalties. 
Subtract all penalties from the base score to get the final score.
"""