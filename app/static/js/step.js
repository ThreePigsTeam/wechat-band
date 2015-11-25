function drawstep(stepsdata){
    require.config({
        paths: {
            echarts: 'http://echarts.baidu.com/build/dist'
        }
    });
        
    // 使用
    require(['echarts', 'echarts/chart/line'], function (ec) {
            // 基于准备好的dom，初始化echarts图表
        var myChart = ec.init(document.getElementById('main')); 
                
        var option = {
                title : {
                    text: '近一周每日步数'
                },
                tooltip : {
                    trigger: 'axis'
                },
                legend: {
                    data:['步数']
                },
                calculable : true,
                xAxis : [{
                    type : 'category',
                    boundaryGap : false,
                    data : ['周一','周二','周三','周四','周五','周六','周日'],
                    axisLabel: {
                        show: true,
                        textStyle: {
                            fontSize: 30,
                        }
                    }
                }],
                yAxis : [{
                    type : 'value',
                    axisLabel: {
                        show:true,
                        textStyle: {
                            fontSize: 25,
                        }
                    }
                }],
                series : [{
                    name:'当日步数',
                    type:'line',
                    data: stepsdata,
                    markPoint : {
                        data : [{type : 'max', name: '最大值'},
                            {type : 'min', name: '最小值'}]
                    },
                    markLine : {
                        data : [{type: 'average', name: '平均值'}],
                        itemStyle: {
                            normal: {
                                label: {
                                    textStyle: {
                                        fontSize:25
                                    },
                                },
                            },
                            emphasis: {
                                label: {
                                    textStyle: {
                                        fontSize: 25
                                    },
                                },
                            },
                        },
                    }
                }]
            };
        myChart.setOption(option); 
    });
};