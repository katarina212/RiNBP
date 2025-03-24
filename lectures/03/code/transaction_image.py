import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os


def generate_transaction_image():
    """
    Generate an image visualizing database transactions with emphasis on ACID properties.
    """
    print("Generating transaction visualization...")

    # Create a figure
    fig, ax = plt.subplots(figsize=(12, 8))

    # Set plot background color to light gray
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_facecolor('#f8f9fa')

    # Remove axis
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Set title
    ax.set_title('Database Transactions', fontsize=22, fontweight='bold', pad=20)

    # Define colors
    colors = {
        'transaction': '#4285F4',
        'database': '#34A853',
        'read': '#FBBC05',
        'write': '#EA4335',
        'commit': '#26A69A',
        'rollback': '#F44336',
        'arrow': '#455A64',
        'text': '#212121'
    }

    # Draw the database cylinder
    cylinder_x = 7
    cylinder_y = 4
    cylinder_width = 2.5
    cylinder_height = 3

    # Top ellipse
    ax.add_patch(patches.Ellipse((cylinder_x, cylinder_y + cylinder_height/2),
                                cylinder_width, cylinder_height/4,
                                facecolor=colors['database'], alpha=0.8))

    # Bottom ellipse
    ax.add_patch(patches.Ellipse((cylinder_x, cylinder_y - cylinder_height/2),
                                cylinder_width, cylinder_height/4,
                                facecolor=colors['database'], alpha=0.8))

    # Rectangle for the body of the cylinder
    ax.add_patch(patches.Rectangle((cylinder_x - cylinder_width/2, cylinder_y - cylinder_height/2),
                                  cylinder_width, cylinder_height,
                                  facecolor=colors['database'], alpha=0.8))

    # Label the database
    ax.text(cylinder_x, cylinder_y - cylinder_height/2 - 0.4, "Database",
            ha='center', va='top', fontsize=14, fontweight='bold', color=colors['text'])

    # Draw three transactions
    transaction_height = 0.8
    transaction_width = 3

    # Transaction 1 - Successful
    tx1_x = 2
    tx1_y = 6
    ax.add_patch(patches.Rectangle((tx1_x, tx1_y), transaction_width, transaction_height,
                                  facecolor=colors['transaction'], alpha=0.8, edgecolor='black'))
    ax.text(tx1_x + transaction_width/2, tx1_y + transaction_height/2, "Transaction 1",
            ha='center', va='center', fontsize=12, fontweight='bold', color='white')

    # Arrow from Transaction 1 to Database
    ax.arrow(tx1_x + transaction_width, tx1_y + transaction_height/2,
             cylinder_x - cylinder_width/2 - tx1_x - transaction_width - 0.2, 0,
             head_width=0.15, head_length=0.15, fc=colors['arrow'], ec=colors['arrow'], linewidth=2)

    # Transaction operations for Tx1
    ax.text(tx1_x + transaction_width/2, tx1_y + transaction_height + 0.3,
            "READ → PROCESS → WRITE → COMMIT", ha='center', va='center',
            fontsize=10, fontweight='bold', color=colors['commit'])

    # Transaction 2 - Failed with Rollback
    tx2_x = 2
    tx2_y = 4
    ax.add_patch(patches.Rectangle((tx2_x, tx2_y), transaction_width, transaction_height,
                                  facecolor=colors['transaction'], alpha=0.8, edgecolor='black'))
    ax.text(tx2_x + transaction_width/2, tx2_y + transaction_height/2, "Transaction 2",
            ha='center', va='center', fontsize=12, fontweight='bold', color='white')

    # Arrow from Transaction 2 to Database
    ax.arrow(tx1_x + transaction_width, tx2_y + transaction_height/2,
             (cylinder_x - cylinder_width/2 - tx1_x - transaction_width - 0.2)/2, 0,
             head_width=0.15, head_length=0.15, fc=colors['arrow'], ec=colors['arrow'], linewidth=2)

    # X mark to indicate rollback
    x_size = 0.2
    x_center_x = tx1_x + transaction_width + (cylinder_x - cylinder_width/2 - tx1_x - transaction_width - 0.2)/2 + 0.3
    x_center_y = tx2_y + transaction_height/2
    ax.plot([x_center_x - x_size, x_center_x + x_size], [x_center_y - x_size, x_center_y + x_size],
            color=colors['rollback'], linewidth=3)
    ax.plot([x_center_x - x_size, x_center_x + x_size], [x_center_y + x_size, x_center_y - x_size],
            color=colors['rollback'], linewidth=3)

    # Transaction operations for Tx2
    ax.text(tx2_x + transaction_width/2, tx2_y + transaction_height + 0.3,
            "READ → PROCESS → ERROR → ROLLBACK", ha='center', va='center',
            fontsize=10, fontweight='bold', color=colors['rollback'])

    # Transaction 3 - In Progress
    tx3_x = 2
    tx3_y = 2
    ax.add_patch(patches.Rectangle((tx3_x, tx3_y), transaction_width, transaction_height,
                                 facecolor=colors['transaction'], alpha=0.8, edgecolor='black'))
    ax.text(tx3_x + transaction_width/2, tx3_y + transaction_height/2, "Transaction 3",
            ha='center', va='center', fontsize=12, fontweight='bold', color='white')

    # Dashed arrow from Transaction 3 to Database
    ax.arrow(tx1_x + transaction_width, tx3_y + transaction_height/2,
             cylinder_x - cylinder_width/2 - tx1_x - transaction_width - 0.2, 0,
             head_width=0.15, head_length=0.15, fc=colors['arrow'], ec=colors['arrow'],
             linewidth=2, linestyle='dashed')

    # Transaction operations for Tx3
    ax.text(tx3_x + transaction_width/2, tx3_y + transaction_height + 0.3,
            "READ → PROCESSING → ...", ha='center', va='center',
            fontsize=10, fontweight='bold', color=colors['text'])

    # Add ACID properties explanation
    properties_x = 2
    properties_y = 8.5

    ax.text(properties_x, properties_y, "ACID Properties:",
            ha='left', va='center', fontsize=16, fontweight='bold', color=colors['text'])

    properties = [
        "• Atomicity: Transactions are all-or-nothing",
        "• Consistency: Database remains valid after transaction",
        "• Isolation: Transactions don't interfere with each other",
        "• Durability: Committed data is permanent"
    ]

    for i, prop in enumerate(properties):
        ax.text(properties_x, properties_y - 0.4 * (i+1), prop,
                ha='left', va='center', fontsize=12, color=colors['text'])

    # Save the figure
    plt.tight_layout()
    plt.savefig('images/transaction.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("Transaction image saved to images/transaction.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)

    # Set random seed for reproducibility
    np.random.seed(42)

    generate_transaction_image()