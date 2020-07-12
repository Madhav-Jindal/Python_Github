if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks=[]
    i=0
    sum=0.0
    av=0.0
    if query_name in student_marks:
        marks=student_marks[query_name]
        for i in range(3):
            print(marks)
            sum=sum+marks[i]
            print(sum)
            av=sum/3

    print(av)