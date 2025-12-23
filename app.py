"""
Hugging Face Spaces entry point for Stable Diffusion WebUI.

This file is the main entry point when running on Hugging Face Spaces.
It sets up the appropriate environment variables and command-line arguments
for optimal operation in the Spaces environment.
"""

import os
import sys

# Set environment variables for Hugging Face Spaces
os.environ.setdefault('COMMANDLINE_ARGS', '--listen --port 7860 --skip-torch-cuda-test --no-half --disable-nan-check --skip-install --skip-prepare-environment')

# Disable Gradio analytics
os.environ.setdefault('GRADIO_ANALYTICS_ENABLED', 'False')

# Set Gradio server name for Spaces
os.environ.setdefault('GRADIO_SERVER_NAME', '0.0.0.0')

# Import and run the main webui
if __name__ == "__main__":
    # Parse environment variable for additional arguments
    cmdline_args = os.environ.get('COMMANDLINE_ARGS', '')
    if cmdline_args:
        sys.argv.extend(cmdline_args.split())

    from launch import main
    main()
