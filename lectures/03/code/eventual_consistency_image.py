import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os


def generate_eventual_consistency_image():
    """
    Generate an image visualizing eventual consistency in distributed databases.
    """
    print("Generating eventual consistency visualization...")

    # Create figure
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8),
                                       gridspec_kw={'height_ratios': [1, 1, 1]})

    # Common styling
    node_colors = ['#42A5F5', '#66BB6A', '#FFA726']  # Blue, Green, Orange
    node_labels = ['Node 1', 'Node 2', 'Node 3']
    time_points = np.arange(1, 10)

    # Data values at each time point for each node
    # Initially all nodes have value 5
    # At t=3, Node 1 updates to 10
    # Eventually all nodes get the updated value
    data = [
        [5, 5, 10, 10, 10, 10, 10, 10, 10],  # Node 1
        [5, 5, 5, 5, 10, 10, 10, 10, 10],    # Node 2
        [5, 5, 5, 5, 5, 5, 10, 10, 10]       # Node 3
    ]

    # Events at specific time points
    events = [
        (3, 0, "Write: X=10"),   # At t=3, Node 1 writes X=10
        (5, 1, "Sync"),          # At t=5, Node 2 syncs with Node 1
        (7, 2, "Sync")           # At t=7, Node 3 syncs with Node 1 or 2
    ]

    # Panel 1: Time-series view of data consistency
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 15)

    # Draw timeline
    ax1.plot([1, 9], [1, 1], 'k-', lw=1)
    for t in time_points:
        ax1.plot([t, t], [0.8, 1.2], 'k-', lw=1)
        ax1.text(t, 0.4, f"t={t}", ha='center', va='center', fontsize=9)

    # Draw data values for each node over time
    for i, (node_data, color, label) in enumerate(zip(data, node_colors, node_labels)):
        y_pos = i * 2 + 3
        ax1.plot(time_points, node_data, '-o', color=color, lw=2)
        ax1.text(0.5, y_pos, label, ha='center', va='center',
                color=color, fontweight='bold')

    # Add events
    for t, node, text in events:
        ax1.annotate(text,
                    xy=(t, data[node][t-1]),
                    xytext=(t, data[node][t-1] + 1.5),
                    ha='center',
                    arrowprops=dict(arrowstyle="->", color=node_colors[node]),
                    bbox=dict(boxstyle="round,pad=0.3",
                             facecolor='white', alpha=0.8),
                    fontsize=9)

    ax1.set_title("System Convergence Over Time", fontsize=12)
    ax1.set_ylabel("Value of X")
    ax1.set_yticks([5, 10])
    ax1.grid(True, alpha=0.3)

    # Panel 2: Distributed nodes at t=4 (inconsistent state)
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 5)

    # Draw distributed nodes
    for i, (color, label, value) in enumerate(zip(node_colors, node_labels,
                                                 [data[0][3], data[1][3], data[2][3]])):
        x_pos = (i + 1) * 3 - 1

        # Draw node
        circle = patches.Circle((x_pos, 2.5), 0.8,
                               facecolor=color, alpha=0.7,
                               edgecolor='black', linewidth=1)
        ax2.add_patch(circle)

        # Add label
        ax2.text(x_pos, 2.5, f"X={value}", ha='center', va='center',
                color='white', fontweight='bold')
        ax2.text(x_pos, 1, label, ha='center', va='center', fontsize=10)

    # Add connections between nodes
    connection_points = [(2, 2.5), (5, 2.5), (8, 2.5)]

    # Connect Node 1 and Node 2
    ax2.plot([connection_points[0][0], connection_points[1][0]],
             [connection_points[0][1], connection_points[1][1]],
             'k--', alpha=0.5)

    # Connect Node 2 and Node 3
    ax2.plot([connection_points[1][0], connection_points[2][0]],
             [connection_points[1][1], connection_points[2][1]],
             'k--', alpha=0.5)

    # Add title and timestamp
    ax2.set_title("t=4: Inconsistent State (During Propagation)", fontsize=12)
    ax2.text(5, 4, "Some nodes have not yet received the update",
            ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='#FFECB3', alpha=0.8))

    # Remove axis
    ax2.axis('off')

    # Panel 3: Distributed nodes at t=8 (consistent state)
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 5)

    # Draw distributed nodes
    for i, (color, label, value) in enumerate(zip(node_colors, node_labels,
                                                 [data[0][7], data[1][7], data[2][7]])):
        x_pos = (i + 1) * 3 - 1

        # Draw node
        circle = patches.Circle((x_pos, 2.5), 0.8,
                               facecolor=color, alpha=0.7,
                               edgecolor='black', linewidth=1)
        ax3.add_patch(circle)

        # Add label
        ax3.text(x_pos, 2.5, f"X={value}", ha='center', va='center',
                color='white', fontweight='bold')
        ax3.text(x_pos, 1, label, ha='center', va='center', fontsize=10)

    # Add connections between nodes (same as in ax2)
    ax3.plot([connection_points[0][0], connection_points[1][0]],
             [connection_points[0][1], connection_points[1][1]],
             'k--', alpha=0.5)

    ax3.plot([connection_points[1][0], connection_points[2][0]],
             [connection_points[1][1], connection_points[2][1]],
             'k--', alpha=0.5)

    # Add title and timestamp
    ax3.set_title("t=8: Consistent State (After Propagation)", fontsize=12)
    ax3.text(5, 4, "All nodes have now received the update",
            ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='#C8E6C9', alpha=0.8))

    # Remove axis
    ax3.axis('off')

    # Add overall title
    fig.suptitle('Eventual Consistency: Data Propagation in Distributed Systems',
                fontsize=14, y=0.98)

    # Add explanation text
    fig.text(0.5, 0.03,
            'Eventual consistency guarantees that if no new updates are made to a given data item,\n'
            'eventually all replicas will converge to the same value.',
            ha='center', fontsize=10, fontweight='bold')

    # Adjust spacing
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.savefig('images/eventual-consistency.png', dpi=200)
    plt.close()

    print("Eventual consistency image saved to images/eventual-consistency.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_eventual_consistency_image()