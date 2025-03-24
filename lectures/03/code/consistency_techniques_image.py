import matplotlib.pyplot as plt
import os


def generate_consistency_techniques_image():
    """
    Generate an image visualizing different database consistency techniques
    used in distributed database systems.
    """
    print("Generating consistency techniques visualization...")

    # Create a figure with 2x2 subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle('Database Consistency Techniques', fontsize=20, fontweight='bold')

    # Flatten the axes array for easier iteration
    axs = axs.flatten()

    # Example: Subplot 1 - Two-Phase Commit Protocol
    ax1 = axs[0]
    ax1.set_title('Two-Phase Commit Protocol', fontsize=14)
    ax1.axis('off')

    # Here you would add visualization elements for two-phase commit protocol
    # For example: a sequence of steps with arrows showing the protocol flow

    # Example: Subplot 2 - Eventual Consistency
    ax2 = axs[1]
    ax2.set_title('Eventual Consistency', fontsize=14)
    ax2.axis('off')

    # Here you would add visualization elements for eventual consistency
    # For example: nodes gradually converging to the same state over time

    # Example: Subplot 3 - Quorum-Based Consistency
    ax3 = axs[2]
    ax3.set_title('Quorum-Based Consistency', fontsize=14)
    ax3.axis('off')

    # Here you would add visualization elements for quorum-based consistency
    # For example: visualization of read/write quorums

    # Example: Subplot 4 - Compensation-Based Approaches
    ax4 = axs[3]
    ax4.set_title('Compensation-Based Approaches', fontsize=14)
    ax4.axis('off')

    # Here you would add visualization elements for compensation approaches
    # For example: saga pattern with compensating transactions

    # Add general explanation at the bottom
    plt.figtext(
        0.5, 0.01,
        "Different consistency techniques offer varying balances between "
        "data consistency,\n"
        "system availability, and tolerance to network partitions.",
        ha='center', fontsize=10
    )

    # Adjust layout
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.1)

    # Save the figure
    plt.savefig('images/consistency-techniques.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("Consistency techniques image saved to images/consistency-techniques.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_consistency_techniques_image()