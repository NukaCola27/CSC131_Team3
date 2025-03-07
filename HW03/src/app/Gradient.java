/*
 * HW 03: Class Diagrams
 * Group Members: Mukesh Mehmi, Brandon Bradley, Saul Serrano, Kenjustin Yabut
 */

package app;
import grading.*;
import java.util.*;

public class Gradient {
    public static void main(String[] args) {
        // Create sample Grade objects
        List<Grade> grades = new ArrayList<>();
        grades.add(new Grade("CSC 133", 85.0));
        grades.add(new Grade("CSC 135", 90.0));
        grades.add(new Grade("CSC 139", 78.0));

        try {
            // Test DropFilter (Drop lowest grade)
            DropFilter dropFilter = new DropFilter(true, false);
            List<Grade> filteredGrades = dropFilter.apply(grades); // apply() throws SizeException
            System.out.println("After DropFilter (Lowest Removed): " + filteredGrades);

            // Test TotalStrategy (Simple average)
            TotalStrategy totalStrategy = new TotalStrategy();
            Grade totalGrade = totalStrategy.calculate("Final", filteredGrades); // calculate() throws SizeException
            System.out.println("TotalStrategy (Equal Weight Average): " + totalGrade);

            // Test WeightedTotalStrategy with Weights
            Map<String, Double> weightMap = new HashMap<>();
            weightMap.put("CSC 133", 0.4);
            weightMap.put("CSC 135", 0.3);
            weightMap.put("CSC 139", 0.3);
            WeightedTotalStrategy weightedStrategy = new WeightedTotalStrategy(weightMap);
            Grade weightedGrade = weightedStrategy.calculate("Final", grades); // calculate() throws SizeException
            System.out.println("WeightedTotalStrategy (Weighted Average): " + weightedGrade);
        } catch (SizeException e) {
            System.out.println("Error: " + e.getMessage());
        }

        // Test Missing Utility (No exceptions here)
        Double missingValue = null;
        System.out.println("Missing Value (Default): " + Missing.doubleValue(missingValue));
        System.out.println("Missing Value (Custom -1.0): " + Missing.doubleValue(missingValue, -1.0));
    }
}
