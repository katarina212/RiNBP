import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os


def generate_isolation_image():
    """
    Generate an image visualizing database isolation property.
    """
    print("Generating isolation visualization...")

    # Create figure
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8),
                                   gridspec_kw={'height_ratios': [1, 1]})

    # Define some colors
    t1_color = '#4CAF50'  # Green
    t2_color = '#2196F3'  # Blue

    # First subplot: Problem without isolation
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 5)

    # Timeline
    ax1.plot([1, 9], [1, 1], 'k-', lw=2)
    ax1.text(0.5, 1, 'Time →', va='center')

    # Transaction 1 (transfer €200)
    ax1.add_patch(patches.FancyArrow(1.5, 2, 6, 0, width=0.4,
                                    head_width=0.8, head_length=0.5,
                                    facecolor=t1_color, edgecolor='none', alpha=0.3))
    ax1.text(4.5, 2.5, 'Transaction 1: Transfer €200 from A to B',
             ha='center', va='center', color=t1_color, fontweight='bold')

    # Transaction 2 (add 5% interest)
    ax1.add_patch(patches.FancyArrow(3, 3, 3, 0, width=0.4,
                                    head_width=0.8, head_length=0.5,
                                    facecolor=t2_color, edgecolor='none', alpha=0.3))
    ax1.text(4.5, 3.5, 'Transaction 2: Add 5% interest to A',
             ha='center', va='center', color=t2_color, fontweight='bold')

    # Events in timeline
    events = [
        (1.5, 'T1 starts', t1_color),
        (2, 'T1 reads A=€1000', t1_color),
        (3, 'T2 starts', t2_color),
        (3.5, 'T2 reads A=€1000', t2_color),
        (4, 'T1 sets A=€800', t1_color),
        (4.5, 'T2 calculates A=€1050', t2_color),  # (€1000 * 1.05)
        (5, 'T2 sets A=€1050', t2_color),  # Overwrites T1's change!
        (5.5, 'T1 sets B=€700', t1_color),
        (6, 'T1 commits', t1_color),
        (6.5, 'T2 commits', t2_color)
    ]

    for x, text, color in events:
        ax1.plot([x, x], [0.8, 1.2], color=color, lw=2)
        ax1.text(x, 0.5, text, ha='center', va='center', color=color,
                rotation=45, fontsize=9)

    ax1.text(8, 4, 'Problem: Final A=€1050 instead of €840\nT2 overwrote T1\'s changes!',
             ha='center', va='center', fontsize=10,
             bbox=dict(facecolor='mistyrose', edgecolor='red', alpha=0.5))

    ax1.set_title('Without Proper Isolation (Lost Update Problem)', fontsize=14)
    ax1.axis('off')

    # Second subplot: Solution with isolation
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 5)

    # Timeline
    ax2.plot([1, 9], [1, 1], 'k-', lw=2)
    ax2.text(0.5, 1, 'Time →', va='center')

    # Transaction 1 (transfer €200)
    ax2.add_patch(patches.FancyArrow(1.5, 2, 3.5, 0, width=0.4,
                                    head_width=0.8, head_length=0.5,
                                    facecolor=t1_color, edgecolor='none', alpha=0.3))
    ax2.text(3.25, 2.5, 'Transaction 1',
             ha='center', va='center', color=t1_color, fontweight='bold')

    # Transaction 2 (add 5% interest)
    ax2.add_patch(patches.FancyArrow(5.5, 3, 3, 0, width=0.4,
                                    head_width=0.8, head_length=0.5,
                                    facecolor=t2_color, edgecolor='none', alpha=0.3))
    ax2.text(7, 3.5, 'Transaction 2',
             ha='center', va='center', color=t2_color, fontweight='bold')

    # Events in timeline (isolated)
    events2 = [
        (1.5, 'T1 starts', t1_color),
        (2, 'T1 reads A=€1000', t1_color),
        (2.5, 'T1 sets A=€800', t1_color),
        (3, 'T1 sets B=€700', t1_color),
        (3.5, 'T1 commits', t1_color),
        (5.5, 'T2 starts', t2_color),
        (6, 'T2 reads A=€800', t2_color),  # Sees T1's committed value
        (6.5, 'T2 calculates A=€840', t2_color),  # (€800 * 1.05)
        (7, 'T2 sets A=€840', t2_color),
        (7.5, 'T2 commits', t2_color)
    ]

    for x, text, color in events2:
        ax2.plot([x, x], [0.8, 1.2], color=color, lw=2)
        ax2.text(x, 0.5, text, ha='center', va='center', color=color,
                rotation=45, fontsize=9)

    ax2.text(8, 4, 'Solution: T2 waits for T1 to finish\nFinal A=€840 (correct value)',
             ha='center', va='center', fontsize=10,
             bbox=dict(facecolor='lightgreen', edgecolor='green', alpha=0.5))

    ax2.set_title('With Proper Isolation (Serializable Transactions)', fontsize=14)
    ax2.axis('off')

    # Add overall title
    fig.suptitle('ISOLATION: Concurrent Transactions Must Not Interfere',
                 fontsize=16, y=0.98)

    # Add explanation text
    fig.text(0.5, 0.02, 'Transactions running concurrently should behave as if they run one after another.\n'
                        'The result should be the same as if transactions executed in some sequential order.',
                         ha='center', fontsize=12, fontweight='bold')

    # Save the figure
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.savefig('images/isolation.png', dpi=200)
    plt.close()

    print("Isolation image saved to images/isolation.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_isolation_image()