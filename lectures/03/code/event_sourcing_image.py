import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os


def generate_event_sourcing_image():
    """
    Generate an image visualizing event sourcing pattern.
    """
    print("Generating event sourcing visualization...")

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Setup plot
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)

    # Define colors
    colors = {
        'event': '#42A5F5',        # Blue
        'command': '#AB47BC',      # Purple
        'read_model': '#66BB6A',   # Green
        'event_store': '#FF7043',  # Orange
        'border': '#455A64',       # Dark gray
        'arrow': '#78909C',        # Light gray
        'text': '#212121',         # Dark text
        'background': '#E1F5FE'    # Light blue background
    }

    # Draw main components
    components = [
        {'name': 'Commands', 'x': 2, 'y': 5.5, 'width': 2, 'height': 1, 'color': colors['command']},
        {'name': 'Event Store', 'x': 5, 'y': 5.5, 'width': 2, 'height': 1, 'color': colors['event_store']},
        {'name': 'Read Model', 'x': 8, 'y': 5.5, 'width': 2, 'height': 1, 'color': colors['read_model']},
        {'name': 'Client Application', 'x': 5, 'y': 1.5, 'width': 3, 'height': 1, 'color': colors['background']}
    ]

    for component in components:
        box = patches.FancyBboxPatch(
            (component['x'] - component['width']/2, component['y'] - component['height']/2),
            component['width'], component['height'],
            boxstyle="round,pad=0.3",
            facecolor=component['color'],
            edgecolor=colors['border'],
            alpha=0.8
        )
        ax.add_patch(box)
        ax.text(component['x'], component['y'], component['name'],
                ha='center', va='center', fontsize=10, fontweight='bold')

    # Draw events
    events = [
        {'name': 'UserCreated', 'x': 4, 'y': 4.2},
        {'name': 'EmailChanged', 'x': 5, 'y': 4.2},
        {'name': 'PasswordChanged', 'x': 6, 'y': 4.2},
        {'name': 'AddressAdded', 'x': 4, 'y': 3.5},
        {'name': 'OrderPlaced', 'x': 5, 'y': 3.5},
        {'name': 'OrderShipped', 'x': 6, 'y': 3.5}
    ]

    for event in events:
        event_box = patches.FancyBboxPatch(
            (event['x'] - 0.6, event['y'] - 0.25),
            1.2, 0.5,
            boxstyle="round,pad=0.2",
            facecolor=colors['event'],
            edgecolor=colors['border'],
            alpha=0.7
        )
        ax.add_patch(event_box)
        ax.text(event['x'], event['y'], event['name'],
                ha='center', va='center', fontsize=8)

    # Draw arrows
    arrows = [
        # Command to Event Store
        {'start': (3, 5.5), 'end': (4, 5.5), 'color': colors['arrow'], 'text': 'submit command'},
        # Event Store to Events
        {'start': (5, 5), 'end': (5, 4.5), 'color': colors['event'], 'text': 'append events'},
        # Events to Read Model
        {'start': (6.5, 4), 'end': (7.5, 5), 'color': colors['event'], 'text': 'project events'},
        # Read Model to Client
        {'start': (7.5, 5), 'end': (6.5, 2), 'color': colors['read_model'], 'text': 'query'},
        # Client to Command
        {'start': (4, 2), 'end': (2.5, 5), 'color': colors['command'], 'text': 'send command'}
    ]

    for arrow in arrows:
        ax.annotate('',
                   xy=arrow['end'],
                   xytext=arrow['start'],
                   arrowprops=dict(facecolor=arrow['color'],
                                  shrink=0.05, width=1.5,
                                  headwidth=8, alpha=0.8))

        # Add text to arrow
        mid_x = (arrow['start'][0] + arrow['end'][0]) / 2
        mid_y = (arrow['start'][1] + arrow['end'][1]) / 2

        # Calculate offset for text based on arrow direction
        dx = arrow['end'][0] - arrow['start'][0]
        dy = arrow['end'][1] - arrow['start'][1]

        # Normalize and perpendicular
        length = (dx**2 + dy**2)**0.5
        if length > 0:
            nx, ny = -dy/length, dx/length
        else:
            nx, ny = 0, 0

        text_offset = 0.3

        ax.text(mid_x + nx * text_offset, mid_y + ny * text_offset,
               arrow['text'], ha='center', va='center', fontsize=8,
               bbox=dict(facecolor='white', alpha=0.7, boxstyle='round,pad=0.1'),
               rotation=0 if abs(dx) > abs(dy) else 90)

    # Draw event stream
    event_stream_x = 5
    event_stream_y = 2.8
    event_stream_width = 3
    event_stream_height = 0.3

    # Draw event stream box
    stream_box = patches.FancyBboxPatch(
        (event_stream_x - event_stream_width/2, event_stream_y - event_stream_height/2),
        event_stream_width, event_stream_height,
        boxstyle="round,pad=0.2",
        facecolor=colors['event_store'],
        edgecolor=colors['border'],
        alpha=0.6
    )
    ax.add_patch(stream_box)

    # Add small event boxes inside the stream
    for i in range(6):
        small_event = patches.Rectangle(
            (event_stream_x - event_stream_width/2 + 0.1 + i * 0.5,
             event_stream_y - event_stream_height/2 + 0.05),
            0.4, 0.2,
            facecolor=colors['event'],
            edgecolor=colors['border'],
            alpha=0.8
        )
        ax.add_patch(small_event)

    # Label the event stream
    ax.text(event_stream_x, event_stream_y - 0.3, "Event Stream (Immutable Log)",
           ha='center', va='center', fontsize=8, fontweight='bold')

    # Add explanation
    explanation = (
        "Event Sourcing Pattern:\n"
        "• State is stored as a sequence of events, not as current state\n"
        "• Events represent facts that have happened in the system\n"
        "• Current state is derived by replaying events\n"
        "• History and audit trail come for free\n"
        "• Enables eventual consistency and CQRS"
    )

    # Add explanation text box
    explanation_box = patches.FancyBboxPatch(
        (0.5, 6), 3, 1.5,
        boxstyle="round,pad=0.3",
        facecolor='white',
        edgecolor=colors['border'],
        alpha=0.8
    )
    ax.add_patch(explanation_box)

    ax.text(2, 6.75, explanation, ha='center', va='center',
           fontsize=8, color=colors['text'])

    # Add title
    ax.set_title("Event Sourcing Pattern", fontsize=14, pad=10)

    # Hide axes
    ax.axis('off')

    # Save the figure
    plt.tight_layout()
    plt.savefig('images/event-sourcing.png', dpi=200)
    plt.close()

    print("Event sourcing image saved to images/event-sourcing.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_event_sourcing_image()