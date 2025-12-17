import nbformat

def disable_streaming(notebook_path):
    print(f"Disabling streaming in {notebook_path}...")
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        for cell in nb.cells:
            if cell.cell_type == 'code':
                if 'stream = True' in cell.source:
                    print("Found streaming cell. Modifying...")
                    cell.source = cell.source.replace('stream = True', 'stream = False')
        
        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print("SUCCESS: Streaming disabled.")

    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    disable_streaming('/workspaces/Arize_University/lab1and2_base_agent.ipynb')
