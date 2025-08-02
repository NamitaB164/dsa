//Count Negatives in a Sorted Matrix

/*
Solve this problem with a complexity less than m+n.

Read the following input: an integer n representing the number of rows in the matrix, and an integer m representing the number of columns in the matrix and the values of the matrix (n rows and m columns).

The matrix is sorted such that all elements in any row are sorted in increasing order from left to right, and all elements in any column are sorted in increasing order from top to bottom. You should print the total number of negative numbers present in the matrix.

The input will be provided as follows:

    The first line of input contains a single integer n, the number of rows in the matrix.
    The second line of input contains a single integer m, the number of columns in the matrix.
    The next n lines each contain m integers separated by spaces, representing the elements of the matrix.

Solve this problem with a complexity less than m+n.

Input Format

3
4
-4 -3 -1 1
-2 -2 1 3
-1 1 2 4

Constraints

    The number of rows n and columns m will not exceed 100.
    Each row and column of the matrix is sorted in non-decreasing order.
    Matrix elements are integers.

Output Format

6. */

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int rows,cols,c=0;
    scanf("%d",&rows);scanf("%d",&cols);
    int mat[rows][cols];
    for (int i=0;i<rows;i++){
        for (int j=0;j<cols;j++){
            scanf("%d",&mat[i][j]);
        }
    }
    int j=cols-1; int i=0;
    while (j>=0 && i<rows){
        if (mat[i][j]<0){
            c+=j+1;
            i+=1;
        }
        else{
            j-=1;
        }
            
        }
    
            
        
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    printf("%d",c);
    return 0;
}
