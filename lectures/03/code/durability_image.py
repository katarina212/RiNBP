import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os


def generate_durability_image():
    """
    Generate an image visualizing database durability property.
    """
    print("Generating durability visualization...")

    # Create figure
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    # Timeline setup
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)

    # Draw timeline
    ax.plot([1, 9], [1, 1], 'k-', lw=2)
    ax.text(0.5, 1, 'Time →', va='center')

    # Database server icon
    server_rect = patches.Rectangle((2, 3.5), 2, 1.5,
                                   facecolor='lightblue',
                                   edgecolor='blue', alpha=0.7)
    ax.add_patch(server_rect)
    ax.text(3, 4.25, 'Database Server', ha='center', fontsize=10)

    # Transaction log icon
    log_rect = patches.Rectangle((6, 3.5), 2, 1.5,
                                facecolor='lightgreen',
                                edgecolor='green', alpha=0.7)
    ax.add_patch(log_rect)
    ax.text(7, 4.25, 'Transaction Log', ha='center', fontsize=10)

    # Disk storage icon
    disk_rect = patches.Rectangle((4, 2), 2, 1,
                                 facecolor='lightgrey',
                                 edgecolor='grey', alpha=0.7)
    ax.add_patch(disk_rect)
    ax.text(5, 2.5, 'Disk Storage', ha='center', fontsize=10)

    # Timeline events
    events = [
        (2, 'BEGIN\nTRANSACTION', 'black'),
        (3, 'UPDATE\nACCOUNTS', 'blue'),
        (4, 'WRITE TO\nTRANSACTION LOG', 'green'),
        (5, 'COMMIT\nTRANSACTION', 'black'),
        (6, 'CONFIRMATION\nTO CLIENT', 'black'),
        (7, 'SYSTEM\nCRASH!', 'red'),
        (8, 'SYSTEM\nRECOVERY', 'purple')
    ]

    for i, (x, text, color) in enumerate(events):
        ax.plot([x, x], [0.8, 1.2], color=color, lw=2)
        ax.text(x, 0.5, text, ha='center', va='center',
               color=color, fontsize=8, rotation=45)

    # Draw arrows for the flow
    arrows = [
        # Transaction to log
        (3, 4.25, 3.5, 0, 'blue'),
        # Log to disk
        (6.5, 3.5, -1, -0.75, 'green'),
        # Crash icon
        (7, 1.5, 0, 0.5, 'red'),
        # Recovery arrow
        (8, 2.5, -2.5, 0, 'purple')
    ]

    for x, y, dx, dy, color in arrows:
        ax.arrow(x, y, dx, dy, head_width=0.2, head_length=0.3,
                fc=color, ec=color, width=0.05)

    # Add "lightning" for crash
    crash_x, crash_y = 7, 1.5
    lightning_points = [
        (crash_x, crash_y + 1),
        (crash_x - 0.2, crash_y + 0.5),
        (crash_x + 0.1, crash_y + 0.3),
        (crash_x - 0.2, crash_y - 0.1),
        (crash_x + 0.1, crash_y - 0.3),
        (crash_x - 0.1, crash_y - 0.7)
    ]
    ax.add_patch(patches.Polygon(lightning_points,
                                closed=False, fill=False,
                                edgecolor='red', lw=2, joinstyle='miter'))

    # Add explanatory text boxes
    explanations = [
        (3, 5.5, 'Database processes\ntransaction and updates\nmemory', 'blue'),
        (7, 5.5, 'Transaction is durable:\nThe committed changes\nsurvive system crash', 'green'),
        (5, 0.3, 'After recovery, all committed transactions\' effects are still present in the database', 'purple')
    ]

    for x, y, text, color in explanations:
        ax.text(x, y, text, ha='center', va='center', fontsize=10,
               bbox=dict(facecolor='white', edgecolor=color,
                        alpha=0.7, boxstyle='round,pad=0.5'))

    # Add overall title
    ax.set_title('DURABILITY: Committed Transactions Survive System Failure',
                fontsize=16, pad=20)

    # Remove axes
    ax.axis('off')

    # Add explanation text
    fig.text(0.5, 0.05, 'Once a transaction is committed, its changes are permanent\n'
                       'and will not be lost even in the event of a system failure.',
                        ha='center', fontsize=12, fontweight='bold')

    # Save the figure
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.savefig('images/durability.png', dpi=200)
    plt.close()

    print("Durability image saved to images/durability.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_durability_image()