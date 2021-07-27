#https://dash-gallery.plotly.host/dash-lastodash-de/ want something like this 
#https://medium.com/swlh/dashboards-in-python-using-dash-creating-a-data-table-using-data-from-reddit-1d6c0cecb4bd - how to format tables

# Importing modules
import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import base64

# Reading in data
df = pd.read_table("/Users/connormadden/Desktop/total_dataframe_repeat_clinvar_omim_annotation", skiprows = 1, names=["Chromosome", "Start", "End", "Strand", "Ensemble ID", "Gene Name", "Exon(s)", "Mean Coverage", "% Coverage at x15", "Repeat Class (RepeatMasker)", "Number of Pathogenic Variants (Clinvar)", "Phenotypes (OMIM)"])

# Creating object of image
image_filename = '/Users/connormadden/Desktop/background.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

# Re-ordering columns
df = df.loc[:,['Gene Name', 'Ensemble ID', 'Exon(s)', 'Chromosome', 'Start', 'End', 'Strand', 'Mean Coverage', '% Coverage at x15', 'Repeat Class (RepeatMasker)', 'Number of Pathogenic Variants (Clinvar)', 'Phenotypes (OMIM)']]
# Rounding all data to 2 dp
df = df.round(decimals=2)

##### Creating application

# Creating dash application in current module
app = dash.Dash(__name__)

### Setting app layout
app.layout = html.Div([
	html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'textAlign': 'center'}),
	# Creating header
	html.H1(
	children='WINGS Exome Coverage Tool: A web application framework for exploring WGS coverage',
	style={
	'fontSize': 50,
	'fontFamily': 'arial',
	'textAlign': 'left'
	}
	),
	# Creating a table component with the ID table
	dash_table.DataTable(id='table',
	# Using an overflow strategy to overflow some cells into multiple lines
	style_header={
	'whiteSpace': 'normal',
	'height': 'auto',
	'font_family': 'arial',
	'font_size': '25px',
	'text_align': 'center',
	'font_weight': 'bold',
	'background_color': 'lightskyblue',
	'border_color': 'black'
	},
	# Creating a conditonal highlight for regions with a min coverage less than x20
	style_data_conditional=[
	{
	'if': {'row_index': 'odd'},
	'background_color': 'gainsboro'
	},
	{
	'if': {
	'filter_query': '{Mean Coverage} lt 20'
	},
	'background_color': 'red',
	'font_weight': 'bold',
	'color' : 'white'
	},
	],
	style_data={
	'whiteSpace': 'normal',
	'height': 'auto',
	'font_family': 'arial',
	'font_size': '25px',
	'text_align': 'center',
	'border_color': 'black'
	},
	# Setting table height and setting scroll option
	style_table={
	'overflowY': 'scroll',
	'overflowX': 'auto'
	},
	# This will keep the headers visible throughout scrolling
#	fixed_rows={'headers': True},
	# For loop to use all data in df dataframe to create table
	columns=[{"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns],
	# This will set the style of the app to a list ie no colum lines
#	style_as_list_view=True,
	# Converting data to a dictionary so it is easier to access
	data=df.to_dict('records'),
	editable=True,
	filter_action="native",
	sort_action="native",
	sort_mode="multi",
	column_selectable="single",
	row_selectable="multi",
	row_deletable=True,
	selected_columns=[],
	selected_rows=[],
	page_action="native",
	page_current= 0,
	page_size= 100)
])

#@app.callback(
#	Output('table', 'style_data_conditional'),
#	Input('table', 'selected_columns')
#)

#def update_styles(selected_columns):
#	return [{
#		'if': { 'column_id': i },
#		'background_color': '#D2F3FF'
#	} for i in selected_columns]

### Executing app
if __name__ == '__main__':
	app.run_server(debug=True)
