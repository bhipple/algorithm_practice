/** 
*  Calculate the angle of 2 hands on an analog clock for a given (hour, min) time.
**/

public class ClockAngle {

	public static int calcAngle(int hour, int min) {
		if(hour < 1 || hour > 12 || min < 0 || min > 60)
			return -1;

		int angle = Math.abs((6*min - (30*(hour) + min/2)));
		if(angle == 360)
			angle = 0;
		
		return angle;
	}
}
