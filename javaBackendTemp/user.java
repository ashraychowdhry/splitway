import java.util.ArrayList;
public class user{
	private double[] currentCoordinates = new double[2];
	private double[] locationCoordinates = new double[2];
	private double arrivalTime;
	private double userData = new double[1][5];
	public static ArrayList<double[]> users = new ArrayList<double[]>;
	public user(double[] currentCoordinates, double[] locationCoordinates, double arrivalTime) {
		this.currentCoordinates = currentCoordinates;
		this.locationCoordinates = locationCoordinates;
		this.arrivalTime = arrivalTime;
		this.userData[0] = currentCoordinates[0];
		this.userData[1] = currentCoordinates[1];
		this.userData[2] = locationCoordinates[0];
		this.userData[3] = locationCoordinates[1];
		this.userData[4] = arrivalTime;
		users.add(userData);
	}
	public double[] getCurrentCoordinates() {
		return currentCoordinates;
	}
	public double[] getLocationCoordinates() {
		return locationCoordinates;
	}
}