import java.util.Scanner;
import java.net.URL;
import java.net.URLConnection;
import java.io.InputStream;
import java.io.IOException;
public class userRunner {
	public static double[] getCoordinates(String url){
		try {
			double[] coordinates = new double[2];
			URL website = new URL(url);
			InputStream in = website.openStream();
			Scanner sc = new Scanner(in);
			while(sc.hasNextLine()) {
				String current = sc.nextLine();
				if(current.contains("location")) {
					break;
				}
			}
			String lat = sc.nextLine();
			lat = lat.substring(23,lat.length()-1);
			System.out.println(lat);
			String lng = sc.nextLine();
			lng = lng.substring(23);
			coordinates[0] = Double.parseDouble(lat);
			coordinates[1] = Double.parseDouble(lng);
			in.close();
			return coordinates;
		} catch (IOException e) {
			System.out.println(e.getMessage());
		}
		return null;
	}
	public static void main(String[] args) {
		Scanner userIn = new Scanner(System.in);
		System.out.println("Enter your current address: ");
		String currentAddress = userIn.nextLine();
		System.out.println("Enter you destination address: ");
		String destinationAddress = userIn.nextLine();
		currentAddress = currentAddress.replace(' ', '+');
		String currentAddressURL = "https://maps.googleapis.com/maps/api/geocode/json?address=" + currentAddress + "&key=AIzaSyCdaPXmz8jQexyn-kWR9rmiumUuLn3GgMs";
		destinationAddress = destinationAddress.replace(' ', '+');
		String destinationAddressURL = "https://maps.googleapis.com/maps/api/geocode/json?address=" + destinationAddress + "&key=AIzaSyCdaPXmz8jQexyn-kWR9rmiumUuLn3GgMs";
		double[] currentCoordinates = getCoordinates(currentAddressURL);
		double[] destinationCoordinates = getCoordinates(destinationAddressURL);
		System.out.println("Coordinates are " + currentCoordinates[1] + destinationCoordinates[0]);
	}
}