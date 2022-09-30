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
