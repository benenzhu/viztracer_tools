import typer
import re
import json

app = typer.Typer()

@app.command()
def hello():
    """
    Filter out specific patterns from traceEvents in a JSON file.
    Creates a new file with '_new.json' suffix.
    """
    input_file = "result.json"
    output_file = "result_new.json"
    
    # Read the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Filter out entries matching specific patterns
    filtered_events = []
    
    # Patterns to filter out using regex
    patterns_to_filter = [
        r'builtins\.print',  # Matches "builtins.print"
        r'ignore_func.*basecode\.py',  # Matches "ignore_func" from basecode.py
    ]
    
    # Compile patterns for better performance
    compiled_patterns = [re.compile(pattern) for pattern in patterns_to_filter]
    
    # Filter the traceEvents
    if 'traceEvents' in data:
        for event in data['traceEvents']:
            # Skip if event is not a string
            # Check if event matches any of our patterns
            should_include = True
            # print()
            for pattern in compiled_patterns:
                if pattern.search(event["name"]):
                    should_include = False
                    # print("not include")
                    break
            
            if should_include:
                filtered_events.append(event)
        
        # Update the data with filtered events
        data['traceEvents'] = filtered_events
    
    # Write to new file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Successfully filtered {len(data.get('traceEvents', []))} events")
    print(f"Output written to: {output_file}")
        

if __name__ == "__main__":
    app()