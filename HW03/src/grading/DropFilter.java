package grading;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;


public class DropFilter implements Filter {
	// Attributes
	private boolean shouldDropLowest;
	private boolean shouldDropHighest;
	
	// Constructors 
    public DropFilter() {
        this.shouldDropLowest = false;
        this.shouldDropHighest = false;
    }

    // Constructor that allows customization
    public DropFilter(boolean shouldDropLowest, boolean shouldDropHighest) {
        this.shouldDropLowest = shouldDropLowest;
        this.shouldDropHighest = shouldDropHighest;
    }
    
    // Implement apply()
	@Override
	public List<Grade> apply(List<Grade> grades) throws SizeException {
		// Check if list is empty
		if (grades == null || grades.isEmpty()) {
			throw new SizeException("List is empty");
		}
		
		List<Grade> newGrades = new ArrayList<>(grades); // copy list, return newGrades
		
		// Remove lowest if shouldDropLowest == true
        if (shouldDropLowest) {
            Grade lowest = Collections.min(newGrades); // use min() to find lowest grade
            newGrades.remove(lowest);
        }
        
        // Remove lowest if shouldDropHighest == true
        if (shouldDropHighest) {
            Grade highest = Collections.max(newGrades); // use max() to find lowest grade
            newGrades.remove(highest);
        }
        
        return newGrades;
        
	}
}
