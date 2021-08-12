#https://dash-gallery.plotly.host/dash-lastodash-de/ want something like this 
#https://medium.com/swlh/dashboards-in-python-using-dash-creating-a-data-table-using-data-from-reddit-1d6c0cecb4bd - how to format tables

# Importing modules
import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np
from natsort import natsorted

# Reading in data
df = pd.read_table("/Users/connormadden/Desktop/directory/assets/total_dataframe_repeat_clinvar_omim_annotation", skiprows = 1, names=["Chr", "Start", "End", "Strand", "Gene ID", "Gene Name", "Exon(s)", "Mean Cov", "% x15", "Repeat", "No Path Variants", "Phenotypes"])

# Re-ordering columns
df = df.loc[:,['Gene Name', 'Gene ID', 'Exon(s)', 'Chr', 'Start', 'End', 'Strand', 'Mean Cov', '% x15', 'Repeat', 'No Path Variants', 'Phenotypes']]

# Rounding all data to 2 dp
df = df.round(decimals=2)

# Naturally sorting columns
df.Chr = natsorted(df.Chr)

# Creating histogram dataframe

df1 = df.loc[:,['Mean Cov', '% x15']]

markdown_text = '''
**If a region of interest has a low seqeuncing coverage, you may find it useful to refer to the [Genomics England panel resource](https://nhsgms-panelapp.genomicsengland.co.uk/panels) to select a suitable panel to increase sequencing coverage.**
'''

##### Creating application

# Creating dash application in current module
app = dash.Dash(__name__)

# Defining column data types
# Stating python must be at least version 3.0
def table_type(df_column):
	if sys.version_info < (3, 0):
		return 'any'
	# Stating that if the column type is a string, boelean, categorical or period data type it is tezt
	if (isinstance(df_column.dtype, pd.StringDtype) or
			isinstance(df_column.dtype, pd.BooleanDtype) or
			isinstance(df_column.dtype, pd.CategoricalDtype) or
			isinstance(df_column.dtype, pd.PeriodDtype)):
		return 'text'
	# Stating that if the column type is sparse, interval or any integer data type, it is numeric data
	elif (isinstance(df_column.dtype, pd.SparseDtype) or
			isinstance(df_column.dtype, pd.IntervalDtype) or
			isinstance(df_column.dtype, pd.Int8Dtype) or
			isinstance(df_column.dtype, pd.Int16Dtype) or
			isinstance(df_column.dtype, pd.Int32Dtype) or
			isinstance(df_column.dtype, pd.Int64Dtype)):
		return 'numeric'
	else:
		return 'any'

### Setting app layout
app.layout = html.Div([
	# Setting the background image at the top of the app
	html.Img(src='/assets/background.png', style={'textAlign': 'center'}),
	# Creating header
	html.H1(
	children='WINGS Exome Coverage Tool: A web application framework for exploring WGS coverage', className='app-header--title',
	style={
	'fontSize': 50,
	'fontFamily': 'arial',
	'textAlign': 'center'
	}
	),
	# Creating a sub header
	html.H2('''
	To remove a column, select the bin symbol within the header of choice. To sort columns from low to high or high to low, select the down or up arrows within the header of choice. To filter by word or value, use the empty boxes below each header however please note, if what you're searching for contains a special character (such as a space), it must be wrapped in quotation marks. To remove rows, use the cross beside each row. To return to an unaltered version of the data table, please refresh your browser.''',
	style={
	'fontSize': 30,
	'fontFamily': 'arial',
	'textAlign': 'left'
	}
	),
	dcc.Markdown(children=markdown_text,
	style={
	'fontSize': 30,
	'fontFamily': 'arial',
	'textAlign': 'left',
	}),
	# Creating a table component with the ID table
	dash_table.DataTable(id='coverage_table_container',
	style_header={
	'whiteSpace': 'normal',
	'height': 'auto',
	'font_family': 'arial',
	'font_size': '25px',
	'text_align': 'center',
	'font_weight': 'bold',
	'background_color': 'lightcyan',
#	'textDecoration': 'underline',
#	'border': '1px solid black',
	},
	# Creating a conditonal highlight for all odd rows to make it easier to distinguish between rows and 
	# another codition to highlight regions with a min coverage less than x20
	style_data_conditional=[
	{
	'if': {'row_index': 'odd'},
	'background_color': 'gainsboro'
	},
	{
	'if': {
	'filter_query': '{Mean Cov} lt 20'
	},
	'background_color': 'red',
	'font_weight': 'bold',
	'color' : 'white'
	},
	],
	# Setting the data cell conditions
	style_data={
	'whiteSpace': 'normal',
	'height': 'auto',
	'font_family': 'arial',
	'font_size': '25px',
	'text_align': 'center',
#	'border': '1px solid black',
	},
	# Setting table height and setting scroll option
	style_table={
#	'height': '3000px',
	'overflowY': 'auto',
	'overflowX': 'auto'
	},
	# Setting column sizes
	style_cell_conditional=[
	{'if': {'column_id': 'Gene Name'},
	'width': '8%'},
	{'if': {'column_id': 'Gene ID'},
	'width': '11%'},
	{'if': {'column_id': 'Exon(s)'},
	'width': '6%'},
	{'if': {'column_id': 'Chr'},
	'width': '3%'},
	{'if': {'column_id': 'Start'},
	'width': '8%'},
	{'if': {'column_id': 'End'},
	'width': '8%'},
	{'if': {'column_id': 'Strand'},
	'width': '6%'},
	{'if': {'column_id': 'Mean Cov'},
	'width': '5%'},
	{'if': {'column_id': '% x15'},
	'width': '5%'},
	{'if': {'column_id': 'Repeat'},
	'width': '17%'},
	{'if': {'column_id': 'No Path Variants'},
	'width': '8%'},
	{'if': {'column_id': 'Phenotypes'},
	'width': '15%'}],
	# This will keep the headers visible throughout scrolling. Currently several limitations that cause poor formatting (https://dash.plotly.com/datatable/height), but may be useful in future.
#	fixed_rows={'headers': True},
	# For loop to use all data in df dataframe to create table
	columns=[{"name": i, "id": i, "deletable": True, "selectable": True} for i in df.columns],
	# This will set the style of the app to a list ie no column lines
#	style_as_list_view=True,
	# Converting data to a dictionary so it is easier to access
	data=df.to_dict('records'),
	# Allows editing of cells
	editable=True,
	# Allows filtering by column
	filter_action="native",
	# This will style the filter. Currently a fault with no workaround (https://community.plotly.com/t/dash-datatable-style-filter-doesnt-seem-to-work/15691/5) but may be useful in the future. 
#	style_filter={
#	'whiteSpace': 'normal',
#	'height': 'auto',
#	'font_family': 'arial',
#	'font_size': '25px',
#	'text_align': 'center',
#	'background_color': 'blue'},
	# Allows sorting by column
	sort_action="native",
	# Allows multiple sort conditions at one time
	sort_mode="multi",
	# Allows columns to be selected
	column_selectable="single",
	# Allows rows to be selected
	row_selectable="multi",
	# Allows rows to be deleted
	row_deletable=True,
	# Creates an open array for selected columns
	selected_columns=[],
	# Creates an open array for selected rows
	selected_rows=[],
	# Puts first page first
	page_action="native",
	page_current= 0,
	# Sets number of rows per page
	page_size= 20,
	# Adding a tooltip enlargement for the header
	tooltip_header={
	'Gene Name': 'Gene Name',
	'Chr': 'Chromosome',
	'Gene ID': 'Gene ID (Ensemble)',
	'Exon(s)': 'Exon(s) within region',
	'Start': 'Start Co-ordinate',
	'End': 'End Co-ordinate',
	'Strand': 'Strand',
	'Mean Cov': 'Mean Coverage (n = 161)',
	'% x15': 'Percentage Coverage above x15 (n = 161)',
	'Repeat': 'Repeat Class (RepeatMasker)',
	'No Path Variants': 'Number of Pathogenic Variants (Clinvar)',
	'Phenotypes': 'Phenotypes (OMIM)'
	},
	# CSS to overight the tooltip header settings
	css=[{
	'selector': '.dash-table-tooltip',
	'rule': 'background-color: white; font-family: arial; font-size: 30px'
	}]),
	# Creating a tooltip conditional
#	tooltip_conditional=[
#	{
#	'if': {
#	'filter_query': '{Mean Coverage} lt 20'
#	},
#	'type': 'markdown',
#	'value': 'This region has low coverage'
#	}
#	]),
	# Tooltip option to zoom in on regions. Can be used to highlight various regions but does slow down app.
#	tooltip_data=[
#	{
#	column: {'value': str(value), 'type': 'markdown'}
#	for column, value in row.items()
#	} for row in df.to_dict('records')
#	],
#	tooltip_delay=0,
#	tooltip_duration=None),
	html.H3(
	children='Select coverage metric for histogram',
	style={
	'fontSize': 30,
	'fontFamily': 'arial',
	'textAlign': 'left'
	}
	),
	dcc.Dropdown(
		id='xaxis',
		options=[{'value': x, 'label': x}
			for x in ['Mean Cov', '% x15']],
		value='Mean Cov',
	style={'display': 'block',
	'width': '40%',
	'fontSize': 25,
	'fontFamily': 'arial',
	'textAlign': 'left',
#	'backgroundColor': 'lightcyan',
	'fontWeight': 'bold',}
	),
	dcc.Graph(id='histogram'),
	html.H3(
	children='Select coverage metric for boxplot',
	style={
	'fontSize': 30,
	'fontFamily': 'arial',
	'textAlign': 'left'
	}
	),
	dcc.Dropdown(
		id='yaxis',
		options=[{'value': x, 'label': x}
			for x in ['Mean Cov', '% x15']],
		value='Mean Cov',
	style={'display': 'block',
	'width': '40%',
	'fontSize': 25,
	'fontFamily': 'arial',
	'textAlign': 'left',
#	'backgroundColor': 'lightcyan',
	'fontWeight': 'bold',}
	),
	dcc.Graph(id='box'),
])

@app.callback(
	Output(component_id='histogram', component_property='figure'),
	Input(component_id='xaxis', component_property='value'))
def display_color(xaxis):
	fig = px.histogram(df, x=xaxis, nbins=400, range_x=[0, 100], color_discrete_sequence=['red'])
	fig.update_layout(
	font=dict(
	family="Arial",
	size=25,
	),
	title={
	'y':0.9,
	'x':0.5,
	'xanchor': 'center',
	'yanchor': 'top'},
	width=2850,
	height=1000,
	margin=dict(l=20, r=20, t=20, b=20),
	paper_bgcolor="gainsboro",)
	return fig

@app.callback(
	Output(component_id='box', component_property='figure'),
	Input(component_id='yaxis', component_property='value'))
def display_color(yaxis):
	fig1 = px.box(df, x='Chr', y=yaxis, color='Chr')
	fig1.update_layout(
	font=dict(
	family="Arial",
	size=25,
	),
	title={
	'y':0.9,
	'x':0.5,
	'xanchor': 'center',
	'yanchor': 'top'},
	width=2850,
	height=1000,
	margin=dict(l=20, r=20, t=20, b=20),
	paper_bgcolor="gainsboro",)
	return fig1


### Executing app
if __name__ == '__main__':
	app.run_server(debug=True)
