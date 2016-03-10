package random;

public class SpiralMatrix {
	int[][] matrix;
	int[] res;
	int elements;

	public int[] spiral(int[][] matrix, int x, int y) {
		this.matrix = matrix;
		this.elements = 0;
		int step = 1;
		
		int size = matrix.length * matrix[0].length;
		res = new int[size];
		
		int posX = x;
		int posY = y;
		add(posX, posY);
		while(elements < size) {
			// Move up
			for(int i=1; i<=step; i++) {
				posY--;
				add(posX, posY);
			}
			
			// Move Left
			for(int i=1; i<=step; i++) {
				posX--;
				add(posX, posY);
			}
			
			// Increment step length
			step++;
			
			// Move down
			for(int i=1; i<=step; i++) {
				posY++;
				add(posX, posY);
			}
			
			// Move right
			for(int i=1; i<=step; i++) {
				posX++;
				add(posX, posY);
			}
			
			// Increment step length
			step++;
		}
		
		return res;
	}


	public void add(int x, int y) {
		if(x < matrix.length && x >=0 && y <matrix[x].length && y >=0) {
			res[elements] = matrix[x][y];
			elements++;
		}
	}
}
