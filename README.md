# PlotlyAndDash

# Introduction
1. Những công cụ để hiển thị data dùng python
    - Matplotlib: chỉ hiển thị những ảnh tĩnh
    - Seaborn: để hiển thị thống kê đẹp hơn trên nền matplotlib
    - Pandas: chủ yếu dùng để phân tích dữ liệu. Dùng matplotlib khi gọi .plots()

# Plotly
1. Reference: https://plotly.com/python/
2. Là tên của công ty và open-source library
    - Công ty Plotly chuyên cung cấp những giải pháp về visualization for business intelligence
    - Open-source library: focused on interactive visualizations. Có libraries cho javascript, react, R and Python. Phổ biến nhất là thư viện cho python
Overview về open-source plotly. Creates interactive plots as .html files. Interact with these plots (zoom in, select, hover over), these plots can’t be connected to changing data sources
Once the interactive plotly plot is generated, the data is “locked in”. Để update data, phải chạy lại file python
Overview Dash

# Dash
1. Reference: https://dash.plotly.com/
1. Dash is an open-source renders a full web app, you can then deploy your dashboards online
Dash apps are composed of two parts
    - the first part: layout the app
    - the second part: interactivity of the application
    - you don't need to know any HTML or CSS to use Dash. Most html tags are provided as 
Python classes. 
    - Dash offers two distinct component libraries
        - dash_html_components
        - dash_core_components: higher-level , interactive components that are generated
   with JavaScript, HTML, and CSS through the React.js library
1. Basic Dash
    - Dash allows us to easily insert plotly graphs into the Dashboard
    - dash can use with markdown text
    - using help() function to see manual
2. Dash Callbacks
    - the way to interact and connect html and core components through the use of 
    callbacks
    - 
    
