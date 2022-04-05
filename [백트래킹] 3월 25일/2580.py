import sys # readline 사용을 위해 sys 불러옴
input = sys.stdin.readline # 사용하기 용이하게 input으로 바꿈

"""
 가지치기 효율: 80ms
 9X9의 스도쿠에서 각 행, 열, 3x3 사각형에 1~9가 존재하는지 체크하는 2차원 배열 활용
 각 2차원 배열의 행: 어느 부분에 대한 체크인지(행, 열, 3x3), 0번 인덱스부터 시작
 각 2차원 배열의 열: 1 ~ 9 숫자 체크
 행과 열은 바로 사용하면 됨
 (ex) check_row[3][2] = true;  //3행에 2라는 숫자가 존재한다는 것
      check_col[8][9] = false; //8열에 9라는 숫자가 존재하지 않는다는 것
 3x3 사각형 (하나를 각 구역이라고 표현)
 -> 행을 3으로 나눈 몫과 열을 3으로 나눈 몫으로 구역 0부터 8까지 다음과 같이 나타낼 수 있음
 (0,0) (0,1) (0,2)
 (1,0) (1,1) (1,2)
 (2,0) (2,1) (2,2)
 -> 1차원 배열 인덱스로 구분하기 위해 각 (행 / 3)값에 3을 곱한 후 (열 / 3)을 더함
 -> 따라서 3x3 사각형의 구간은 (row / 3) * 3 + (col / 3) = 0 ~ 8인 구간으로 나눌 수 있음
"""

SIZE = 9    # 스도쿠 한 행 사이즈
check_row = [[False] * (SIZE + 1) for _ in range(SIZE)]     # 각 행의 숫자 존재 여부 체크
check_col = [[False] * (SIZE + 1) for _ in range(SIZE)]     # 각 열의 숫자 존재 여부 체크
check_3x3 = [[False] * (SIZE + 1) for _ in range(SIZE)]     # 각 3x3 사각형의 숫자 존재 여부 체크

def calc_area(x, y): # 1차원 배열 인덱스로 구분하기 위한 함수
    return (x // 3) * 3 + y // 3

def fill_sudoku(cnt): # 스도쿠 채우기 함수
    if cnt == SIZE * SIZE: # 입력받은 값이 SIZE의 제곱과 같다면
        return True # True값 반환
    
    x, y = cnt // SIZE, cnt % SIZE # x와 y는 각각 cnt를 SIZE값으로 나눈 몫과 SIZE로 나눈 나머지

    if sudoku[x][y] > 0:    # 이미 숫자가 채워진 칸이면 
        return fill_sudoku(cnt + 1) #다음 칸 값을 리턴

    for i in range(1, SIZE + 1):    # 1~9까지 넣어보기
        if check_row[x][i] or check_col[y][i] or check_3x3[calc_area(x, y)][i]: # check_row, check_col, check_3x3값 중 하나가 True라면
            continue # 넘어가서 뒷 연산을 계속함

        check_row[x][i] = True # 윗줄에서 True인지 False인지 판단한 배열들에
        check_col[y][i] = True # True값 대입함
        check_3x3[calc_area(x, y)][i] = True # 이후로 sudoku[x][y]값에
        sudoku[x][y] = i # i를 넣어줌

        if fill_sudoku(cnt + 1):    # fill_sudoku(cnt + 1)의 값이 들어있다면
            return True # True 반환해줌

        check_row[x][i] = False # 앞에서는 True값을 넣어주었던 배열에
        check_col[y][i] = False # False값 대입해줌
        check_3x3[calc_area(x, y)][i] = False # 이후 i였던 sudoku[x][y]값을
        sudoku[x][y] = 0 # 0으로 변경해줌. 

    return False # False값 리턴

sudoku = [list(map(int, input().split())) for _ in range(SIZE)] #스도쿠 값 입력받아서 sudoku 변수에 저장

# 스도쿠 상태 표시
for i in range(SIZE): # SIZE동안
    for j in range(SIZE): # SIZE동안22
        if sudoku[i][j] == 0: # sudoku[i][j]값이 0이라면
            continue # 다음 코드 계속 진행함
        check_row[i][sudoku[i][j]] = True # [i]행에 [sudoku[i][j]] 숫자 존재
        check_col[j][sudoku[i][j]] = True # [j]열에 [sudoku[i][j]] 숫자 존재
        check_3x3[calc_area(i, j)][sudoku[i][j]] = True # [calc_area(i, j)][sudoku[i][j]] 칸에 숫자 존재

fill_sudoku(0) # 연산

# 출력
for line in sudoku: # sudoku의 원소를
    print(*line)    # 하나씩 풀어서 print()에 인자로 넣어줌
               
