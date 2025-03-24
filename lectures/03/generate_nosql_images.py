import os
import importlib.util
import sys


def load_module(name, path):
    """Load a Python module from a file path."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    """Run all image generation scripts from the code directory."""
    # Ensure images directory exists
    os.makedirs('images', exist_ok=True)

    # List of image generation modules
    image_modules = [
        "trade_offs_image",
        "normalization_image",
        "complex_joins_image",
        "denormalization_image",
        "transaction_image",
        "consistency_techniques_image",
        "isolation_levels_image",
        "concurrency_problems_image",
        "distributed_transactions_image",
        "two_phase_commit_image",
        "two_phase_example_image",
        "eventual_consistency_image",
        "atomicity_image",
        "consistency_image",
        "isolation_image",
        "durability_image",
        "saga_pattern_image",
        "saga_example_image",
        "event_sourcing_image",
        "key_takeaways_image",
        "norm_vs_denorm_image",
        "acid_vs_base_image"
    ]

    # Import and run each module
    for module_name in image_modules:
        file_path = f"code/{module_name}.py"

        # Skip if file doesn't exist
        if not os.path.exists(file_path):
            print(f"Warning: {file_path} not found. Skipping.")
            continue

        try:
            # Load and run the module
            print(f"Running {module_name}...")
            module = load_module(module_name, file_path)

            # Get the main generation function (assumed to be generate_X_image)
            generator_func = getattr(module, f"generate_{module_name}")
            generator_func()

        except Exception as e:
            print(f"Error in {module_name}: {str(e)}")


if __name__ == "__main__":
    main()
    print("Image generation completed!")
