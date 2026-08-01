import random
from time import sleep
import heapq

teams=["A", "B", "C", "D", "E", "F", "G", "H","I", "J"]
group1=random.sample(teams, 5)
group2=random.sample([team for team in teams if team not in group1], 5)
semi_finalists=[]
d=[0]*5
y=[0]*5
points_23=[0]*5
points_12=[0]*5

for i in range(5):
        winner=random.choice([group1[i], group2[i]])
        points_1=3 if winner==group1[i] else 0
        d[i]=points_1
        points_23[i]+=points_1
        points_2=3 if winner==group2[i] else 0
        y[i]=points_2
        points_12[i]+=points_2
        print(f"Group 1: {group1[i]} vs Group 2: {group2[i]} -> Winner: {winner} (Points: {d[i], y[i]})\n")
        sleep(1.3)
    
semi_finalists_1=heapq.nlargest(2, group1)
semi_finalists_2=heapq.nlargest(2, group2)
semi_finalists=semi_finalists_1+semi_finalists_2
print(f"Semi-Finalists: {semi_finalists}\n")
sleep(1.3)

finalists_1=random.choice(semi_finalists)
finalists_2=random.choice([team for team in semi_finalists if team!=finalists_1])
final_winner=random.choice([finalists_1, finalists_2])
print(f"Final: {finalists_1} vs {finalists_2} -> Winner: {final_winner}\n")


