import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os


def generate_distributed_transactions_image():
    """
    Generate an image visualizing distributed database transactions.
    """
    print("Generating distributed transactions visualization...")

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Set up plot area
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)

    # Color palette
    colors = {
        'coordinator': '#D81B60',  # Pink
        'db1': '#1E88E5',          # Blue
        'db2': '#43A047',          # Green
        'db3': '#F57C00',          # Orange
        'client': '#5E35B1',       # Purple
        'network': '#B0BEC5',      # Gray
        'success': '#A5D6A7',      # Light green
        'failure': '#FFCDD2'       # Light red
    }

    # Create network cloud
    cloud_x, cloud_y = 5, 3
    cloud_w, cloud_h = 6, 2

    # Draw network cloud
    cloud = patches.Ellipse((cloud_x, cloud_y), cloud_w, cloud_h,
                           angle=0, alpha=0.2, facecolor=colors['network'],
                           edgecolor='gray', linewidth=1)
    ax.add_patch(cloud)
    ax.text(cloud_x, cloud_y, 'Network', ha='center', va='center',
           fontsize=12, fontweight='bold', color='gray')

    # Define database positions
    coord_pos = (5, 1)
    db_positions = [
        (2, 5),  # DB1
        (5, 5),  # DB2
        (8, 5)   # DB3
    ]
    client_pos = (1, 1)

    # Draw coordinator
    coord_rect = patches.Rectangle((coord_pos[0]-0.8, coord_pos[1]-0.5), 1.6, 1,
                                  facecolor=colors['coordinator'], alpha=0.7,
                                  edgecolor='black', linewidth=1)
    ax.add_patch(coord_rect)
    ax.text(coord_pos[0], coord_pos[1], 'Coordinator', ha='center', va='center',
           fontsize=10, fontweight='bold', color='white')

    # Draw databases
    db_names = ['Orders DB', 'Inventory DB', 'Payment DB']

    for i, (x, y) in enumerate(db_positions):
        db_color = [colors['db1'], colors['db2'], colors['db3']][i]
        db_rect = patches.Rectangle((x-0.8, y-0.5), 1.6, 1,
                                   facecolor=db_color, alpha=0.7,
                                   edgecolor='black', linewidth=1)
        ax.add_patch(db_rect)
        ax.text(x, y, db_names[i], ha='center', va='center',
               fontsize=10, fontweight='bold', color='white')

    # Draw client
    client_rect = patches.Rectangle((client_pos[0]-0.8, client_pos[1]-0.5), 1.6, 1,
                                   facecolor=colors['client'], alpha=0.7,
                                   edgecolor='black', linewidth=1)
    ax.add_patch(client_rect)
    ax.text(client_pos[0], client_pos[1], 'Client', ha='center', va='center',
           fontsize=10, fontweight='bold', color='white')

    # Draw connections
    # Client to coordinator
    ax.plot([client_pos[0]+0.8, coord_pos[0]-0.8],
            [client_pos[1], coord_pos[1]],
            'k-', linewidth=1.5, alpha=0.6)

    # Coordinator to databases
    for db_pos in db_positions:
        ax.plot([coord_pos[0], db_pos[0]],
                [coord_pos[1]+0.5, db_pos[1]-0.5],
                'k-', linewidth=1.5, alpha=0.6)

    # Add transaction flow arrows
    # 1. Client sends request
    ax.arrow(client_pos[0]+0.4, client_pos[1]+0.2,
            0.8, 0, head_width=0.1, head_length=0.2,
            fc=colors['client'], ec='none', linewidth=2)

    # 2. Coordinator sends prepare
    for i, db_pos in enumerate(db_positions):
        db_color = [colors['db1'], colors['db2'], colors['db3']][i]
        dx = db_pos[0] - coord_pos[0]
        dy = db_pos[1] - coord_pos[1] - 0.5
        arrow_len = np.sqrt(dx**2 + dy**2)
        ax.arrow(coord_pos[0], coord_pos[1]+0.3,
                dx*0.7/arrow_len, dy*0.7/arrow_len,
                head_width=0.1, head_length=0.2,
                fc=colors['coordinator'], ec='none', linewidth=2)

    # 3. Databases respond
    for i, db_pos in enumerate(db_positions):
        db_color = [colors['db1'], colors['db2'], colors['db3']][i]
        dx = coord_pos[0] - db_pos[0]
        dy = coord_pos[1] - db_pos[1] + 0.5
        arrow_len = np.sqrt(dx**2 + dy**2)

        # For illustration, show 2 successful and 1 failed response
        if i != 1:  # Success
            response_color = colors['success']
            response_text = 'Yes'
        else:  # Failure
            response_color = colors['failure']
            response_text = 'No'

        # Draw arrow
        ax.arrow(db_pos[0], db_pos[1]-0.3,
                dx*0.5/arrow_len, dy*0.5/arrow_len,
                head_width=0.1, head_length=0.2,
                fc=db_color, ec='none', linewidth=2)

        # Add response indicator
        response_x = db_pos[0] + dx*0.3/arrow_len
        response_y = db_pos[1] + dy*0.3/arrow_len
        response_circle = patches.Circle((response_x, response_y), 0.2,
                                        facecolor=response_color, alpha=0.9,
                                        edgecolor='black', linewidth=1)
        ax.add_patch(response_circle)
        ax.text(response_x, response_y, response_text, ha='center', va='center',
               fontsize=8, fontweight='bold')

    # 4. Coordinator sends abort
    for i, db_pos in enumerate(db_positions):
        if i == 1:  # Skip the failing DB since it already said no
            continue

        db_color = [colors['db1'], colors['db2'], colors['db3']][i]
        dx = db_pos[0] - coord_pos[0]
        dy = db_pos[1] - coord_pos[1] - 0.5
        arrow_len = np.sqrt(dx**2 + dy**2)

        # Draw arrow
        ax.arrow(coord_pos[0]+0.3, coord_pos[1]+0.3,
                dx*0.2/arrow_len, dy*0.2/arrow_len,
                head_width=0.1, head_length=0.2,
                fc='red', ec='none', linewidth=2)

        # Add abort indicator
        abort_x = coord_pos[0] + dx*0.4/arrow_len
        abort_y = coord_pos[1] + dy*0.4/arrow_len + 0.3
        abort_circle = patches.Circle((abort_x, abort_y), 0.2,
                                     facecolor=colors['failure'], alpha=0.9,
                                     edgecolor='black', linewidth=1)
        ax.add_patch(abort_circle)
        ax.text(abort_x, abort_y, 'Abort', ha='center', va='center',
               fontsize=6, fontweight='bold')

    # 5. Coordinator responds to client
    ax.arrow(coord_pos[0]-0.4, coord_pos[1]-0.2,
            -0.8, 0, head_width=0.1, head_length=0.2,
            fc='red', ec='none', linewidth=2)

    # Add final transaction status
    ax.text(3, 0.5, 'Transaction Aborted - Not All Participants Agreed',
           ha='center', va='center', color='red', fontsize=12, fontweight='bold',
           bbox=dict(facecolor='white', edgecolor='red', alpha=0.7,
                    boxstyle='round,pad=0.3'))

    # Add title
    ax.set_title('Distributed Transaction with Two-Phase Commit Protocol',
                fontsize=14, pad=10)

    # Remove axes
    ax.axis('off')

    # Save the figure
    plt.tight_layout()
    plt.savefig('images/distributed-transactions.png', dpi=200)
    plt.close()

    print("Distributed transactions image saved to images/distributed-transactions.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_distributed_transactions_image()