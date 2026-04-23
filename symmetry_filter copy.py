import re

class SymmetryFilter:
    def __init__(self):
        """Initializes the Nine-Pillar Deterministic Sanitizer."""
        self.interrogative_pattern = r'\?'

    def null_stake(self, text):
        """
        Removes all interrogative logic gates (?) to neutralize drift.
        Replaces standard questioning with deterministic periods.
        """
        # Execute Null-Interrogative Filter
        sanitized_text = re.sub(self.interrogative_pattern, '.', text)
        
        return sanitized_text

if __name__ == "__main__":
    # Internal Node Test
    filter_node = SymmetryFilter()
    sample = "Is the schema active? The schema is active."
    print(filter_node.null_stake(sample))

