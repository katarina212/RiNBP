import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os


def generate_concurrency_problems_image():
    """
    Generate an image visualizing common database concurrency problems.
    """
    print("Generating concurrency problems visualization...")

    # Create figure with 2x2 grid
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    axs = axs.flatten()

    # Common style settings
    timeline_y = 1
    transaction_colors = ['#4CAF50', '#2196F3']  # Green, Blue
    problem_colors = ['#F44336', '#E91E63', '#9C27B0', '#FF5722']  # Red, Pink, Purple, Orange

    # Define the four concurrency problems
    problems = [
        {
            'title': 'Dirty Read',
            'description': 'Transaction reads data that has been modified\nbut not yet committed by another transaction',
            'events': [
                {'tx': 0, 'time': 1, 'action': 'START'},
                {'tx': 0, 'time': 2, 'action': 'WRITE A=100'},
                {'tx': 1, 'time': 3, 'action': 'START'},
                {'tx': 1, 'time': 4, 'action': 'READ A=100'},
                {'tx': 0, 'time': 5, 'action': 'ROLLBACK'},
                {'tx': 1, 'time': 6, 'action': 'USE INVALID A'}
            ]
        },
        {
            'title': 'Non-repeatable Read',
            'description': 'Data read twice within same transaction\nreturns different results',
            'events': [
                {'tx': 0, 'time': 1, 'action': 'START'},
                {'tx': 0, 'time': 2, 'action': 'READ A=100'},
                {'tx': 1, 'time': 3, 'action': 'START'},
                {'tx': 1, 'time': 4, 'action': 'WRITE A=200'},
                {'tx': 1, 'time': 5, 'action': 'COMMIT'},
                {'tx': 0, 'time': 6, 'action': 'READ A=200'},
                {'tx': 0, 'time': 7, 'action': 'INCONSISTENT!'}
            ]
        },
        {
            'title': 'Phantom Read',
            'description': 'Query executed twice returns different\nsets of rows',
            'events': [
                {'tx': 0, 'time': 1, 'action': 'START'},
                {'tx': 0, 'time': 2, 'action': 'SELECT (3 rows)'},
                {'tx': 1, 'time': 3, 'action': 'START'},
                {'tx': 1, 'time': 4, 'action': 'INSERT ROW'},
                {'tx': 1, 'time': 5, 'action': 'COMMIT'},
                {'tx': 0, 'time': 6, 'action': 'SELECT (4 rows)'},
                {'tx': 0, 'time': 7, 'action': 'INCONSISTENT!'}
            ]
        },
        {
            'title': 'Lost Update',
            'description': 'Two transactions update same data\nbut one overwrites the other',
            'events': [
                {'tx': 0, 'time': 1, 'action': 'START'},
                {'tx': 0, 'time': 2, 'action': 'READ A=100'},
                {'tx': 1, 'time': 3, 'action': 'START'},
                {'tx': 1, 'time': 4, 'action': 'READ A=100'},
                {'tx': 0, 'time': 5, 'action': 'WRITE A=150'},
                {'tx': 0, 'time': 6, 'action': 'COMMIT'},
                {'tx': 1, 'time': 7, 'action': 'WRITE A=200'},
                {'tx': 1, 'time': 8, 'action': 'COMMIT (A=150 lost!)'}
            ]
        }
    ]

    # Draw each problem
    for i, (ax, problem) in enumerate(zip(axs, problems)):
        # Set up the plot
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 6)

        # Draw timeline
        ax.plot([1, 9], [timeline_y, timeline_y], 'k-', lw=2)

        # Title and description
        ax.set_title(problem['title'], fontsize=14, pad=10)
        ax.text(5, 5.5, problem['description'], ha='center', va='center',
               fontsize=9, bbox=dict(facecolor='white', alpha=0.7,
                                     boxstyle='round,pad=0.3'))

        # Draw transaction bars
        tx_y_positions = [2, 3.5]  # Y positions for transactions

        # Transaction labels
        for tx_idx, y_pos in enumerate(tx_y_positions):
            ax.text(0.5, y_pos, f'TX {tx_idx+1}', ha='center', va='center',
                   fontsize=10, fontweight='bold', color=transaction_colors[tx_idx])

        # Draw transaction timelines and events
        for tx_idx, y_pos in enumerate(tx_y_positions):
            # Find events for this transaction
            tx_events = [e for e in problem['events'] if e['tx'] == tx_idx]

            if tx_events:
                start_time = tx_events[0]['time']
                end_time = tx_events[-1]['time']

                # Draw transaction bar
                bar = patches.Rectangle((start_time, y_pos - 0.3), end_time - start_time,
                                      0.6, alpha=0.3, facecolor=transaction_colors[tx_idx])
                ax.add_patch(bar)

                # Add events
                for event in tx_events:
                    time = event['time']
                    action = event['action']

                    # Draw event marker
                    ax.plot([time, time], [timeline_y, y_pos], '--',
                           color=transaction_colors[tx_idx], alpha=0.6)
                    ax.scatter(time, y_pos, color=transaction_colors[tx_idx],
                              s=50, zorder=10)

                    # Add action text
                    ax.text(time, y_pos - 0.5, action, ha='center', va='top',
                           fontsize=8, rotation=45, color=transaction_colors[tx_idx])

        # Highlight problem point
        problem_time = problem['events'][-2]['time']
        problem_y = timeline_y + 0.5

        # Draw problem indicator
        ax.scatter(problem_time, problem_y, color=problem_colors[i],
                  s=100, marker='*', zorder=10)
        ax.text(problem_time, problem_y + 0.5, '!', ha='center', va='center',
               fontsize=14, fontweight='bold', color=problem_colors[i])

        # Remove axis
        ax.axis('off')

    # Adjust overall appearance
    plt.suptitle('Common Concurrency Problems in Database Transactions',
                fontsize=16, y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Save the figure
    plt.savefig('images/concurrency-problems.png', dpi=200)
    plt.close()

    print("Concurrency problems image saved to images/concurrency-problems.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_concurrency_problems_image()