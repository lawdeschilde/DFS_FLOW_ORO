
from core_engine import OROCore
from symmetry_filter import SymmetryFilter
from kinetic_handler import KineticHandler

def run_oro_protocol():
    """Executes the Unified ORO Operational Node."""
    # Initialize the Triad
    core = OROCore()
    filtrate = SymmetryFilter()
    handler = KineticHandler()

    # Define Input Stream
    raw_stream = "Is the ORO rollout functional? The system is active and secure."

    # Execute Logic Gates
    step_1 = filtrate.null_stake(raw_stream)
    final_output = handler.finalize(step_1)

    print(f"ORO SYSTEM OUTPUT: {final_output}")

if __name__ == "__main__":
    run_oro_protocol()
