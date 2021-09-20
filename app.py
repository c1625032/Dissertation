# Importing modules
import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from natsort import natsorted
import numpy as np

# Reading in data frame
df = pd.read_table("/Users/connormadden/Desktop/directory/assets/total_dataframe_repeat_clinvar_omim_annotation", skiprows = 1, names=["Chr", "Start", "End", "Strand", "Gene ID", "Gene Name", "Exon(s)", "Mean Cov", "% x15", "Repeat", "No Path Variants", "Phenotypes"])

# Re-ordering columns
df = df.loc[:,['Gene Name', 'Gene ID', 'Exon(s)', 'Chr', 'Start', 'End', 'Strand', 'Mean Cov', '% x15', 'Repeat', 'No Path Variants', 'Phenotypes']]

# Rounding all data to 2 dp
df = df.round(decimals=2)

# Naturally sorting columns
df.Chr = natsorted(df.Chr)

# Creating histogram dataframe
df1 = df.loc[:,['Mean Cov', '% x15']]

# Creating markdown text object
markdown_text1 = '''
**If a region of interest has a low seqeuncing coverage, you may find it useful to refer to the [Genomics England panel resource](https://nhsgms-panelapp.genomicsengland.co.uk/panels) to select a suitable panel to increase sequencing coverage.**
'''

# Creating markdown text object
markdown_text2 = '''
**If more information is needed regarding a gene, the following sites may be useful: [Ensembl](http://www.ensembl.org/index.html), [UCSC genome browser](https://genome-euro.ucsc.edu/cgi-bin/hgGateway), [OMIM](https://omim.org) and [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/).**
'''

# Creating markdown text object
markdown_text3 = '''
**The following sites may be helpful when comparing coverage data in the event of a negative test: [gnomAD coverage browser](https://gnomad.broadinstitute.org), [eurofins coverage tool](https://www.egl-eurofins.com/exome-coverage/search-results.php) and [Exeter Clinical Labratory exome coverage tool](http://www.exeterlaboratory.com/test/exome-sequencing-services/) (found at the bottom of page).**
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
	# Creating header and styling
	html.H1(
	children='WINGS Exome Coverage Tool: A web application framework for exploring WGS coverage', className='app-header--title',
	style={
	'fontSize': 50,
	'fontFamily': 'arial',
	'textAlign': 'center'
	}
	),
	# Creating sub-header and styling
	html.H2('''
	To remove a column, select the bin symbol within the header of choice. To sort a column from low to high or high to low, select the down or up arrows within the header of choice. To filter rows, use the empty boxes below each header by typing in the letters or values of interest. If you wish to filter by value use > or <. Please note, if word of interest contains a special character (such as a space), it must be wrapped in quotation marks. To remove rows, use the cross beside each row. To copy information within a cell, click on the cell and use the copy command on your keyboard (mac = cmd + c, windows = ctrl + c). To return to an unaltered version of the data table, please refresh your browser.''',
	style={
	'fontSize': 30,
	'fontFamily': 'arial',
	'textAlign': 'left'
	}
	),
	# Inserting markdown text and styling
	dcc.Markdown(children=markdown_text1,
	style={
	'fontSize': 30,
	'fontFamily': 'arial',
	'textAlign': 'left',
	}),
	# Inserting markdown text and styling
	dcc.Markdown(children=markdown_text2,
	style={
	'fontSize': 30,
	'fontFamily': 'arial',
	'textAlign': 'left',
	}),
	# Inserting markdown text and styling
	dcc.Markdown(children=markdown_text3,
	style={
	'fontSize': 30,
	'fontFamily': 'arial',
	'textAlign': 'left',
	}),
	# Creating table component
	dash_table.DataTable(id='coverage_table_container',
	# Styling the header
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
	# Creating one conditonal argument to highlight all odd rows and another to highlight regions with a min coverage less than x20
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
	# Styling data cells
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
	# for loop to use all data in df dataframe to create table
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
#	column_selectable="single",
	# Allows rows to be selected
#	row_selectable="multi",
	# Allows rows to be deleted
	row_deletable=True,
	# Creates an open array for selected columns
#	selected_columns=[],
	# Creates an open array for selected rows
#	selected_rows=[],
	# Puts first page first
	page_action="native",
	page_current= 0,
	# Sets number of rows per page
	page_size= 20,
	# Adding a tooltip enlargement for the header to add additonal information
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
	# Creating a tooltip conditional to highlight regions with coverage below x20, currently faulty but may be useful in future. 
#	tooltip_conditional=[
#	{
#	'if': {
#	'filter_query': '{Mean Coverage} lt 20'
#	},
#	'type': 'markdown',
#	'value': 'This region has low coverage'
#	}
#	]),
	# Tooltip option to zoom in on regions. Can be used to highlight various regions but does slow down app considerably do disabled.
#	tooltip_data=[
#	{
#	column: {'value': str(value), 'type': 'markdown'}
#	for column, value in row.items()
#	} for row in df.to_dict('records')
#	],
#	tooltip_delay=0,
#	tooltip_duration=None),
	# Header above histogram and styling
	html.H3(
	children='Select coverage metric for histogram',
	style={
	'fontSize': 30,
	'fontFamily': 'arial',
	'textAlign': 'left'
	}
	),
	# Dropdown option for histogram
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
	# Histogram
	dcc.Graph(id='histogram'),
	html.H3(
	children='Select coverage metric for boxplot',
	style={
	'fontSize': 30,
	'fontFamily': 'arial',
	'textAlign': 'left'
	}
	),
	# Dropdown option for boxplot
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
	# Boxplot
	dcc.Graph(id='box'),
])

# Creating callback to have reactive histogram
@app.callback(
	Output(component_id='histogram', component_property='figure'),
	Input(component_id='xaxis', component_property='value'))
# Creating histogram and styling
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

# Creating callback to have reactive boxplot
@app.callback(
	Output(component_id='box', component_property='figure'),
	Input(component_id='yaxis', component_property='value'))
# Creating boxplot and styling
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
