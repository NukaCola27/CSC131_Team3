package grading;
import java.util.Map;
import java.util.HashMap;
import java.util.List;

public class WeightedTotalStrategy implements GradingStrategy {
    private Map<String, Double> weights;

    // Constructors
    public WeightedTotalStrategy() {
        this.weights = new HashMap<>(); // Initializes an empty map
    }

    public WeightedTotalStrategy(Map<String, Double> weights) {
        this.weights = weights; // Assigns provided map
    }

    // Implements calculate()
    @Override
    public Grade calculate(String key, List<Grade> grades) throws SizeException {
    	// Check if list is empty
        if (grades == null || grades.isEmpty()) {
            throw new SizeException("List is empty");
        }

        double total = 0;
        double weightSum = 0;

        for (Grade g : grades) {
            double weight = weights.getOrDefault(g.getKey(), 1.0);
            total += g.getValue() * weight;
            weightSum += weight;
        }

        double finalGrade = weightSum == 0 ? 0 : total / weightSum;
        return new Grade(key, finalGrade);
    }
}
