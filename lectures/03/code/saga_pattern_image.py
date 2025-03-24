import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os


def generate_saga_pattern_image():
    """
    Generate an image visualizing the Saga pattern for distributed transactions.
    """
    print("Generating saga pattern visualization...")

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Set up the plot
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)

    # Define colors
    colors = {
        'success': '#66BB6A',      # Green
        'failure': '#EF5350',      # Red
        'compensate': '#FFA726',   # Orange
        'border': '#37474F',       # Dark gray
        'box': '#E3F2FD',          # Light blue
        'text': '#212121'          # Dark text
    }

    # Create two scenarios: successful and compensating transaction
    scenario_height = 3

    # Scenario 1: Successful Saga
    ax.text(1, 6.5, "Scenario 1: Successful Saga", fontsize=12, fontweight='bold')

    # Draw transaction steps
    steps = [
        {'name': 'Book Flight', 'x': 2, 'success': True},
        {'name': 'Reserve Hotel', 'x': 4, 'success': True},
        {'name': 'Rent Car', 'x': 6, 'success': True},
        {'name': 'Charge Credit Card', 'x': 8, 'success': True}
    ]

    for step in steps:
        # Draw success box
        color = colors['success'] if step['success'] else colors['failure']
        box = patches.FancyBboxPatch((step['x']-0.8, 5.5), 1.6, 0.8,
                                    boxstyle="round,pad=0.3",
                                    facecolor=color, alpha=0.8,
                                    edgecolor=colors['border'])
        ax.add_patch(box)

        # Add step name
        ax.text(step['x'], 5.9, step['name'], ha='center', va='center',
               color='white', fontsize=10, fontweight='bold')

    # Draw flow arrows
    for i in range(len(steps)-1):
        ax.arrow(steps[i]['x']+0.8, 5.9, steps[i+1]['x']-steps[i]['x']-1.6, 0,
                head_width=0.2, head_length=0.2, fc=colors['border'], ec=colors['border'])

    # Add success label
    ax.text(9.5, 5.9, "✓", ha='center', va='center',
           color=colors['success'], fontsize=16, fontweight='bold')

    # Scenario 2: Compensating Saga
    ax.text(1, 3.5, "Scenario 2: Saga with Compensation", fontsize=12, fontweight='bold')

    # Draw transaction steps with failure
    steps_comp = [
        {'name': 'Book Flight', 'x': 2, 'success': True},
        {'name': 'Reserve Hotel', 'x': 4, 'success': True},
        {'name': 'Rent Car', 'x': 6, 'success': False},  # This step fails
        {'name': 'Charge Credit Card', 'x': 8, 'skipped': True}
    ]

    for step in steps_comp:
        if 'skipped' in step and step['skipped']:
            # Draw skipped step with dashed line
            box = patches.FancyBboxPatch((step['x']-0.8, 2.5), 1.6, 0.8,
                                        boxstyle="round,pad=0.3",
                                        facecolor='white', alpha=0.3,
                                        edgecolor=colors['border'], linestyle='--')
            ax.add_patch(box)
            ax.text(step['x'], 2.9, step['name'], ha='center', va='center',
                   color=colors['text'], fontsize=10, alpha=0.5)
        else:
            # Draw regular step
            color = colors['success'] if step['success'] else colors['failure']
            box = patches.FancyBboxPatch((step['x']-0.8, 2.5), 1.6, 0.8,
                                        boxstyle="round,pad=0.3",
                                        facecolor=color, alpha=0.8,
                                        edgecolor=colors['border'])
            ax.add_patch(box)
            ax.text(step['x'], 2.9, step['name'], ha='center', va='center',
                   color='white', fontsize=10, fontweight='bold')

    # Draw compensation steps
    comp_steps = [
        {'name': 'Cancel Hotel', 'x': 4, 'y': 1.5},
        {'name': 'Cancel Flight', 'x': 2, 'y': 1.5}
    ]

    for step in comp_steps:
        # Draw compensation box
        box = patches.FancyBboxPatch((step['x']-0.8, step['y']-0.4), 1.6, 0.8,
                                    boxstyle="round,pad=0.3",
                                    facecolor=colors['compensate'], alpha=0.8,
                                    edgecolor=colors['border'])
        ax.add_patch(box)

        # Add step name
        ax.text(step['x'], step['y'], step['name'], ha='center', va='center',
               color='white', fontsize=10, fontweight='bold')

    # Draw flow arrows for success path
    for i in range(len(steps_comp)-2):
        ax.arrow(steps_comp[i]['x']+0.8, 2.9,
                steps_comp[i+1]['x']-steps_comp[i]['x']-1.6, 0,
                head_width=0.2, head_length=0.2,
                fc=colors['border'], ec=colors['border'])

    # Draw arrow to failure
    ax.arrow(steps_comp[1]['x']+0.8, 2.9,
            steps_comp[2]['x']-steps_comp[1]['x']-1.6, 0,
            head_width=0.2, head_length=0.2,
            fc=colors['border'], ec=colors['border'])

    # Draw arrow from failure to first compensation
    ax.arrow(steps_comp[2]['x'], 2.5-0.1,
            comp_steps[0]['x']-steps_comp[2]['x'], comp_steps[0]['y']-(2.5-0.1),
            head_width=0.2, head_length=0.2,
            fc=colors['failure'], ec=colors['failure'])

    # Draw arrow between compensation steps
    ax.arrow(comp_steps[0]['x']-0.8, comp_steps[0]['y'],
            comp_steps[1]['x']+0.8-comp_steps[0]['x']+0.8, 0,
            head_width=0.2, head_length=0.2,
            fc=colors['compensate'], ec=colors['compensate'])

    # Add failure label
    ax.text(9.5, 2.9, "✗", ha='center', va='center',
           color=colors['failure'], fontsize=16, fontweight='bold')

    # Add compensation label
    ax.text(0.5, 1.5, "Compensation:", ha='center', va='center',
           color=colors['compensate'], fontsize=10, fontweight='bold')

    # Add explanation
    explanation = (
        "Saga Pattern in Distributed Transactions:\n"
        "• Each transaction has a compensating transaction that undoes its changes\n"
        "• If any step fails, previous steps are undone by running their compensations\n"
        "• Provides coordination without two-phase commit\n"
        "• Ensures eventual consistency by cleaning up partial transactions"
    )

    # Add explanation text box
    explanation_box = patches.FancyBboxPatch((0.5, 0.2), 9, 0.8,
                                            boxstyle="round,pad=0.5",
                                            facecolor=colors['box'], alpha=0.8,
                                            edgecolor=colors['border'])
    ax.add_patch(explanation_box)
    ax.text(5, 0.6, explanation, ha='center', va='center',
           fontsize=10, color=colors['text'])

    # Add title
    ax.set_title("Saga Pattern: Long-Running Transactions with Compensation",
                fontsize=14, pad=10)

    # Remove axes
    ax.axis('off')

    # Save the figure
    plt.tight_layout()
    plt.savefig('images/saga-pattern.png', dpi=200)
    plt.close()

    print("Saga pattern image saved to images/saga-pattern.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_saga_pattern_image()