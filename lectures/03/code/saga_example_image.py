import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os


def generate_saga_example_image():
    """
    Generate an image visualizing a saga example for travel booking.
    """
    print("Generating saga example visualization...")

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Setup plot
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Define colors
    colors = {
        'success': '#66BB6A',      # Green
        'failure': '#EF5350',      # Red
        'local_tx': '#2196F3',     # Blue
        'compensate': '#FFA726',   # Orange
        'border': '#455A64',       # Dark gray
        'text': '#212121',         # Dark text
        'highlight': '#FFD54F'     # Yellow highlight
    }

    # Define systems
    systems = [
        {'name': 'Flight Service', 'y': 8},
        {'name': 'Hotel Service', 'y': 6},
        {'name': 'Car Service', 'y': 4},
        {'name': 'Payment Service', 'y': 2}
    ]

    # Define swimlanes
    for system in systems:
        # Draw line
        ax.plot([0.5, 9.5], [system['y'] - 1, system['y'] - 1],
               'k--', alpha=0.3)

        # Add system name
        ax.text(0.5, system['y'], system['name'], ha='left', va='center',
               fontsize=10, fontweight='bold')

    # Define transactions and their positions
    transactions = [
        {'name': 'Book Flight', 'x': 2, 'system': 0, 'success': True},
        {'name': 'Book Hotel', 'x': 3.5, 'system': 1, 'success': True},
        {'name': 'Rent Car', 'x': 5, 'system': 2, 'success': False},
        {'name': 'Process Payment', 'x': 6.5, 'system': 3, 'skipped': True}
    ]

    # Define compensating transactions
    compensations = [
        {'name': 'Cancel Hotel', 'x': 7, 'system': 1},
        {'name': 'Cancel Flight', 'x': 8.5, 'system': 0}
    ]

    # Draw transaction boxes
    for tx in transactions:
        y = systems[tx['system']]['y']

        if 'skipped' in tx and tx['skipped']:
            # Skipped transaction
            box = patches.Rectangle((tx['x'] - 0.7, y - 0.7), 1.4, 0.7,
                                   facecolor='white', edgecolor=colors['border'],
                                   linestyle='--', alpha=0.5)
            ax.add_patch(box)
            ax.text(tx['x'], y - 0.35, tx['name'], ha='center', va='center',
                   fontsize=9, alpha=0.5)
        else:
            # Regular transaction
            color = colors['success'] if tx.get('success', False) else colors['failure']
            box = patches.Rectangle((tx['x'] - 0.7, y - 0.7), 1.4, 0.7,
                                   facecolor=color, edgecolor=colors['border'],
                                   alpha=0.7)
            ax.add_patch(box)
            ax.text(tx['x'], y - 0.35, tx['name'], ha='center', va='center',
                   fontsize=9, color='white', fontweight='bold')

    # Draw compensating transactions
    for comp in compensations:
        y = systems[comp['system']]['y']

        # Compensation transaction
        box = patches.Rectangle((comp['x'] - 0.7, y - 0.7), 1.4, 0.7,
                               facecolor=colors['compensate'],
                               edgecolor=colors['border'], alpha=0.7)
        ax.add_patch(box)
        ax.text(comp['x'], y - 0.35, comp['name'], ha='center', va='center',
               fontsize=9, color='white', fontweight='bold')

    # Draw flow arrows
    # Main transaction flow
    arrow_y_offset = -0.1

    # T1 -> T2
    ax.arrow(transactions[0]['x'] + 0.7, systems[transactions[0]['system']]['y'] + arrow_y_offset,
            transactions[1]['x'] - transactions[0]['x'] - 1.4,
            systems[transactions[1]['system']]['y'] - systems[transactions[0]['system']]['y'],
            head_width=0.2, head_length=0.2, fc=colors['local_tx'], ec=colors['local_tx'],
            length_includes_head=True)

    # T2 -> T3
    ax.arrow(transactions[1]['x'] + 0.7, systems[transactions[1]['system']]['y'] + arrow_y_offset,
            transactions[2]['x'] - transactions[1]['x'] - 1.4,
            systems[transactions[2]['system']]['y'] - systems[transactions[1]['system']]['y'],
            head_width=0.2, head_length=0.2, fc=colors['local_tx'], ec=colors['local_tx'],
            length_includes_head=True)

    # T3 -> C1 (failure to compensation)
    ax.arrow(transactions[2]['x'] + 0.2, systems[transactions[2]['system']]['y'] + arrow_y_offset,
            compensations[0]['x'] - transactions[2]['x'] - 0.9,
            systems[compensations[0]['system']]['y'] - systems[transactions[2]['system']]['y'],
            head_width=0.2, head_length=0.2, fc=colors['failure'], ec=colors['failure'],
            length_includes_head=True)

    # C1 -> C2
    ax.arrow(compensations[0]['x'] + 0.7, systems[compensations[0]['system']]['y'] + arrow_y_offset,
            compensations[1]['x'] - compensations[0]['x'] - 1.4,
            systems[compensations[1]['system']]['y'] - systems[compensations[0]['system']]['y'],
            head_width=0.2, head_length=0.2, fc=colors['compensate'], ec=colors['compensate'],
            length_includes_head=True)

    # Add status icons
    for tx in transactions:
        if 'skipped' in tx and tx['skipped']:
            continue

        y = systems[tx['system']]['y']
        icon = "✓" if tx.get('success', False) else "✗"
        icon_color = colors['success'] if tx.get('success', False) else colors['failure']

        ax.text(tx['x'] + 0.9, y - 0.35, icon, ha='center', va='center',
               fontsize=12, color=icon_color, fontweight='bold')

    # Add compensation icons
    for comp in compensations:
        y = systems[comp['system']]['y']

        ax.text(comp['x'] + 0.9, y - 0.35, "↩", ha='center', va='center',
               fontsize=12, color=colors['text'], fontweight='bold')

    # Add timeline indicators
    timeline_positions = [
        (1.3, 'Start Transaction'),
        (transactions[0]['x'], 'T1: Flight'),
        (transactions[1]['x'], 'T2: Hotel'),
        (transactions[2]['x'], 'T3: Car (Fails)'),
        (compensations[0]['x'], 'C1: Cancel Hotel'),
        (compensations[1]['x'], 'C2: Cancel Flight'),
        (9.3, 'End (Rolled Back)')
    ]

    for i, (x, label) in enumerate(timeline_positions):
        ax.plot([x, x], [0.5, 0.8], 'k-', lw=1)
        ax.text(x, 0.3, label, ha='center', va='center', fontsize=8,
               rotation=45 if i > 0 and i < len(timeline_positions)-1 else 0)

    # Add horizontal timeline
    ax.plot([timeline_positions[0][0], timeline_positions[-1][0]], [0.5, 0.5], 'k-', lw=1)

    # Add failure highlight
    failure_patch = patches.Rectangle((transactions[2]['x'] - 0.8,
                                      systems[transactions[2]['system']]['y'] - 0.8),
                                     1.6, 0.9,
                                     facecolor=colors['highlight'],
                                     edgecolor=colors['failure'],
                                     alpha=0.3, linestyle='--', fill=True)
    ax.add_patch(failure_patch)

    # Add title
    ax.set_title("Saga Pattern Example: Travel Booking with Compensation",
                fontsize=14, pad=10)

    # Add explanation
    explanation = (
        "This example illustrates a travel booking saga:\n"
        "1. Flight booking succeeds\n"
        "2. Hotel booking succeeds\n"
        "3. Car rental fails\n"
        "4. Payment is skipped\n"
        "5. Compensation begins: Cancel hotel reservation\n"
        "6. Compensation continues: Cancel flight reservation\n"
        "7. All completed steps are rolled back in reverse order"
    )

    # Add explanation text box
    exp_box = patches.FancyBboxPatch((7, 8.5), 2.5, 1.3,
                                    boxstyle="round,pad=0.3",
                                    facecolor='white', alpha=0.8,
                                    edgecolor=colors['border'])
    ax.add_patch(exp_box)
    ax.text(8.25, 9.15, explanation, ha='center', va='center',
           fontsize=7, color=colors['text'])

    # Remove axes
    ax.axis('off')

    # Save the figure
    plt.tight_layout()
    plt.savefig('images/saga-example.png', dpi=200)
    plt.close()

    print("Saga example image saved to images/saga-example.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_saga_example_image()