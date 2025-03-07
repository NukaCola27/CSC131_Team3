package grading;

public class Grade implements Comparable<Grade> {
	// Attributes
	private String key;
	private java.lang.Double value;
	
	// Constructors
	public Grade(String key) throws IllegalArgumentException {
		if (key == null || key.isEmpty()) {
			throw new IllegalArgumentException("The key cannot be null or empty");
		}
		this.key = key;
		this.value = null; // No argument passed for value
	}
	
	public Grade(String key, double value) throws IllegalArgumentException {
		if (key == null || key.isEmpty()) {
			throw new IllegalArgumentException("The key cannot be null or empty");
		}
		this.key = key;
		this.value = value;
	}
	
	public Grade(String key, java.lang.Double value) throws IllegalArgumentException {
		if (key == null || key.isEmpty()) {
			throw new IllegalArgumentException("The key cannot be null or empty");
		}
		this.key = key;
		this.value = value;
	}
	
	// Public Methods
	public String getKey() {
		return this.key;
	}
	
	public java.lang.Double getValue() {
		return this.value;
	}
	
	// Call compareTo from within Grade first then built in compareTo
	@Override
	public int compareTo(Grade other) {
		return this.value.compareTo(other.value);
	}
	
	public String toString() {
		return key + ": " + (value != null ? value : "No grade was assigned");
	}
}
