from dash import Dash, html, dcc, Output, Input # Added Output and Input

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Hello from Dash!"),
    html.P("This is a simple Dash application."),
    dcc.Input(id='my-input', value='World', type='text'),
    html.Div(id='my-output')
])

@app.callback(
    Output('my-output', 'children'), # Corrected this line
    [Input('my-input', 'value')]     # Corrected this line as well for consistency, though the previous one might have worked
)
def update_output_div(input_value):
    return f'Hello, {input_value}!'

if __name__ == '__main__':
    app.run(debug=True) # Corrected from app.run_server to app.run
