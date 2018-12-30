public class Q47 {

    public int maxvalue(int[][] matrix){
        if (matrix == null || matrix.length == 0) return 0;

        int m=matrix.length-1, n=matrix[0].length-1;
        for (int i=m; i>=0; i--){
            for (int j=n; j>=0; j++){
                if (j==n && i==m) continue;
                if (j==n) matrix[i][j] = matrix[i+1][j];
                else if (i==m) matrix[i][j] = matrix[i][j+1];
                else matrix[i][j] += Math.max(matrix[i][j+1], matrix[i+1][j]);
            }
        }
        return matrix[0][0];
    }
}
