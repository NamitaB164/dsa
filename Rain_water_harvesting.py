#Rain water harvesting
'''Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
https://s3.amazonaws.com/hr-assets/0/1632670152-6a2401e17d-rainwatertrap.png
Eg : This elevation map is representative of the integers : [0,1,0,2,1,0,1,3,2,1,2,1]

    The blue regions represent the water stored.
    The black sections represent the various sections.

Input Format

    The first line of input contains a integer n representing the number of sections to the elevation map.
    The second line contains n separated positive integers representing the elevations of these sections

Constraints

0 <= n <= 10^5 0 <= height[i] <= 10^5

Output Format

    Output in a single line the amount of water that would be trapped in this elevation map if it were to be filled up.'''


n=int(input())
heights=[int(x) for x in input().split()]
r=l=0
maxL=[0]*n
maxR=[0]*n
for i in range(n):
    j=-i-1
    maxL[i]=l
    maxR[j]=r
    l=max(l,heights[i])
    r=max(r,heights[j])
wt=0
for i in range(n):
    h=min(maxL[i],maxR[i])
    wt+=max(0,h-heights[i])
print(wt)


