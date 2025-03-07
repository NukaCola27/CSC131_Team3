package grading;

public class Missing {
    // Constant for missing value
    public static final double DEFAULT_MISSING_VALUE = 0.0;

    // If number null, return default missing value
    public static double doubleValue(Double number) {
        return (number != null) ? number : DEFAULT_MISSING_VALUE;
    }

    // Return custom missing value
    public static double doubleValue(Double number, double missingValue) {
        return (number != null) ? number : missingValue;
    }
}
