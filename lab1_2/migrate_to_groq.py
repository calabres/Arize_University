import nbformat
import re

def migrate_to_groq(notebook_path):
    print(f"Migrating {notebook_path} to Groq...")
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # API Keys
        keys_map = {
            "ARIZE_SPACE_ID": "YOUR_SPACE_ID",
            "ARIZE_API_KEY": "YOUR_ARIZE_API_KEY",
            "GROQ_API_KEY": "YOUR_GROQ_API_KEY",
            "TAVILY_API_KEY": "YOUR_TAVILY_API_KEY"
        }

        for cell in nb.cells:
            if cell.cell_type == 'code':
                original_source = cell.source
                new_source = original_source
                
                # 1. Pip Install
                if '!pip install' in new_source and 'openai' in new_source:
                    new_source = new_source.replace('openai', 'groq')
                    new_source = new_source.replace('openinference-instrumentation-openai', 'openinference-instrumentation-groq')
                
                # 2. Imports & Instrumentation
                if 'openinference.instrumentation.openai' in new_source:
                    new_source = new_source.replace(
                        'from openinference.instrumentation.openai import OpenAIInstrumentor', 
                        'from openinference.instrumentation.groq import GroqInstrumentor'
                    )
                if 'OpenAIInstrumentor' in new_source:
                    new_source = new_source.replace('OpenAIInstrumentor', 'GroqInstrumentor')
                
                # 3. Agent Model
                if 'agno.models.openai' in new_source:
                    new_source = new_source.replace(
                        'from agno.models.openai import OpenAIChat', 
                        'from agno.models.groq import Groq'
                    )
                
                if 'OpenAIChat' in new_source:
                    # Replace with Groq model
                    new_source = re.sub(r'OpenAIChat\(.*?\)', 'Groq(id="llama-3.3-70b-versatile")', new_source)

                # 4. Turn off streaming (safer for first run/debugging)
                if 'stream = True' in new_source:
                    new_source = new_source.replace('stream = True', 'stream = False')

                # 5. Set Keys (Hardcode for ease of use as requested)
                if 'os.environ["OPENAI_API_KEY"]' in new_source:
                    new_source = new_source.replace('OPENAI_API_KEY', 'GROQ_API_KEY')
                    new_source = new_source.replace('Enter your OpenAI API Key', 'Enter your Groq API Key')
                
                for key, value in keys_map.items():
                    # Direct replacement for keys setup block
                    if f'os.environ["{key}"]' in new_source:
                        pattern = f'os.environ\\["{key}"\\].*?getpass\\(.*?\\)'
                        replacement = f'os.environ["{key}"] = "{value}"'
                        # First try regex replacement of the getpass line
                        new_source_mod = re.sub(pattern, replacement, new_source)
                        if new_source_mod == new_source:
                           # Fallback if regex didnt match strict getpass pattern (maybe original file dif)
                           # Just naive replace
                           pass
                        else:
                           new_source = new_source_mod
                
                # Special case for OpenAI key replacement to Groq Key if regex didn't catch it
                if 'GROQ_API_KEY' in new_source and 'getpass' in new_source:
                     pattern = r'os.environ\["GROQ_API_KEY"\].*?getpass\(.*?\)'
                     replacement = f'os.environ["GROQ_API_KEY"] = "{keys_map["GROQ_API_KEY"]}"'
                     new_source = re.sub(pattern, replacement, new_source)


                cell.source = new_source

        with open(notebook_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print("SUCCESS: Migrated notebook to Groq.")

    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    migrate_to_groq('lab1and2_groq_agent.ipynb')
