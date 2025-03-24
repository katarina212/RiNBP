import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow
import os


def generate_two_phase_commit_image():
    """
    Generate an image visualizing the two-phase commit protocol.
    """
    print("Generating two-phase commit visualization...")

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Set up plot
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)

    # Colors
    colors = {
        'coordinator': '#D32F2F',    # Red
        'participant': '#1976D2',    # Blue
        'phase1': '#FFB74D',         # Orange
        'phase2': '#AED581',         # Green
        'arrow': '#616161',          # Dark gray
        'success': '#66BB6A',        # Green
        'failure': '#EF5350'         # Red
    }

    # Draw coordinator
    coord_rect = Rectangle((4, 7), 2, 0.8, facecolor=colors['coordinator'],
                          alpha=0.8, edgecolor='black')
    ax.add_patch(coord_rect)
    ax.text(5, 7.4, "Coordinator", ha='center', va='center',
           color='white', fontsize=12, fontweight='bold')

    # Draw participants
    participant_positions = [(2, 5), (5, 5), (8, 5)]
    participant_labels = ["Participant 1", "Participant 2", "Participant 3"]

    for i, (pos, label) in enumerate(zip(participant_positions, participant_labels)):
        part_rect = Rectangle((pos[0]-1, pos[1]), 2, 0.8,
                             facecolor=colors['participant'],
                             alpha=0.8, edgecolor='black')
        ax.add_patch(part_rect)
        ax.text(pos[0], pos[1]+0.4, label, ha='center', va='center',
               color='white', fontsize=10, fontweight='bold')

    # Phase 1: Prepare
    ax.text(1, 6.3, "Phase 1: Prepare", fontsize=14, fontweight='bold')

    # Draw prepare requests
    for pos in participant_positions:
        # Arrow from coordinator to participant
        prepare_arrow = FancyArrow(5, 6.8, pos[0]-5, pos[1]-6.3,
                                  width=0.05, head_width=0.2, head_length=0.3,
                                  facecolor=colors['phase1'], edgecolor='black')
        ax.add_patch(prepare_arrow)

        # Label the arrow
        mid_x = (5 + pos[0]) / 2
        mid_y = (6.8 + pos[1]) / 2 - 0.3
        ax.text(mid_x, mid_y, "Prepare?", ha='center', va='center',
               color=colors['arrow'], fontsize=10, fontweight='bold',
               bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.2'))

    # Draw votes (responses)
    for i, pos in enumerate(participant_positions):
        # Determine if this participant votes yes or no
        # For illustration, let's say all vote yes except participant 2 in "failure" scenario
        vote_color = colors['success']
        vote_text = "Yes"

        if i == 1 and 'failure_scenario' in globals() and failure_scenario:
            vote_color = colors['failure']
            vote_text = "No"

        # Arrow from participant to coordinator
        vote_arrow = FancyArrow(pos[0], pos[1]+0.9, 5-pos[0], 6.9-pos[1]-0.9,
                               width=0.05, head_width=0.2, head_length=0.3,
                               facecolor=vote_color, edgecolor='black')
        ax.add_patch(vote_arrow)

        # Label the arrow
        mid_x = (pos[0] + 5) / 2
        mid_y = (pos[1]+0.9 + 6.9) / 2
        ax.text(mid_x, mid_y, vote_text, ha='center', va='center',
               color=colors['arrow'], fontsize=10, fontweight='bold',
               bbox=dict(facecolor=vote_color, alpha=0.3, boxstyle='round,pad=0.2'))

    # Phase 2: Commit/Abort
    ax.text(1, 4, "Phase 2: Commit", fontsize=14, fontweight='bold')

    # Draw final decision arrows
    for pos in participant_positions:
        # Arrow from coordinator to participant for final decision
        decision_arrow = FancyArrow(5, 6.7, pos[0]-5, pos[1]+0.9-6.7,
                                   width=0.05, head_width=0.2, head_length=0.3,
                                   facecolor=colors['phase2'], edgecolor='black')
        ax.add_patch(decision_arrow)

        # Label the arrow
        mid_x = (5 + pos[0]) / 2
        mid_y = (6.7 + pos[1]+0.9) / 2 - 0.6

        # All participants receive commit in the success scenario
        decision_text = "Commit"
        decision_color = colors['success']

        ax.text(mid_x, mid_y, decision_text, ha='center', va='center',
               color=colors['arrow'], fontsize=10, fontweight='bold',
               bbox=dict(facecolor=decision_color, alpha=0.3, boxstyle='round,pad=0.2'))

    # Add participant final states
    for pos in participant_positions:
        ax.text(pos[0], pos[1]-0.3, "Committed", ha='center', va='center',
               color=colors['success'], fontsize=10, fontweight='bold')

    # Add decision point in coordinator
    decision_rect = Rectangle((4.5, 6.2), 1, 0.5, facecolor=colors['success'],
                             alpha=0.5, edgecolor='black')
    ax.add_patch(decision_rect)
    ax.text(5, 6.45, "All Yes", ha='center', va='center', fontsize=10, fontweight='bold')

    # Add transaction outcome
    outcome_rect = Rectangle((3, 3), 4, 0.8, facecolor=colors['success'],
                            alpha=0.3, edgecolor='black')
    ax.add_patch(outcome_rect)
    ax.text(5, 3.4, "Transaction Committed Successfully",
           ha='center', va='center', color='green',
           fontsize=12, fontweight='bold')

    # Add explanation
    ax.text(5, 2, "All participants agreed to commit,\nso the coordinator "
           "instructs all to commit the transaction.",
           ha='center', va='center', fontsize=10)

    # Add title
    ax.set_title("Two-Phase Commit Protocol (Successful Scenario)",
                fontsize=16, pad=20)

    # Hide axes
    ax.axis('off')

    # Save the figure
    plt.tight_layout()
    plt.savefig('images/two-phase-commit.png', dpi=200)
    plt.close()

    print("Two-phase commit image saved to images/two-phase-commit.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_two_phase_commit_image()