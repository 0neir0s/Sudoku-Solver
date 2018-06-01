#----------------- Sudoku solver algorithm -----------------------------------

'''
  Find row, col of an unassigned cell
  If there is none, return true
  For digits from 1 to 9
    a) If there is no conflict for digit at row, col
        assign digit to row, col and recursively try fill in rest of grid
    b) If recursion successful, return true
    c) Else, remove digit and try another
  If all digits have been tried and nothing worked, return false
'''

#--------------- Helper functions -----------------------------------
def checkConflict(Input,position,digit):
	#----------- Check for conflicts if digit ia added in the position -------
	#--- a) Check for horizontal conflict
	hPosition = (position/9)*9
	checkList = Input[hPosition : hPosition + 9]
	if digit in checkList:	#---the horizontal straight line of position---
		return True
	#--- b) Check for vertical conflict
	vPosition = position % 9
	i = vPosition
	checkList = []
	while(i < 81):
		checkList.append(Input[i])
		i = i + 9
	if digit in checkList:
		return True
	#--- c) Check for box conflict
	boxPosition = (vPosition/3)*3 + (hPosition/27)*27 
	checkList = [Input[i] for i in [boxPosition,boxPosition+1,boxPosition+2,boxPosition+9,boxPosition+10, \
									boxPosition+11,boxPosition+18,boxPosition+19,boxPosition+20]]
	if digit in checkList:
		return True
	return False
	

#--------------- Main function -----------------------------------------
def Sudoku(Input):
	#----------- Find row, col of an unassigned cell -----------------
	#----------- If there is none, return true -----------------------
	if 0 not in Input:
		return True 
	position = Input.index(0)
	for digit in range(1,10):
	#--- a) If there is no conflict for digit at row, col assign digit to row, col and recursively try fill in rest of grid
		conflictFlag = checkConflict(Input,position,digit)
		if conflictFlag:
			continue
		Input[position] = digit
		status = Sudoku(Input)
	#--- b) If recursion successful, return true
		if status:
			return True
	#--- c) Else, remove digit and try another
		Input[position] = 0
	#--- If all digits have been tried and nothing worked, return false
	return False


#-------------- Checking the function ---------------------------------------
if __name__ == '__main__':
	Input = [3, 0, 6, 5, 0, 8, 4, 0, 0, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 8, 7, 0, 0, 0, 0, 3, 1, \
			 0, 0, 3, 0, 1, 0, 0, 8, 0, 9, 0, 0, 8, 6, 3, 0, 0, 5, 0, 5, 0, 0, 9, 0, 6, 0, 0, \
			 1, 3, 0, 0, 0, 0, 2, 5, 0, 0, 0, 0, 0, 0, 0, 0, 7, 4, 0, 0, 5, 2, 0, 6, 3, 0, 0]
	status = Sudoku(Input)
	if status:
		for i in range(0,9):
			print Input[i*9:i*9+9]