"""
Hugging Face Spaces entry point for Stable Diffusion WebUI.

This file is the main entry point when running on Hugging Face Spaces.
It sets up the appropriate environment variables and command-line arguments
for optimal operation in the Spaces environment.
"""

import os
import sys

# Default command-line arguments for Hugging Face Spaces
DEFAULT_SPACES_ARGS = [
    '--listen',
    '--port', '7860',
    '--skip-torch-cuda-test',
    '--no-half',
    '--disable-nan-check',
    '--skip-install',
    '--skip-prepare-environment',
]

# Disable Gradio analytics
os.environ.setdefault('GRADIO_ANALYTICS_ENABLED', 'False')

# Set Gradio server name for Spaces
os.environ.setdefault('GRADIO_SERVER_NAME', '0.0.0.0')

# Import and run the main webui
if __name__ == "__main__":
    # Add default Spaces arguments if not already set via COMMANDLINE_ARGS
    cmdline_args = os.environ.get('COMMANDLINE_ARGS', '')
    if cmdline_args:
        # Use user-provided arguments from environment
        sys.argv.extend(cmdline_args.split())
    else:
        # Use default Spaces arguments
        sys.argv.extend(DEFAULT_SPACES_ARGS)

    from launch import main
    main()
