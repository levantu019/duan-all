// Functions
// Create random color
function randomColor(num) {
    var colors = [];
    for(let i = 0; i < num; i++) {
        colors.push("#" + Math.floor(Math.random()*16777215).toString(16));
    }

    return colors;
}

// Detail tooltip (%)
var test;
function tooltip_details(tooltipItems){
    test = tooltipItems;
    let label = `Tên trang bị: ${tooltipItems.label}`;
    let amount = `Số lượng: ${tooltipItems.dataset.origin_data[tooltipItems.dataIndex]}/${tooltipItems.dataset.origin_data.reduce((previousValue, currentValue) => previousValue + currentValue,)}`;
    let ratio = `Tỉ lệ: ${tooltipItems.parsed.toFixed(2)} %`;
    return [label, amount, ratio];
}

// 
function handleHover(evt, item, legend) {
    legend.chart.data.datasets[0].backgroundColor.forEach((color, index, colors) => {
        colors[index] = index === item.index || color.length === 9 ? color : color + '4D';
    });
    legend.chart.update();
}

// 
function handleLeave(evt, item, legend) {
    legend.chart.data.datasets[0].backgroundColor.forEach((color, index, colors) => {
        colors[index] = color.length === 9 ? color.slice(0, -2) : color;
    });
    legend.chart.update();
}


// Create chart
function createBarChart(canvasID, data, colors, title) {
    const ctx = document.getElementById(canvasID).getContext('2d');
    let labels = Object.keys(data);

    const myChart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "Số lượng",
                data: data,
                backgroundColor: colors,

            }]
        },
        options: {
            plugins: {
                title: {
                    display: true,
                    text: `Biểu đồ số lượng trang bị theo ${title}`
                },
                legend: false,
                tooltip: {
                    callbacks:{
                        label: tooltip_details,
                    }
                }
            },
            responsive: true
        }
    });

    return myChart;
}

function createPieChart(canvasID, data, colors, title) {
    const ctx = document.getElementById(canvasID).getContext('2d');
    let labels = Object.keys(data);

    let total = 0;
    let values = [];
    for (let key in data) {
        total+=data[key];
        values.push(data[key]);
    }
    let values_ratio=values.map(value=>value*100/total);

    const myChart = new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: labels,
            datasets: [{
                label: "Phần trăm",
                data: values_ratio,
                backgroundColor: colors,
                origin_data: values
            }]
        },
        options: {
            plugins: {
                title: {
                    display: true,
                    text: `Biểu đồ số lượng trang bị khí tài theo ${title}`
                },
                legend: {
                    display:true,
                    onClick: false,
                    position:"right",
                    title: {
                        display: true,
                        text: "Chú thích",
                        font: {
                            size: 16,
                            weight: 900,
                        }
                    },
                    onHover: handleHover,
                    onLeave: handleLeave
                },
                tooltip: {
                    callbacks:{
                        label: tooltip_details,
                    }
                }
            },
            aspectRatio: 2
        }
    });

    return myChart;
}



//Biến lưu các instances của chartjs 
let charts = {
    "cap-don-vi" : null,
    "nhom-don-vi": null,
    "don-vi-ql" : null,
    "loai-trang-bi" : null,
    "xuat-xu" : null,
    "nam-sx" : null,
    "tinh-trang-hd" : null,
    "cap-do-chlg" : null
}

//Biến định nghĩa tên biểu đồ
const NAME_CHART = {
    "cap-don-vi" : "cấp đơn vị",
    "nhom-don-vi": "nhóm đơn vị",
    "don-vi-ql" : "đơn vị quản lý",
    "loai-trang-bi" : "loại trang bị",
    "xuat-xu" : "xuất xứ",
    "nam-sx" : "năm sản xuất",
    "tinh-trang-hd" : "tình trạng hoạt động",
    "cap-do-chlg" : "phân cấp chất lượng"
}

function createPieCharts() {
        for(key in charts) {
            if(charts[key]) charts[key].destroy();  

            //Gọi API lấy dữ liệu
            // GET `http://prefix/${key}`
            let data = {"BQP":3,"Trực thuộc bộ":3,"Trực thuộc học viện":12}
            charts[key] = createPieChart(`chart-${key}`,data, randomColor(Object.keys(data).length), NAME_CHART[key]);
        }   
}

function createBarCharts() {
    for(key in charts) {
        if(charts[key]) charts[key].destroy();      
        
        //Gọi API 
        // GET `http://prefix/${key}`
        let data = {"BQP":3,"Trực thuộc bộ":3,"Trực thuộc học viện":12}
        charts[key] = createBarChart(`chart-${key}`,data, randomColor(Object.keys(data).length), NAME_CHART[key]);
    }
}