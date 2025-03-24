import matplotlib.pyplot as plt
import numpy as np
import os


def generate_isolation_levels_image():
    """
    Generate an image visualizing different database isolation levels.
    """
    print("Generating isolation levels visualization...")

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 7))

    # Set up the plot
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Define colors
    colors = {
        'read_uncommitted': '#ffcdd2',  # Light red
        'read_committed': '#fff9c4',    # Light yellow
        'repeatable_read': '#c8e6c9',   # Light green
        'serializable': '#bbdefb',      # Light blue
        'border': '#616161',            # Dark gray
        'text': '#212121'               # Nearly black
    }

    # Create pyramid for isolation levels
    level_heights = [2, 3, 4, 5]
    level_widths = [8, 6, 4, 2]
    level_bottoms = [0, 2, 5, 9]
    level_names = ['Read Uncommitted', 'Read Committed',
                  'Repeatable Read', 'Serializable']
    level_colors = [colors['read_uncommitted'], colors['read_committed'],
                   colors['repeatable_read'], colors['serializable']]

    # Draw each level
    for i, (height, width, bottom, name, color) in enumerate(
            zip(level_heights, level_widths, level_bottoms, level_names, level_colors)):
        left = (10 - width) / 2
        rect = plt.Rectangle((left, bottom), width, height,
                            facecolor=color, edgecolor=colors['border'],
                            linewidth=1.5, alpha=0.8)
        ax.add_patch(rect)

        # Add level name
        ax.text(5, bottom + height/2, name,
                ha='center', va='center',
                fontsize=14, fontweight='bold', color=colors['text'])

        # Add problem icons and description for all but serializable
        if i < 3:
            problems = [
                "Dirty Reads",
                "Non-Repeatable Reads",
                "Phantom Reads"
            ]

            problem_text = problems[i]

            # Show which problems are prevented
            if i == 0:
                problem_status = "❌ Not prevented"
            elif i == 1:
                problem_status = "✓ Prevented"
            elif i == 2:
                problem_status = "✓ Prevented"

            ax.text(8.5, bottom + height/2, problem_status,
                    ha='center', va='center',
                    fontsize=10, color=colors['text'],
                    bbox=dict(facecolor='white', alpha=0.7,
                             boxstyle='round,pad=0.3'))

            ax.text(1.5, bottom + height/2, problem_text,
                    ha='center', va='center',
                    fontsize=10, color=colors['text'],
                    bbox=dict(facecolor='white', alpha=0.7,
                             boxstyle='round,pad=0.3'))

    # Draw arrows for the trade-offs
    ax.annotate('Stronger Isolation',
                xy=(9, 5), xytext=(9, 2),
                arrowprops=dict(facecolor='green', shrink=0.05, width=2),
                ha='center', va='center', fontsize=12)

    ax.annotate('Better Performance',
                xy=(1, 2), xytext=(1, 5),
                arrowprops=dict(facecolor='blue', shrink=0.05, width=2),
                ha='center', va='center', fontsize=12)

    # Add overall title and explanation
    ax.set_title('Database Isolation Levels: Strength vs. Performance',
                fontsize=16, pad=20)

    fig.text(0.5, 0.02,
             'Higher isolation levels provide stronger guarantees but may reduce performance.\n'
             'Lower isolation levels offer better performance but with weaker consistency guarantees.',
             ha='center', fontsize=12, fontweight='bold')

    # Remove axes
    ax.axis('off')

    # Save the figure
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.savefig('images/isolation-levels.png', dpi=200)
    plt.close()

    print("Isolation levels image saved to images/isolation-levels.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_isolation_levels_image()