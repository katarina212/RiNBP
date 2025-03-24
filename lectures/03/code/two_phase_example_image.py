import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os


def generate_two_phase_example_image():
    """
    Generate an image visualizing a two-phase commit example for online shopping.
    """
    print("Generating two-phase example visualization...")

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Set up plot
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)

    # Define colors
    colors = {
        'coordinator': '#E91E63',  # Pink
        'system1': '#2196F3',      # Blue
        'system2': '#4CAF50',      # Green
        'system3': '#FF9800',      # Orange
        'success': '#A5D6A7',      # Light green
        'failure': '#FFCDD2',      # Light red
        'prepare': '#BBDEFB',      # Light blue
        'commit': '#C8E6C9',       # Light green
        'abort': '#FFCCBC',        # Light orange
        'border': '#455A64'        # Dark bluish gray
    }

    # Draw systems
    systems = [
        {'name': 'Order System', 'color': colors['system1'], 'pos': (2, 5.5)},
        {'name': 'Payment System', 'color': colors['system2'], 'pos': (5, 5.5)},
        {'name': 'Inventory System', 'color': colors['system3'], 'pos': (8, 5.5)}
    ]

    coordinator = {'name': 'Transaction Coordinator', 'color': colors['coordinator'], 'pos': (5, 3)}

    # Draw coordinator
    coord_box = patches.FancyBboxPatch(
        (coordinator['pos'][0]-1.5, coordinator['pos'][1]-0.5), 3, 1,
        boxstyle="round,pad=0.3",
        facecolor=coordinator['color'],
        edgecolor=colors['border'],
        alpha=0.8
    )
    ax.add_patch(coord_box)
    ax.text(coordinator['pos'][0], coordinator['pos'][1], coordinator['name'],
            ha='center', va='center', color='white', fontweight='bold')

    # Draw systems
    for system in systems:
        sys_box = patches.FancyBboxPatch(
            (system['pos'][0]-1, system['pos'][1]-0.5), 2, 1,
            boxstyle="round,pad=0.3",
            facecolor=system['color'],
            edgecolor=colors['border'],
            alpha=0.8
        )
        ax.add_patch(sys_box)
        ax.text(system['pos'][0], system['pos'][1], system['name'],
                ha='center', va='center', color='white', fontweight='bold')

    # Draw phase 1: Prepare
    # Phase title
    ax.text(1, 4.5, "Phase 1: Prepare", fontsize=12, fontweight='bold')

    # Prepare messages
    for system in systems:
        ax.annotate("Prepare?",
                   xy=system['pos'],
                   xytext=(coordinator['pos'][0], coordinator['pos'][1]+0.3),
                   arrowprops=dict(facecolor=colors['prepare'], shrink=0.05,
                                  width=1, headwidth=8, alpha=0.8),
                   ha='center', va='center',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor=colors['prepare'],
                            alpha=0.8),
                   fontsize=9)

    # Draw responses (all yes for first two, no for inventory)
    responses = [
        {"from": systems[0], "text": "Yes", "color": colors['success']},
        {"from": systems[1], "text": "Yes", "color": colors['success']},
        {"from": systems[2], "text": "No", "color": colors['failure']}
    ]

    for response in responses:
        ax.annotate(response['text'],
                   xy=(coordinator['pos'][0], coordinator['pos'][1]-0.3),
                   xytext=(response['from']['pos'][0], response['from']['pos'][1]-0.3),
                   arrowprops=dict(facecolor=response['color'], shrink=0.05,
                                  width=1, headwidth=8, alpha=0.8),
                   ha='center', va='center',
                   bbox=dict(boxstyle="round,pad=0.2", facecolor=response['color'],
                            alpha=0.8),
                   fontsize=9)

    # Draw phase 2: Abort
    # Phase title
    ax.text(1, 2, "Phase 2: Abort", fontsize=12, fontweight='bold')

    # Abort messages
    for system in systems[:2]:  # Only send to systems that responded "Yes"
        ax.annotate("Abort!",
                   xy=system['pos'],
                   xytext=(coordinator['pos'][0], coordinator['pos'][1]-0.3),
                   arrowprops=dict(facecolor=colors['abort'], shrink=0.05,
                                  width=1, headwidth=8, alpha=0.8),
                   ha='center', va='center',
                   bbox=dict(boxstyle="round,pad=0.2", facecolor=colors['abort'],
                            alpha=0.8),
                   fontsize=9)

    # Add explanation of the scenario
    scenario_text = (
        "Online Purchase Scenario:\n"
        "1. Order System: Can create the order ✓\n"
        "2. Payment System: Card payment authorized ✓\n"
        "3. Inventory System: Item out of stock ✗\n\n"
        "Result: Transaction aborted, payment authorization reversed"
    )

    ax.text(5, 1.2, scenario_text, ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.5", facecolor='white',
                     edgecolor=colors['border'], alpha=0.8),
            fontsize=10)

    # Add title
    ax.set_title("Two-Phase Commit: Online Shopping Example", fontsize=14, pad=15)

    # Hide axes
    ax.axis('off')

    # Save the figure
    plt.tight_layout()
    plt.savefig('images/two-phase-example.png', dpi=200)
    plt.close()

    print("Two-phase example image saved to images/two-phase-example.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_two_phase_example_image()