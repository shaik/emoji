import os

def is_relevant_file(filename):
    """Check if the file is a relevant source file."""
    return filename.endswith(('.py', '.js', '.html', '.css'))

def write_file_contents(root, filename, output_file):
    """Write the contents of a file to the output file."""
    with open(os.path.join(root, filename), 'r') as file:
        output_file.write(f"{'=' * 20}\n")
        output_file.write(f"File: {os.path.join(root, filename)}\n")
        output_file.write(f"{'=' * 20}\n\n")
        output_file.write(file.read())
        output_file.write("\n\n")

def generate_printout(root_directory, output_filename='application_printout.txt'):
    """Generate a printout of all relevant files in the application."""
    with open(output_filename, 'w') as output_file:
        for root, dirs, files in os.walk(root_directory):
            # Exclude specific directories
            dirs[:] = [d for d in dirs if d not in ['static', 'data', '.git', '__pycache__']]
            for filename in files:
                if is_relevant_file(filename):
                    write_file_contents(root, filename, output_file)
    print(f"Printout generated: {output_filename}")

# Set the root directory of your Flask app
root_directory = '.'  # Current directory (or specify the path to your project root)
generate_printout(root_directory)
