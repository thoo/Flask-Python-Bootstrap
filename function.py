from bokeh.plotting import figure, output_file , show
import json
from bokeh.charts import Bar,Histogram,BoxPlot,Scatter
from bokeh.io import push_notebook, show, output_notebook
from bokeh.layouts import column
from bokeh.models import HoverTool, BoxSelectTool,Legend
from bokeh.embed import components
import quandl as ql
from bokeh.palettes import viridis,inferno,magma,brewer,d3
from quandl.errors.quandl_error import NotFoundError
from bokeh.resources import CDN
from bokeh.embed import components

wwdi_dist=json.load(open('dict_data/plot_dict.txt'))
quandl_api_key= json.load(open('.key')) # Api key is saved in .key file.
ql.ApiConfig.api_key=quandl_api_key["Quardl_API_Key"]




head = """
<link rel="stylesheet"
 href="https://cdn.pydata.org/bokeh/release/bokeh-0.12.4.min.css"
 type="text/css" />
<script type="text/javascript"
 src="https://cdn.pydata.org/bokeh/release/bokeh-0.12.4.min.js">
</script>
<script type="text/javascript">
Bokeh.set_log_level("info");
</script>
"""


APEC=[u'Australia',
 u'Brunei Darussalam',
 u'Canada',
 u'Chile',
 u'China',
 u'Hong Kong SAR, China',
 u'Indonesia',
 u'Japan',
 u'Korea, Dem. Rep.',
 u'Korea, Rep.',
 u'Malaysia',
 u'Mexico',
 u'Namibia',
 u'New Zealand',
 u'Papua New Guinea',
 u'Peru',
 u'Philippines',
 u'Russian Federation',
 u'Singapore',
 u'Thailand',
 u'United States'
]




ASEAN=['Brunei Darussalam',
 'Cambodia',
 'Indonesia',
 'Lao PDR',
 'Malaysia',
 'Myanmar',
 'Philippines',
 'Singapore',
 'Thailand',
 'Vietnam']



ASEAN_color=['#a6cee3','#1f78b4','#b2df8a','#33a02c','#fb9a99','#e31a1c','#fdbf6f','#ff7f00','#cab2d6','#6a3d9a','#ffff99','#b15928']
APTA=['Bangladesh', 'China', 'India', 'Korea, Rep.', 'Lao PDR', 'Sri Lanka']
APTA_color=['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#ffff33']
group_dict={'APTA':APTA,'ASEAN':ASEAN,'APEC':APEC}
color=d3['Category20'][20]
country_dict=json.load(open('dict_data/country_dict.txt'))
#wwdi_dist={"GDP growth (annual %)":"NY_GDP_MKTP_KD_ZG","GDP per capita (current US$)":"NY_GDP_PCAP_CD"}


def GDP_PCA_plot(country=['ASEAN'],plot_name=["GDP per capita (current US$)"]):



    return_list=[]

    return_list.append(head)

    for p_name in plot_name:


        TOOLS="crosshair,pan,wheel_zoom,box_zoom,reset,hover,save"
        p1 = figure(width=800, height=400,title=p_name, \
                    tools=TOOLS,\
                    toolbar_location="below",toolbar_sticky=False,\
                    responsive=True)



        new_list=[]

        for i in country:
            if i == 'ASEAN':
                new_list.extend(group_dict[i])

            if i == 'APTA':
                new_list.extend(group_dict[i])

            if i == 'APEC':
                new_list.extend(group_dict[i])

            if i != 'ASEAN' and i != 'APTA' and i != 'APEC':
                new_list.append(i)


        new_list=list(set(new_list))



        color_len=len(new_list)

        if color_len < 7:
            color_dict=dict(zip(new_list,APTA_color[:color_len]))

        if color_len > 6 and color_len < 13:
            color_dict=dict(zip(new_list,ASEAN_color[:color_len]))

        if color_len > 12:
            color_dict=dict(zip(new_list,viridis(color_len)))

        #print(new_list)
        my_legend=[]
        for i in new_list:
            try:
                data=ql.get("WWDI/"+country_dict[i]+"_"+wwdi_dist[p_name])

                data=data.reset_index()

                #print(data.head())
                #p1.circle(data.ix[:,0].dt.year,data.ix[:,1],legend=i,color=color,size=4)
                my_plot=p1.line(data.ix[:,0].dt.year,data.ix[:,1].values,color=color_dict[i],line_width=3)
                my_legend.append((i,[my_plot]))
                label=data.columns
            except NotFoundError:
                pass

        legend=Legend(items=my_legend,location=(0,-48))

        p1.title.text_font_size = '20pt'
        p1.xaxis.axis_label = data.columns[0]
        p1.yaxis.axis_label = data.columns[1]
        p1.xaxis.axis_label_text_font_size = "14pt"
        p1.yaxis.axis_label_text_font_size = "14pt"
        p1.add_layout(legend, 'right')






        #plots = {'Navy': p1, 'Blue': p2};
        tuple_plot = components(p1);
        #script2, div2 = components(p2);


        return_list.append(list(tuple_plot))


    return return_list
