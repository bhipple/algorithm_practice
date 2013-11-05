public class LongestOverlap()
{

  public double longestOverlap(Range[] inputs) {
    	Arrays.sort(inputs);
    	int cur = 0;
    	double res = 0;
    	
    	while(cur < inputs.length) {
    		double rangeStart = inputs[cur].start;
    		double rangeEnd = inputs[cur].end;
    		
    		while(cur < inputs.length && inputs[cur].start < rangeEnd) {
    			rangeEnd = Math.max(rangeEnd, inputs[cur].end);
    			cur++;
    		}
    		
    		res = Math.max(res, rangeEnd - rangeStart);
    		cur++;
    	}
    
    	return res;
  }
  
  class Range implements Comparable
  {
  	public double start;
  	public double end;
  	
  	Range(double start, double end) {
  		this.start = start;
  		this.end = end;
  	}
  	
  	public int compareTo(Range other) {
  		return start - other.start;
  	}
  }
}
