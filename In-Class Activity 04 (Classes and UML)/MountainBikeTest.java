// Bicycle.java (Superclass) - Renamed to avoid file conflict, but keeping logic
class Bicycle {
    private int gear;
    private int speed;

    // Constructor
    public Bicycle(int gear, int speed) {
        this.gear = gear;
        this.speed = speed;
    }

    // Default toString for Bicycle
    @Override
    public String toString() {
        return "Gear: " + gear + ", Speed: " + speed;
    }
}

// MountainBike.java (Subclass) - Renamed to avoid file conflict
class MountainBike extends Bicycle {
    private int seatHeight;

    // Constructor
    public MountainBike(int gear, int speed, int seatHeight) {
        super(gear, speed); // Call the Bicycle constructor
        this.seatHeight = seatHeight;
    }

    // Method to update seatHeight
    public void setHeight(int newValue) {
        this.seatHeight = newValue;
    }

    // toString method as specified
    @Override
    public String toString() {
        return super.toString() + "\nSeat height: " + seatHeight;
    }
}

// Test.java (Test class) - Renamed to avoid file conflict
public class MountainBikeTest {
    public static void main(String[] args) {
        MountainBike mb = new MountainBike(3, 100, 25);
        System.out.println(mb.toString());
    }
}