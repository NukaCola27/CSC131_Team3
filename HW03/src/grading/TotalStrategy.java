package grading;
import java.util.HashMap;

public class TotalStrategy extends WeightedTotalStrategy {
    public TotalStrategy() {
        super(new HashMap<>()); // No weights = default weight of 1.0
    }
}
