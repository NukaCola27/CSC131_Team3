package grading;
import java.util.List;

public interface GradingStrategy {
	Grade calculate(String key, List<Grade> grades) throws SizeException;
}
