import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as mpath
import numpy as np
import os


def generate_complex_joins_image():
    """
    Generate an image visualizing complex joins in database queries.
    """
    print("Generating complex joins visualization...")

    # Create a figure with 2 rows and 2 columns for the different join types
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    # flatten the axs array for easier iteration
    axs = axs.flatten()

    # Set the figure title
    fig.suptitle('SQL JOIN Operations', fontsize=24, fontweight='bold', y=0.98)
    fig.patch.set_facecolor('#f8f9fa')

    # Define colors for different elements
    colors = {
        'table_a': '#4285F4',      # Blue
        'table_b': '#34A853',      # Green
        'intersection': '#673AB7', # Purple
        'text': '#212121',         # Dark text
        'highlight': '#F44336',    # Red highlight
        'background': '#f8f9fa',   # Light gray background
    }

    # Define the join types and their data
    join_types = [
        {
            'name': 'INNER JOIN',
            'description': 'Returns rows when there is a match in both tables',
            'highlight': 'intersection',
            'ax_index': 0
        },
        {
            'name': 'LEFT JOIN',
            'description': 'Returns all rows from the left table, and matched rows from the right',
            'highlight': 'left',
            'ax_index': 1
        },
        {
            'name': 'RIGHT JOIN',
            'description': 'Returns all rows from the right table, and matched rows from the left',
            'highlight': 'right',
            'ax_index': 2
        },
        {
            'name': 'FULL OUTER JOIN',
            'description': 'Returns rows when there is a match in one of the tables',
            'highlight': 'full',
            'ax_index': 3
        }
    ]

    # Draw the visualizations for each join type
    for join_type in join_types:
        ax_idx = join_type['ax_index']
        ax = axs[ax_idx]

        # Set up the plot
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.set_facecolor(colors['background'])
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)

        # Title for this join type
        ax.set_title(join_type['name'], fontsize=18, fontweight='bold', pad=10)

        # Draw the Venn diagram
        circle_radius = 2
        circle1_center = (4, 4)
        circle2_center = (6, 4)

        # Draw the circles (tables)
        circle1 = plt.Circle(circle1_center, circle_radius, alpha=0.6, fc=colors['table_a'], ec='black')
        circle2 = plt.Circle(circle2_center, circle_radius, alpha=0.6, fc=colors['table_b'], ec='black')

        # Add the circles to the plot
        ax.add_patch(circle1)
        ax.add_patch(circle2)

        # Label the tables
        ax.text(circle1_center[0] - 1, circle1_center[1], "Table A",
                fontsize=14, fontweight='bold', ha='center', va='center')
        ax.text(circle2_center[0] + 1, circle2_center[1], "Table B",
                fontsize=14, fontweight='bold', ha='center', va='center')

        # Add some sample rows to each circle
        table_a_rows = [
            "id: 1, name: 'Apple'",
            "id: 2, name: 'Banana'",
            "id: 3, name: 'Cherry'"
        ]

        table_b_rows = [
            "id: 2, price: '$1.50'",
            "id: 3, price: '$2.00'",
            "id: 4, price: '$3.25'"
        ]

        # Position the sample rows
        for i, row in enumerate(table_a_rows):
            y_offset = 0.5 * (i - 1)
            ax.text(circle1_center[0] - 1, circle1_center[1] + y_offset, row,
                    fontsize=9, ha='center', va='center')

        for i, row in enumerate(table_b_rows):
            y_offset = 0.5 * (i - 1)
            ax.text(circle2_center[0] + 1, circle2_center[1] + y_offset, row,
                    fontsize=9, ha='center', va='center')

        # Highlight the appropriate section based on join type
        if join_type['highlight'] == 'intersection':
            # Highlight the intersection for INNER JOIN
            intersection = plt.Circle((5, 4), 0.8, fc=colors['highlight'], ec='none', alpha=0.5)
            ax.add_patch(intersection)
            ax.text(5, 4, "Matching\nRows", fontsize=10, ha='center', va='center')

        elif join_type['highlight'] == 'left':
            # Highlight the left circle for LEFT JOIN
            left_highlight = plt.Circle(circle1_center, circle_radius, fc=colors['highlight'], ec='none', alpha=0.3)
            ax.add_patch(left_highlight)

        elif join_type['highlight'] == 'right':
            # Highlight the right circle for RIGHT JOIN
            right_highlight = plt.Circle(circle2_center, circle_radius, fc=colors['highlight'], ec='none', alpha=0.3)
            ax.add_patch(right_highlight)

        elif join_type['highlight'] == 'full':
            # Create a path for the full outer join (both circles)
            left_highlight = plt.Circle(circle1_center, circle_radius, fc=colors['highlight'], ec='none', alpha=0.3)
            right_highlight = plt.Circle(circle2_center, circle_radius, fc=colors['highlight'], ec='none', alpha=0.3)
            ax.add_patch(left_highlight)
            ax.add_patch(right_highlight)

        # Add SQL query example
        query_text = f"""
        SELECT
            A.id, A.name, B.price
        FROM
            TableA A
        {join_type['name']}
            TableB B ON A.id = B.id
        """

        # Draw a box for the SQL query
        query_box = patches.Rectangle((1.5, 1), 7, 1.5, fc='white', ec='black', alpha=0.8)
        ax.add_patch(query_box)

        # Add the query text
        ax.text(5, 1.8, query_text, fontsize=10, ha='center', va='center', family='monospace')

        # Add a description of the join
        ax.text(5, 6.5, join_type['description'], fontsize=12, ha='center', va='center')

    # Add a sample result set for the INNER JOIN (axs[0])
    result_text = """
    Result of INNER JOIN:
    | id | name    | price  |
    |----|---------|--------|
    | 2  | Banana  | $1.50  |
    | 3  | Cherry  | $2.00  |
    """
    axs[0].text(2, 2.8, result_text, fontsize=8, ha='left', va='center', family='monospace', bbox=dict(facecolor='white', alpha=0.5))

    # Create an explanation of when to use complex joins
    complex_join_info = """
    When to use complex joins:
    • Multi-table data retrieval needs
    • Data analysis requiring related information
    • Reporting across multiple related tables
    • Complex business rules involving multiple entities
    """

    # Add this explanation to the bottom of the figure
    fig.text(0.5, 0.02, complex_join_info, fontsize=10, ha='center', va='center',
             bbox=dict(facecolor='#E3F2FD', alpha=0.8, boxstyle='round,pad=0.5'))

    # Add notes about performance considerations
    performance_note = """
    Performance considerations:
    - Joins can be expensive operations
    - Proper indexing is crucial for performance
    - Consider denormalization for frequent complex joins
    """

    fig.text(0.9, 0.5, performance_note, fontsize=9, ha='right', va='center',
             rotation=-90, bbox=dict(facecolor='#FFF3E0', alpha=0.8, boxstyle='round,pad=0.5'))

    # Save the figure
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust the layout to make room for the title
    plt.savefig('images/complex-joins.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("Complex joins image saved to images/complex-joins.png")


def generate_join_diagram(ax, title, highlight_area, description):
    """
    Helper function to generate a join diagram on the given axis.
    """
    # Set up the plot
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)

    # Implementation details would go here
    pass


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)

    # Set random seed for reproducibility
    np.random.seed(42)

    generate_complex_joins_image()