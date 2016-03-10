/** 
 * Check to see if a Sudoku int[][] is valid
 * 
 * Assumption: puzzle is 9x9 and contains only numbers from 1-9
 * 
**/

public class SudokuChecker {
	
	public static boolean isValid(int[][] sudoku) {
		boolean[] checker;

		// check rows
		for(int i=0; i<9; i++) {
			checker = new boolean[10];
			for(int j=0; j<9; j++) {
				if(checker[(sudoku[i][j])]) {
					return false;
				}
				checker[(sudoku[i][j])] = true;
			}
		}
		
		// check columns
		for(int j=0; j<9; j++) {
			checker = new boolean[10];
			for(int i=0; i<9; i++) {
				if(checker[(sudoku[i][j])]) {
					return false;
				}
				checker[(sudoku[i][j])] = true;
			}
		}

		// check boxes
		for(int i=0; i<6; i+=3) {
			for(int j=0; j<6; j+=3) {
				if(!checkBox(sudoku, i, j))
					return false;
			}
		}

		
		return true;
	}
	
	private static boolean checkBox(int[][] sudoku, int x, int y) {
		boolean[] checker = new boolean[10];
		
		for(int i=x; i<x+3; i++) {
			for(int j=y; j<y+3; j++) {
				if(checker[(sudoku[i][j])])
					return false;
				checker[sudoku[i][j]] = true;
			}
		}
		return true;
	}

}
