import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os


def generate_key_takeaways_image():
    """
    Generate an image visualizing key takeaways for denormalization and transactions.
    """
    print("Generating key takeaways visualization...")

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Setup plot
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Define colors
    colors = {
        'header': '#1976D2',       # Dark Blue
        'item1': '#42A5F5',        # Blue
        'item2': '#66BB6A',        # Green
        'item3': '#FFCA28',        # Yellow
        'item4': '#FF7043',        # Orange
        'item5': '#EC407A',        # Pink
        'border': '#37474F',       # Dark Gray
        'text': '#FFFFFF',         # White text
        'dark_text': '#212121',    # Dark text
        'arrow': '#455A64'         # Arrow color
    }

    # Define takeaway boxes with different colors
    takeaways = [
        {
            'text': 'Denormalization is a conscious design choice,\nnot an accident',
            'x': 5, 'y': 8, 'width': 8, 'height': 1.2,
            'color': colors['item1']
        },
        {
            'text': 'Transactions are essential for maintaining\nintegrity in distributed systems',
            'x': 5, 'y': 6.5, 'width': 8, 'height': 1.2,
            'color': colors['item2']
        },
        {
            'text': 'NoSQL systems offer different trade-offs\nbetween consistency and availability',
            'x': 5, 'y': 5, 'width': 8, 'height': 1.2,
            'color': colors['item3']
        },
        {
            'text': 'Understanding your specific requirements\nis key to choosing the right strategy',
            'x': 5, 'y': 3.5, 'width': 8, 'height': 1.2,
            'color': colors['item4']
        },
        {
            'text': 'Practical solutions often combine multiple\napproaches for optimal results',
            'x': 5, 'y': 2, 'width': 8, 'height': 1.2,
            'color': colors['item5']
        }
    ]

    # Add header
    header_box = patches.FancyBboxPatch(
        (1, 9.2), 8, 0.6,
        boxstyle="round,pad=0.3",
        facecolor=colors['header'],
        edgecolor=colors['border'],
        alpha=0.9
    )
    ax.add_patch(header_box)
    ax.text(5, 9.5, "Key Takeaways: Denormalization and Transactions",
           ha='center', va='center', fontsize=14,
           color=colors['text'], fontweight='bold')

    # Draw takeaway boxes
    for i, takeaway in enumerate(takeaways):
        # Create box with left side emphasis
        main_box = patches.FancyBboxPatch(
            (takeaway['x'] - takeaway['width']/2, takeaway['y'] - takeaway['height']/2),
            takeaway['width'], takeaway['height'],
            boxstyle="round,pad=0.3",
            facecolor=takeaway['color'],
            edgecolor=colors['border'],
            alpha=0.8
        )
        ax.add_patch(main_box)

        # Create number bubble
        circle_radius = 0.4
        circle = patches.Circle(
            (takeaway['x'] - takeaway['width']/2 + circle_radius + 0.1,
             takeaway['y']),
            circle_radius,
            facecolor='white',
            edgecolor=takeaway['color'],
            alpha=0.9
        )
        ax.add_patch(circle)

        # Add number
        ax.text(takeaway['x'] - takeaway['width']/2 + circle_radius + 0.1,
               takeaway['y'], str(i+1),
               ha='center', va='center', fontsize=14,
               color=takeaway['color'], fontweight='bold')

        # Add takeaway text
        ax.text(takeaway['x'] + 0.5, takeaway['y'], takeaway['text'],
               ha='center', va='center', fontsize=11,
               color=colors['text'], fontweight='bold')

    # Add connecting arrows between items
    for i in range(len(takeaways) - 1):
        current = takeaways[i]
        next_item = takeaways[i + 1]

        ax.arrow(current['x'] - 2, current['y'] - current['height']/2,
                0, next_item['y'] - current['y'] + current['height']/2,
                head_width=0.2, head_length=0.2, fc=colors['arrow'], ec=colors['arrow'],
                alpha=0.6, length_includes_head=True)

    # Add "Balance" text on the left side
    balance_points = [
        (1.5, 7.25, "Performance\nvs.\nConsistency"),
        (1.5, 4.25, "Scalability\nvs.\nReliability")
    ]

    for x, y, text in balance_points:
        balance_box = patches.FancyBboxPatch(
            (x - 0.8, y - 0.8), 1.6, 1.6,
            boxstyle="round,pad=0.3",
            facecolor='white',
            edgecolor=colors['border'],
            alpha=0.7
        )
        ax.add_patch(balance_box)
        ax.text(x, y, text, ha='center', va='center',
               fontsize=9, color=colors['dark_text'])

    # Hide axes
    ax.axis('off')

    # Save the figure
    plt.tight_layout()
    plt.savefig('images/key-takeaways.png', dpi=200)
    plt.close()

    print("Key takeaways image saved to images/key-takeaways.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_key_takeaways_image()