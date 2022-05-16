
# Input: file name
#   structure:  Name structure: text/text_title_plot_metric.csv
# 
# Output: dict{title:,plot_name:,metric:}

def parse_file_name(file_name):
    # 
    # 

    name_split = file_name.split('/')
    #title = name_split[0]

    info = name_split[1].split('.')[0]
  
    name_info = info.split('_')
    
    title = name_info[1]
    plot_name = name_info[2]
    metric    = name_info[-1]

    return({'title':title,'plot_name':plot_name,'metric':metric})