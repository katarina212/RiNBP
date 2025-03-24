import matplotlib.pyplot as plt
import numpy as np
import os

def generate_atomicity_image():
    """
    Generate an image visualizing database atomicity property.
    """
    print("Generating atomicity visualization...")

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Set up the timeline
    timeline = np.linspace(0, 10, 11)
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-1, 5)

    # Plot timeline
    ax.plot(timeline, [0]*len(timeline), 'k-', linewidth=2)
    for t in timeline:
        ax.plot([t, t], [-0.2, 0.2], 'k-', linewidth=2)

    # Label the timeline
    ax.text(-0.5, -0.5, 'Time →', fontsize=12)

    # Transaction area (successful case)
    ax.fill_between([1, 7], 0.5, 2.5, color='lightgreen', alpha=0.3)
    ax.text(4, 2.8, 'Successful Transaction', fontsize=12, ha='center', fontweight='bold')

    # Add transaction operations for success case
    ops_success = [
        (1.5, 'Start Transaction', 1.5),
        (2.5, 'Debit Account A: €200', 1.5),
        (4, 'Credit Account B: €200', 1.5),
        (5.5, 'Update Transaction Log', 1.5),
        (6.5, 'Commit Transaction', 1.5)
    ]

    for x, text, y in ops_success:
        ax.plot([x, x], [0, y], 'g-', linewidth=1.5)
        ax.scatter(x, y, s=50, color='green')
        ax.text(x, y+0.2, text, ha='center', va='bottom', fontsize=10, color='green')

    # Transaction area (failed case)
    ax.fill_between([1, 5], 3, 5, color='mistyrose', alpha=0.3)
    ax.text(3, 4.5, 'Failed Transaction', fontsize=12, ha='center', fontweight='bold')

    # Add transaction operations for failed case
    ops_failed = [
        (1.5, 'Start Transaction', 4),
        (2.5, 'Debit Account A: €200', 4),
        (3.5, 'Credit Account B: Fails', 4),
        (4.5, 'Rollback Transaction', 4)
    ]

    for x, text, y in ops_failed:
        ax.plot([x, x], [0, y], 'r-', linewidth=1.5)
        ax.scatter(x, y, s=50, color='red')
        ax.text(x, y+0.2, text, ha='center', va='bottom', fontsize=10, color='red')

    # Add red X for failure
    ax.plot([3.3, 3.7], [3.8, 4.2], 'r-', linewidth=2)
    ax.plot([3.7, 3.3], [3.8, 4.2], 'r-', linewidth=2)

    # Add a title
    ax.set_title('ATOMICITY: All-or-Nothing Principle', fontsize=16, pad=20)

    # Remove axes
    ax.axis('off')

    # Add explanation text
    fig.text(0.5, 0.05, 'Either ALL operations in a transaction complete successfully (commit),\n'
              'or NONE of them are applied to the database (rollback).',
              ha='center', fontsize=12, fontweight='bold')

    # Save the figure
    plt.tight_layout()
    plt.savefig('images/atomicity.png', dpi=200, bbox_inches='tight')
    plt.close()

    print("Atomicity image saved to images/atomicity.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_atomicity_image()