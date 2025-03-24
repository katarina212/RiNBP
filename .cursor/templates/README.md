# Cursor Templates for Lecture

This directory contains templates for creating consistent and high-quality content across the course materials.

## Available Templates

### Image Generation

- **[`image_generation_template.py`](image_generation_template.py)**: A template Python script for generating images to support lecture slides.
  - Includes functions for creating and saving network visualizations
  - Demonstrates proper organization of image generation code
  - Contains examples for creating different types of visualizations
  - Follows the guidelines in the [Lecture Image Generation](../rules/lecture-image-generation.mdc) rule

## Using These Templates

### For New Lecture Materials

1. Copy the appropriate template to your lecture directory:
   ```bash
   cp .cursor/templates/image_generation_template.py lectures/XX/generate_images.py
   ```

2. Customize the template for your specific lecture needs:
   - Modify the image generation functions
   - Add new functions for specific visualizations
   - Update the main function to generate all required images

3. Run the script to generate images:
   ```bash
   cd lectures/XX
   python generate_images.py
   ```

### Template Customization

When customizing templates, maintain the general structure and organization to ensure consistency. You can:

- Add new functions for specific visualization types
- Modify parameters and styling to match your lecture theme
- Update documentation and comments to reflect your changes
- Extend functionality while following the established patterns

## Adding New Templates

If you create a useful template that could benefit others, consider adding it to this directory:

1. Create your template with thorough documentation
2. Update this README to include your new template
3. Reference relevant rules that the template follows

## Related Rules

Templates in this directory follow the guidelines specified in these rules:

- [Lecture Image Generation](../rules/lecture-image-generation.mdc)
- [Lecture Image Linking](../rules/lecture-image-linking.mdc)
- [Marp Directives and Styling](../rules/marp-directives-styling.mdc)