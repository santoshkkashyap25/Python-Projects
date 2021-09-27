# spiral trversing animation
import turtle
import random

turtle.bgcolor("black")
seurat=turtle.Turtle()
width=5
height=7
dot_distance=25
seurat.penup()
list_color=["red","yellow","blue","green","brown","orange","pink","grey","cyan"]

seurat.setpos(-250,250)


def spiral(m,n):
    k=0
    l=0
    f=0
    col=random.randint(0,8)
    seurat.color(list_color[col])
    while(k<m and l<n):
        if f==1:
            seurat.right(90)
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[k][i], end=" ")
        k+=1
        f=1
        seurat.right(90)
        col=random.randint(0,8)
        seurat.color(list_color[col])

        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[i][n-1],end=" ")
        n-=1
        seurat.right(90)
        
        col=random.randint(0,8)
        seurat.color(list_color[col])

        if k<m:
            for i in range(n-1,(l-1),-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[m-1][i],end=" ")
            m-=1
        seurat.right(90)
        col=random.randint(0,8)
        seurat.color(list_color[col])

        if l<n:
            for i in range(m-1,k-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[i][l],end=" ")
            l+=1
            
R=10
C=10         

spiral(R,C)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            