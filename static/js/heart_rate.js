// 路径配置
        require.config({
            paths: {
                echarts: 'http://echarts.baidu.com/build/dist'
            }
        });

        // 使用
        require(
            [
                'echarts',
                'echarts/chart/line' // 使用柱状图就加载bar模块，按需加载
            ],
            function (ec) {
                // 基于准备好的dom，初始化echarts图表
                var myChart = ec.init(document.getElementById('main'));

                var option = {
                    title: {
                        text: '今日心率'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data: ['心率']
                    },
                    calculable: true,
                    xAxis: [
                        {
                            type: 'category',
                            boundaryGap: false,
                            data: ['0:00:00', '0:10:00', '0:20:00', '0:30:00', '0:40:00', '0:50:00',
                                   '1:00:00', '1:10:00', '1:20:00', '1:30:00', '1:40:00', '1:50:00',
                                   '2:00:00', '2:10:00', '2:20:00', '2:30:00', '2:40:00', '2:50:00',
                                   '3:00:00', '3:10:00', '3:20:00', '3:30:00', '3:40:00', '3:50:00',
                                   '4:00:00', '4:10:00', '4:20:00', '4:30:00', '4:40:00', '4:50:00',
                                   '5:00:00', '5:10:00', '5:20:00', '5:30:00', '5:40:00', '5:50:00',
                                   '6:00:00', '6:10:00', '6:20:00', '6:30:00', '6:40:00', '6:50:00',
                                   '7:00:00', '7:10:00', '7:20:00', '7:30:00', '7:40:00', '7:50:00',
                                   '8:00:00', '8:10:00', '8:20:00', '8:30:00', '8:40:00', '8:50:00',
                                   '9:00:00', '9:10:00', '9:20:00', '9:30:00', '9:40:00', '9:50:00',
                                   '10:00:00', '10:10:00', '10:20:00', '10:30:00', '10:40:00', '10:50:00',
                                   '11:00:00', '11:10:00', '11:20:00', '11:30:00', '11:40:00', '11:50:00',
                                   '12:00:00', '12:10:00', '12:20:00', '12:30:00', '12:40:00', '12:50:00',
                                   '13:00:00', '13:10:00', '13:20:00', '13:30:00', '13:40:00', '13:50:00',
                                   '14:00:00', '14:10:00', '14:20:00', '14:30:00', '14:40:00', '14:50:00',
                                   '15:00:00', '15:10:00', '15:20:00', '15:30:00', '15:40:00', '15:50:00',
                                   '16:00:00', '16:10:00', '16:20:00', '16:30:00', '16:40:00', '16:50:00',
                                   '17:00:00', '17:10:00', '17:20:00', '17:30:00', '17:40:00', '17:50:00',
                                   '18:00:00', '18:10:00', '18:20:00', '18:30:00', '18:40:00', '18:50:00',
                                   '19:00:00', '19:10:00', '19:20:00', '19:30:00', '19:40:00', '19:50:00',
                                   '20:00:00', '20:10:00', '20:20:00', '20:30:00', '20:40:00', '20:50:00',
                                   '21:00:00', '21:10:00', '21:20:00', '21:30:00', '21:40:00', '21:50:00',
                                   '22:00:00', '22:10:00', '22:20:00', '22:30:00', '22:40:00', '22:50:00',
                                   '23:00:00', '23:10:00', '23:20:00', '23:30:00', '23:40:00', '23:50:00', ],
                            axisLabel: {
                                show: true,
                                textStyle: {
                                    fontSize: 25,
                                }
                            }
                        }
                    ],
                    yAxis: [
                        {
                            type: 'value',
                            axisLabel: {
                                show: true,
                                textStyle: {
                                    fontSize: 25,
                                }
                            }
                        }
                    ],
                    series: [
                        {
                            name: '心率',
                            type: 'line',
                            data: {{ data }},
                            markPoint: {
                                data: [
                                    { type: 'max', name: '最大值' },
                                    { type: 'min', name: '最小值' }
                                ]
                            },
                            markLine: {
                                data: [
                                    {
                                        type: 'average',
                                        name: '平均值',
                                    }
                                ],
                                itemStyle: {
                                    normal: {
                                        label: {
                                            textStyle: {
                                                fontSize: 25
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
                        }
                    ]
                };

                // 为echarts对象加载数据 
                myChart.setOption(option);
            }
        );